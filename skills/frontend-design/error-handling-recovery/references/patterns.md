# Error Handling & Recovery — Pattern Gallery

Implementations and copy examples per error class. The decision rules live in
`../SKILL.md`.

## Message rewrites (bad → good)

| Bad | Good |
|---|---|
| "Invalid input" | "Please enter a valid email address (e.g., user@example.com)" |
| "Error 404" | "We couldn't find that page. Try searching instead." |
| "Something went wrong" | "Your connection was lost. We saved your work. Reconnect when ready." |
| "CORS policy violation detected" | "We couldn't connect to the server. Check your internet and try again." |
| "Password too weak" | "Password too weak" + live checklist of which rule is unmet |

Full anatomy example:

```
Email already in use

This email is already associated with an account.

Try:
- Sign in with this email instead
- Use a different email address
- Reset your password if you forgot it

Need help? Contact support@example.com
```

## Validation errors

Validate on blur (or on submit), never on every keystroke of an incomplete
entry; re-validate on change only *after* a field has erred, so fixes clear
immediately.

```javascript
// Good — validate when the user leaves the field
const handleBlur = (e) => {
  if (!isValidEmail(e.target.value)) {
    showError('Please enter a valid email');
  }
};
```

Constructive guidance beats restating the rule:

```html
<div class="error">
  <strong>Password too weak</strong>
  <ul>
    <li>✓ At least 8 characters</li>
    <li>✗ At least one uppercase letter</li>
    <li>✓ At least one number</li>
  </ul>
</div>
```

Error placed with the field, wired for assistive tech:

```html
<div class="form-group">
  <label for="email">Email</label>
  <input id="email" type="email" aria-invalid="true" aria-describedby="email-error" />
  <div id="email-error" class="error-message" role="alert">
    Please enter a valid email
  </div>
</div>
```

## Network errors

Offer retry; preserve work; allow offline continuation where the app supports it.

```html
<div class="error-state">
  <span class="error-icon" aria-hidden="true">📡</span>
  <h3>Connection Lost</h3>
  <p>We couldn't reach the server. Your changes are saved locally.</p>
  <button class="button-primary">Retry</button>
  <button class="button-secondary">Continue Offline</button>
</div>
```

Retry rule of thumb: automatic retry with backoff for idempotent reads;
explicit user-triggered retry for mutations (never silently resubmit a payment
or post).

## Permission errors

Explain why, offer the path to access:

```html
<div class="error-state">
  <span class="error-icon" aria-hidden="true">🔒</span>
  <h3>Permission Denied</h3>
  <p>You don't have permission to edit this document.</p>
  <p>Ask the owner to give you edit access.</p>
  <button class="button-secondary">Request Access</button>
</div>
```

## System errors

Apologize, give a support reference ID, offer retry + support:

```html
<div class="error-state">
  <span class="error-icon" aria-hidden="true">⚠️</span>
  <h3>Something Went Wrong</h3>
  <p>We're having trouble processing your request. Our team has been notified.</p>
  <p>Error ID: #12345 (share this if contacting support)</p>
  <button class="button-primary">Try Again</button>
  <button class="button-secondary">Contact Support</button>
</div>
```

## 404 pages

Acknowledge, then route onward — search plus key destinations:

```html
<div class="error-state">
  <h1>404 — Page Not Found</h1>
  <p>The page you're looking for doesn't exist or has been moved.</p>
  <form class="search-form">
    <input type="search" placeholder="Search for what you need..." />
    <button type="submit">Search</button>
  </form>
  <nav class="error-nav">
    <a href="/">Home</a>
    <a href="/help">Help Center</a>
    <a href="/contact">Contact Us</a>
  </nav>
</div>
```

## Recovery workflow patterns

### Inline recovery (simple, field-level)

```html
<div class="error">
  This email is already registered.
  <button class="link-button">Sign in instead</button>
</div>
```

### Modal recovery (blocking, critical — e.g. payment failure)

```html
<div class="modal error-modal" role="alertdialog" aria-modal="true">
  <div class="modal-content">
    <h2>Payment Failed</h2>
    <p>Your card was declined. Please try another payment method.</p>
    <button class="button-primary">Try Again</button>
    <button class="button-secondary">Use Different Method</button>
  </div>
</div>
```

### Progressive recovery (multi-step diagnosis)

Guide through ordered steps — check connection → clear cache → contact
support — revealing the next step only if the previous fails.

## Graceful degradation

```html
<!-- Image fallback -->
<img src="image.jpg" alt="Product photo" onerror="this.src='placeholder.jpg'" />

<!-- Feature unavailable: disable + explain, don't hide or break -->
<button disabled title="Feature unavailable in offline mode">Share</button>
<p class="help-text">You're offline. Sharing will be available when you reconnect.</p>
```

In React, wrap independent sections in error boundaries so one crashed widget
doesn't blank the page; the boundary's fallback is an error-empty state with
retry.

## Error styling

```css
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 48px 24px;
  text-align: center;
  background: var(--error-bg);
  border-radius: 8px;
  border-left: 4px solid var(--error-color);
}

.error-input {
  border: 2px solid var(--error-color);
  background-color: var(--error-bg);
}

.error-input:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

.error-message {
  display: flex;
  align-items: center;
  margin-top: 8px;
  font-size: 14px;
  color: var(--error-color);
  animation: slideDown 300ms ease-out;
}

/* Icon + color + text — never color alone */
.error-message::before {
  content: '⚠';
  margin-right: 8px;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

## Accessibility wiring

```html
<!-- Announce dynamic errors -->
<div role="alert">Please enter a valid email address</div>

<!-- Associate error with field -->
<input type="email" aria-invalid="true" aria-describedby="email-error" />
<div id="email-error">Please enter a valid email</div>
```

- `role="alert"` (assertive) for errors blocking the user's current task;
  `aria-live="polite"` for background failures.
- On submit-level validation failure, move focus to the first invalid field
  (or to an error summary that links to each field).
- Icon + text + color for every error indicator — color is never the only
  signal.
