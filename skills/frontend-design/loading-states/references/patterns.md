# Loading & Empty States — Implementation Gallery

Copy-adapt implementations. The decision rules (which state to use when) live
in `../SKILL.md`.

## Skeletons

```css
.skeleton {
  background: #e5e7eb;
  border-radius: 4px;
}

/* Animated shimmer */
.skeleton-animated {
  background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Building blocks */
.skeleton-text   { height: 16px; margin-bottom: 8px; }
.skeleton-avatar { width: 40px; height: 40px; border-radius: 50%; }
.skeleton-image  { width: 100%; aspect-ratio: 16/9; }
```

```html
<!-- Card skeleton mirroring the real card's layout -->
<article class="card card-skeleton" aria-hidden="true">
  <div class="skeleton skeleton-image"></div>
  <div class="card-content">
    <div class="skeleton skeleton-text" style="width: 70%"></div>
    <div class="skeleton skeleton-text" style="width: 90%"></div>
    <div class="skeleton skeleton-text" style="width: 50%"></div>
  </div>
</article>
```

Vary text-line widths (50–90%) — uniform bars read as stripes, not text.

## Spinners

```css
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #e5e7eb;
  border-top-color: var(--primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### Button loading state (preserves button width)

```css
.button-loading {
  position: relative;
  color: transparent;      /* hide label, keep layout */
  pointer-events: none;
}

.button-loading::after {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 20px; height: 20px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
```

## Progress bars

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 65%"
       aria-valuenow="65" aria-valuemin="0" aria-valuemax="100">
  </div>
</div>
```

```css
.progress {
  height: 8px;
  background: #e5e7eb;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: var(--primary);
  transition: width 0.3s ease-out;
}

/* Indeterminate — total unknown but ongoing */
.progress-indeterminate .progress-bar {
  width: 30%;
  animation: indeterminate 1.5s infinite ease-in-out;
}

@keyframes indeterminate {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(400%); }
}
```

Pair the bar with text context when possible: "Uploading… 2 of 3 files".

## Empty states

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  text-align: center;
}

.empty-illustration { width: 200px; max-width: 100%; margin-bottom: 24px; }
.empty-icon         { font-size: 48px; margin-bottom: 16px; }

.empty-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.empty-description {
  font-size: 14px;
  color: var(--text-secondary);
  max-width: 300px;
  margin-bottom: 24px;
}
```

### First use — sell the action

```html
<div class="empty-state">
  <img src="illustration.svg" alt="" class="empty-illustration">
  <h3 class="empty-title">No projects yet</h3>
  <p class="empty-description">Create your first project to get started</p>
  <button class="button-primary">Create Project</button>
</div>
```

### No results — offer the way out

```html
<div class="empty-state">
  <span class="empty-icon" aria-hidden="true">🔍</span>
  <h3 class="empty-title">No results found</h3>
  <p class="empty-description">Try adjusting your search or filters</p>
  <button class="button-secondary">Clear Filters</button>
</div>
```

### Load failure — always a retry

```html
<div class="empty-state error-state">
  <span class="empty-icon" aria-hidden="true">⚠️</span>
  <h3 class="empty-title">Something went wrong</h3>
  <p class="empty-description">We couldn't load your data. Please try again.</p>
  <button class="button-primary">Retry</button>
</div>
```

### Success-empty (inbox zero) — celebrate, don't apologize

Same structure; congratulatory copy ("You're all caught up"), no CTA required.

## Accessibility

```html
<!-- Region that loads content -->
<section aria-busy="true" aria-live="polite">
  <!-- skeleton now; content later -->
</section>
```

```css
/* Visually-hidden announcement for screen readers */
.loading-region[aria-busy="true"]::before {
  content: "Loading...";
  position: absolute;
  clip: rect(0, 0, 0, 0);
}

/* Respect reduced motion: stop shimmer, slow spinner */
@media (prefers-reduced-motion: reduce) {
  .skeleton-animated { animation: none; }
  .spinner { animation-duration: 1.5s; }
}
```

Mark skeletons `aria-hidden="true"` — screen readers should hear "loading",
not a parade of empty divs.
