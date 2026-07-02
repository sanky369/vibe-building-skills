# Performance Optimization — Implementation Gallery

Implementations for the strategies chosen in `../SKILL.md`.

## Optimistic UI patterns

Every optimistic mutation has three parts: immediate local update, background
request, rollback + notification on failure. Snapshot the previous state
before mutating so rollback is exact.

### Optimistic create

```javascript
// 1. Update UI immediately
const prevItems = items;
const newItem = { id: `tmp-${Date.now()}`, text: input.value };
setItems([...items, newItem]);
clearInput();

// 2. Send to server
const response = await fetch('/api/items', {
  method: 'POST',
  body: JSON.stringify(newItem),
});

// 3. Reconcile: swap temp id for server id, or roll back
if (response.ok) {
  const saved = await response.json();
  setItems((cur) => cur.map((i) => (i.id === newItem.id ? saved : i)));
} else {
  setItems(prevItems);
  showError('Failed to save');
}
```

### Optimistic delete

```javascript
const prevItems = items;
setItems(items.filter((item) => item.id !== id));

const response = await fetch(`/api/items/${id}`, { method: 'DELETE' });
if (!response.ok) {
  setItems(prevItems);          // restore
  showError('Failed to delete');
}
```

### Optimistic toggle (like/vote)

```javascript
const prev = { count, isLiked };
setLikeCount(isLiked ? count - 1 : count + 1);
setIsLiked(!isLiked);

const response = await fetch(`/api/items/${id}/like`, {
  method: 'POST',
  body: JSON.stringify({ liked: !isLiked }),
});
if (!response.ok) {
  setLikeCount(prev.count);
  setIsLiked(prev.isLiked);
  showError('Failed to update');
}
```

If the project uses TanStack Query / SWR / Apollo, implement optimistic
updates through their mutation APIs (`onMutate`/`onError` rollback with
snapshots) instead of hand-rolling state.

## Latency masking

### Skeleton screens

Placeholder mirroring the incoming layout — the brain builds a spatial map
while waiting, and matching dimensions prevent layout shift (CLS):

```html
<div class="card-skeleton" aria-hidden="true">
  <div class="skeleton skeleton-image" style="height: 200px;"></div>
  <div class="skeleton skeleton-text" style="width: 80%;"></div>
  <div class="skeleton skeleton-text" style="width: 60%;"></div>
</div>
```

Full skeleton CSS lives in
`skills/frontend-design/loading-states/references/patterns.md`.

### Blur-up images

```css
.image-blur  { filter: blur(20px); transition: opacity 300ms; }
.image-sharp { opacity: 0; transition: opacity 300ms; }
.image-sharp.loaded { opacity: 1; }
```

Reserve image dimensions (`width`/`height` attributes or `aspect-ratio`) so
the swap never shifts layout.

### Progressive enhancement

Render critical content first (server-rendered or cached); hydrate secondary
content (comments, recommendations) afterward into pre-reserved space.

### Staggered list entrances

Cascading entrances feel faster than a simultaneous pop-in:

```css
.list-item {
  animation: slideIn 300ms ease-out both;
}
.list-item:nth-child(1) { animation-delay: 0ms; }
.list-item:nth-child(2) { animation-delay: 50ms; }
.list-item:nth-child(3) { animation-delay: 100ms; }
.list-item:nth-child(4) { animation-delay: 150ms; }

@keyframes slideIn {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Cap total stagger (~300–400ms); respect `prefers-reduced-motion`.

## Anticipatory loading

```javascript
// Preload next page as the user approaches the bottom
const handleScroll = () => {
  if (isNearBottom()) preloadNextPage();
};

// Preload on hover intent (pointer enters a nav link / card)
const handleMouseEnter = () => {
  preloadUserProfile(userId);
};
```

Frameworks often provide this (Next.js `<Link>` viewport prefetch, router
prefetch APIs) — prefer the built-in.

## Network optimization

### Request batching

```javascript
// Instead of 5 serial fetches, one batched request
const data = await fetch('/api/batch', {
  method: 'POST',
  body: JSON.stringify({
    requests: ['user', 'posts', 'comments', 'likes', 'followers'],
  }),
});
```

Where the API can't batch, at minimum parallelize with `Promise.all` instead
of awaiting serially.

### Request deduplication

```javascript
const requestCache = new Map();

const fetchData = async (url) => {
  if (requestCache.has(url)) return requestCache.get(url); // in-flight reuse

  const promise = fetch(url).then((r) => r.json());
  requestCache.set(url, promise);
  try {
    return await promise;
  } finally {
    requestCache.delete(url);
  }
};
```

Data libraries (TanStack Query, SWR) do this automatically — another reason
to route fetches through them if already present.

## Measuring Core Web Vitals

Prefer the `web-vitals` npm package in production analytics. Raw observer
sketch for LCP:

```javascript
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const last = entries[entries.length - 1];
  console.log('LCP:', last.renderTime || last.loadTime);
});
observer.observe({ type: 'largest-contentful-paint', buffered: true });
```

Lab vs field: Lighthouse/devtools give lab numbers; CrUX / RUM give field
numbers. Judge against thresholds at the 75th percentile of field data when
available.

## Progress display

```javascript
// Real progress when total is known
setProgress((completed / total) * 100);
```

Show indeterminate progress plus explanatory text when the total is unknown.
Do not fabricate percentages or time estimates shown to users.
