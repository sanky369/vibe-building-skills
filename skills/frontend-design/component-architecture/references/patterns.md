# Component Architecture — Pattern Gallery

Extended code examples for each atomic level and principle. The decision rules
live in `../SKILL.md`; this file is the implementation reference.

## Atomic level examples

### Atom: Button

```typescript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  fullWidth?: boolean;
  icon?: React.ReactNode;
  onClick?: () => void;
  children: React.ReactNode;
  className?: string;
  'aria-label'?: string;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  onClick,
  children,
  ...rest
}) => {
  return (
    <button
      className={`button button--${variant} button--${size}`}
      disabled={disabled || loading}
      onClick={onClick}
      {...rest}
    >
      {loading && <Spinner size="sm" />}
      {children}
    </button>
  );
};
```

### Molecule: FormInput (Label + Input + ErrorMessage)

```typescript
interface FormInputProps {
  label: string;
  placeholder?: string;
  error?: string;
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
}

export const FormInput: React.FC<FormInputProps> = ({
  label, placeholder, error, value, onChange, disabled,
}) => {
  return (
    <div className="form-input">
      <Label>{label}</Label>
      <Input
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
        aria-invalid={!!error}
      />
      {error && <ErrorMessage>{error}</ErrorMessage>}
    </div>
  );
};
```

### Organism: Card

```typescript
interface CardProps {
  title: string;
  description?: string;
  image?: string;
  action?: { label: string; onClick: () => void };
  children?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({
  title, description, image, action, children,
}) => {
  return (
    <div className="card">
      {image && <img src={image} alt={title} className="card-image" />}
      <div className="card-content">
        <h3 className="card-title">{title}</h3>
        {description && <p className="card-description">{description}</p>}
        {children}
        {action && (
          <Button onClick={action.onClick} variant="secondary">
            {action.label}
          </Button>
        )}
      </div>
    </div>
  );
};
```

### Template: BlogPostTemplate

Templates place organisms into a page-level layout; they are specific to a page
type and rarely reusable.

```typescript
export const BlogPostTemplate: React.FC<BlogPostTemplateProps> = ({
  title, author, date, image, content, relatedPosts,
}) => {
  return (
    <div className="blog-post-template">
      <Header />
      <article className="blog-post">
        <div className="blog-post-hero">
          <img src={image} alt={title} />
        </div>
        <div className="blog-post-content">
          <h1>{title}</h1>
          <div className="blog-post-meta">
            <Avatar src={author.avatar} alt={author.name} />
            <span>{author.name}</span>
            <span>{formatDate(date)}</span>
          </div>
          <div className="blog-post-body">{content}</div>
        </div>
      </article>
      <section className="related-posts">
        <h2>Related Posts</h2>
        <div className="related-posts-grid">
          {relatedPosts.map((post) => <Card key={post.id} {...post} />)}
        </div>
      </section>
      <Footer />
    </div>
  );
};
```

Pages are instances of templates with real data — use them to spot edge cases
(long names, missing images, empty lists).

## Principle examples

### Single responsibility — before/after

```typescript
// BEFORE: one component renders, fetches, validates, and submits
const UserProfile = () => {
  const [user, setUser] = useState(null);
  const [formData, setFormData] = useState({});
  const [errors, setErrors] = useState({});
  useEffect(() => { fetchUser().then(setUser); }, []);
  const handleSubmit = () => { /* validation + submission */ };
  return ( /* complex JSX */ );
};

// AFTER: an orchestrator plus focused children
const UserProfile = () => {
  const { user } = useUser();
  return (
    <>
      <UserHeader user={user} />
      <UserEditForm user={user} />
      <UserActivity user={user} />
    </>
  );
};
```

### Composition over inheritance

```typescript
// Avoid: class hierarchies for variants
class Button extends React.Component {}
class PrimaryButton extends Button {}
class LargePrimaryButton extends Button {}

// Prefer: one component, props for variation, wrappers for common presets
const Button = ({ variant = 'primary', size = 'md', ...props }) => (
  <button className={`button button--${variant} button--${size}`} {...props} />
);
const PrimaryButton = (props) => <Button variant="primary" {...props} />;
```

### Controlled vs uncontrolled

```typescript
// Controlled: parent owns state — required when other UI reacts to the value
const ControlledInput = ({ value, onChange }) => (
  <input value={value} onChange={(e) => onChange(e.target.value)} />
);

// Uncontrolled: component owns state — fine for fire-and-forget inputs
const UncontrolledInput = ({ defaultValue, onSubmit }) => {
  const inputRef = useRef(null);
  return (
    <>
      <input ref={inputRef} defaultValue={defaultValue} />
      <button onClick={() => onSubmit(inputRef.current.value)}>Submit</button>
    </>
  );
};
```

## Component documentation template

Use this structure for every documented component:

```markdown
# ComponentName

## Purpose
One sentence: what it does and when to use it.

## Props
| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `variant` | 'primary' \| 'secondary' | 'primary' | Visual variant |
| `size` | 'sm' \| 'md' \| 'lg' | 'md' | Component size |
| `disabled` | boolean | false | Disable the component |
| `children` | ReactNode | — | Content |

## Variants
One subsection per variant: when to use it + a JSX example.
(e.g. primary = main action "Save"; secondary = "Cancel"; ghost = tertiary
"Learn more"; danger = destructive "Delete")

## States
default / hover / active / focus-visible / disabled / loading — with the rule
for each (disabled = not clickable + not-allowed cursor; loading = spinner +
not clickable).

## Accessibility
Keyboard activation, focus-visible outline, aria-label requirement for
icon-only usage, screen-reader announcements.

## Edge cases
Icon-only needs aria-label; long text wraps or truncates; empty children.
```

## Size conventions (common defaults, adjust to the project's scale)

| Size | Height | Font size | Use |
| :--- | :--- | :--- | :--- |
| sm | 32px | 12–13px | Dense UI, table rows |
| md | 40px | 14px | Default |
| lg | 48px | 16px | Prominent / marketing CTAs |
