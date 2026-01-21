---
name: animation-patterns
description: Common animation patterns for Remotion video scripts.
metadata:
  tags: animations, patterns, effects, remotion
---

## Animation Patterns

When generating video scripts, use these proven animation patterns based on Remotion best practices:

### Text Animations

#### Fade In
```json
{
  "type": "fade-in",
  "durationInSeconds": 1,
  "easing": "easeInOut"
}
```

#### Slide In
```json
{
  "type": "slide-in",
  "direction": "from-left",
  "durationInSeconds": 0.8,
  "easing": "easeOut"
}
```

#### Typewriter Effect
```json
{
  "type": "typewriter",
  "charactersPerSecond": 10,
  "pauseAfterComplete": 0.5
}
```

#### Scale In (Spring)
```json
{
  "type": "scale-in",
  "springConfig": {
    "damping": 200
  }
}
```

### Code Animations

#### Code Reveal
```json
{
  "type": "code-reveal",
  "linesPerSecond": 2,
  "highlightSyntax": true,
  "theme": "github-dark"
}
```

#### Code Highlight
```json
{
  "type": "code-highlight",
  "lines": [5, 6, 7],
  "durationInSeconds": 1,
  "highlightColor": "#ffeb3b"
}
```

#### Code Transform
```json
{
  "type": "code-transform",
  "fromCode": "const x = 1;",
  "toCode": "const x = 2;",
  "durationInSeconds": 1.5
}
```

### Element Animations

#### Bounce In
```json
{
  "type": "bounce-in",
  "springConfig": {
    "damping": 8
  }
}
```

#### Rotate In
```json
{
  "type": "rotate-in",
  "degrees": 360,
  "durationInSeconds": 1,
  "easing": "easeInOut"
}
```

#### Blur In
```json
{
  "type": "blur-in",
  "fromBlur": 10,
  "toBlur": 0,
  "durationInSeconds": 0.8
}
```

### Exit Animations

#### Fade Out
```json
{
  "type": "fade-out",
  "durationInSeconds": 0.5,
  "easing": "easeIn"
}
```

#### Slide Out
```json
{
  "type": "slide-out",
  "direction": "to-right",
  "durationInSeconds": 0.8
}
```

#### Scale Out
```json
{
  "type": "scale-out",
  "durationInSeconds": 0.6,
  "easing": "easeIn"
}
```

## Animation Timing Guidelines

- **Quick actions** (UI interactions): 0.2-0.4 seconds
- **Standard animations** (text, elements): 0.5-1 second
- **Emphasis animations** (important content): 1-2 seconds
- **Transitions between scenes**: 0.5-1.5 seconds
- **Typewriter effects**: 8-12 characters per second

## Spring Animation Configurations

Use these spring configs for different animation feels:

```json
{
  "smooth": { "damping": 200 },
  "snappy": { "damping": 20, "stiffness": 200 },
  "bouncy": { "damping": 8 },
  "heavy": { "damping": 15, "stiffness": 80, "mass": 2 }
}
```

## Easing Functions

Common easing functions for interpolate:

- **`easeInOut`**: Smooth start and end (default for most animations)
- **`easeIn`**: Slow start, fast end (exit animations)
- **`easeOut`**: Fast start, slow end (entrance animations)
- **`linear`**: Constant speed (progress bars, counters)

## Animation Sequencing

When multiple elements animate in a scene:

1. **Stagger animations** by 0.1-0.2 seconds for visual interest
2. **Group related elements** to animate together
3. **Use spring animations** for organic, natural motion
4. **Avoid animating too many elements** at once (max 3-4)

Example staggered animation:

```json
{
  "elements": [
    {
      "type": "text",
      "content": "Feature 1",
      "animation": { "type": "fade-in", "delay": 0 }
    },
    {
      "type": "text",
      "content": "Feature 2",
      "animation": { "type": "fade-in", "delay": 0.2 }
    },
    {
      "type": "text",
      "content": "Feature 3",
      "animation": { "type": "fade-in", "delay": 0.4 }
    }
  ]
}
```
