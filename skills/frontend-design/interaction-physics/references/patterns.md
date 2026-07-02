# Interaction Physics — Implementation Gallery

Canonical CSS for the standard microinteractions. Timing/easing decision rules
live in `../SKILL.md`; copy and adapt these implementations to the project's
tokens and naming.

## Button states (complete set)

```css
button {
  background-color: var(--color-primary);
  color: white;
  transition: background-color 200ms ease-out;
}

button:hover:not(:disabled) {
  background-color: var(--color-primary-dark);
}

button:active:not(:disabled) {
  background-color: var(--color-primary-darker);
  transform: scale(0.98);
}

button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

button:disabled {
  background-color: var(--color-disabled);
  cursor: not-allowed;
  opacity: 0.6;
}

button.loading {
  pointer-events: none;
  opacity: 0.8;
}

button.loading::after {
  content: '';
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-left: 8px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

## Form validation feedback

```css
input {
  border: 1px solid var(--color-border);
  transition: border-color 200ms ease-out, box-shadow 200ms ease-out;
}

input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

input.valid { border-color: var(--color-success); }
input.error { border-color: var(--color-error); }

input.error:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

.error-message {
  animation: slideDown 300ms ease-out;
  color: var(--color-error);
  font-size: 14px;
  margin-top: 4px;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

## Loading indicators

```css
/* Skeleton shimmer */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-skeleton) 0%,
    var(--color-skeleton-light) 50%,
    var(--color-skeleton) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Spinner */
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid var(--color-border);
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Progress bar fill */
.progress-bar-fill {
  height: 100%;
  background-color: var(--color-primary);
  transition: width 300ms ease-out;
}
```

## Notifications (toast) enter/exit

```css
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 16px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  animation: toastIn 300ms ease-out;
  z-index: 1000;
}

.notification.success { border-left: 4px solid var(--color-success); }
.notification.error   { border-left: 4px solid var(--color-error); }
.notification.warning { border-left: 4px solid var(--color-warning); }

.notification.exiting {
  animation: toastOut 300ms ease-in forwards;
}

@keyframes toastIn {
  from { opacity: 0; transform: translateX(400px); }
  to   { opacity: 1; transform: translateX(0); }
}

@keyframes toastOut {
  from { opacity: 1; transform: translateX(0); }
  to   { opacity: 0; transform: translateX(400px); }
}
```

## Page / view transitions

```css
/* Fade */
.page          { animation: fadeIn 400ms ease-out; }
.page.exiting  { animation: fadeOut 300ms ease-in forwards; }

@keyframes fadeIn  { from { opacity: 0; } to { opacity: 1; } }
@keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }

/* Slide (directional — implies navigation hierarchy) */
.page-slide         { animation: pageIn 400ms ease-out; }
.page-slide.exiting { animation: pageOut 300ms ease-in forwards; }

@keyframes pageIn {
  from { opacity: 0; transform: translateX(30px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes pageOut {
  from { opacity: 1; transform: translateX(0); }
  to   { opacity: 0; transform: translateX(-30px); }
}
```

## Modal open/close

```css
.modal {
  animation: modalIn 400ms ease-out;
}
.modal.closing {
  animation: modalOut 300ms ease-in forwards;
}

@keyframes modalIn {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes modalOut {
  from { opacity: 1; transform: translateY(0); }
  to   { opacity: 0; transform: translateY(20px); }
}
```

## Playful accent (use sparingly)

```css
.bounce {
  animation: bounce 600ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Attention pulse (accessible alternative to flashing)

```css
/* Never flash rapidly — this slow pulse draws attention safely */
.alert {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%      { opacity: 0.7; }
}
```

## Reduced motion baseline

Apply globally in every project this skill touches:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Keep purely informational motion (e.g. a progress bar's width updates) but
remove decorative movement. Opacity-only crossfades are an acceptable
reduced-motion substitute for slides/scales.
