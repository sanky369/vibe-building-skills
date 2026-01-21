---
name: scene-templates
description: Reusable scene templates for common video scenarios.
metadata:
  tags: scenes, templates, structure, video
---

## Scene Templates

Use these templates as starting points for common video scenes:

### 1. Title Scene

A simple title card to introduce the video.

```json
{
  "sceneNumber": 1,
  "title": "Title Card",
  "durationInSeconds": 5,
  "visuals": {
    "background": "#007bff",
    "elements": [
      {
        "type": "text",
        "content": "Video Title",
        "fontSize": 64,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#FFFFFF",
        "position": { "x": "center", "y": "center" },
        "animation": {
          "type": "scale-in",
          "springConfig": { "damping": 200 }
        }
      },
      {
        "type": "text",
        "content": "Subtitle or tagline",
        "fontSize": 24,
        "fontFamily": "Roboto",
        "color": "#FFFFFF",
        "opacity": 0.8,
        "position": { "x": "center", "y": "60%" },
        "animation": {
          "type": "fade-in",
          "delay": 0.5,
          "durationInSeconds": 1
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Welcome to [Video Title]"
  },
  "transitionToNextScene": {
    "type": "fade",
    "durationInSeconds": 1
  }
}
```

### 2. Feature Showcase

Highlight a specific feature with text and visuals.

```json
{
  "sceneNumber": 2,
  "title": "Feature Showcase",
  "durationInSeconds": 10,
  "visuals": {
    "background": "#FFFFFF",
    "elements": [
      {
        "type": "text",
        "content": "Feature Name",
        "fontSize": 48,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#333333",
        "position": { "x": "10%", "y": "20%" },
        "animation": {
          "type": "slide-in",
          "direction": "from-left",
          "durationInSeconds": 0.8
        }
      },
      {
        "type": "text",
        "content": "Description of the feature and its benefits.",
        "fontSize": 24,
        "fontFamily": "Roboto",
        "color": "#666666",
        "position": { "x": "10%", "y": "35%" },
        "maxWidth": "40%",
        "animation": {
          "type": "fade-in",
          "delay": 0.5,
          "durationInSeconds": 1
        }
      },
      {
        "type": "image",
        "src": "/assets/feature-screenshot.png",
        "position": { "x": "60%", "y": "50%" },
        "width": "35%",
        "animation": {
          "type": "scale-in",
          "delay": 0.8,
          "springConfig": { "damping": 200 }
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Our [Feature Name] allows you to [benefit]. This makes [task] easier and more efficient."
  },
  "transitionToNextScene": {
    "type": "wipe",
    "direction": "from-left",
    "durationInSeconds": 1
  }
}
```

### 3. Code Explanation

Show and explain a code snippet.

```json
{
  "sceneNumber": 3,
  "title": "Code Explanation",
  "durationInSeconds": 15,
  "visuals": {
    "background": "#1e1e1e",
    "elements": [
      {
        "type": "text",
        "content": "How it works",
        "fontSize": 36,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#FFFFFF",
        "position": { "x": "5%", "y": "5%" },
        "animation": {
          "type": "fade-in",
          "durationInSeconds": 0.5
        }
      },
      {
        "type": "code",
        "language": "javascript",
        "content": "const example = () => {\n  return 'Hello World';\n};",
        "fontSize": 20,
        "theme": "github-dark",
        "position": { "x": "5%", "y": "20%" },
        "width": "90%",
        "animation": {
          "type": "code-reveal",
          "linesPerSecond": 2,
          "delay": 0.5
        }
      },
      {
        "type": "text",
        "content": "This function returns a greeting message.",
        "fontSize": 20,
        "fontFamily": "Roboto",
        "color": "#CCCCCC",
        "position": { "x": "5%", "y": "70%" },
        "maxWidth": "90%",
        "animation": {
          "type": "fade-in",
          "delay": 3,
          "durationInSeconds": 1
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Let's look at how this works in code. This function demonstrates [concept]. As you can see, it [explanation]."
  },
  "transitionToNextScene": {
    "type": "fade",
    "durationInSeconds": 1
  }
}
```

### 4. Comparison Scene

Compare two options or approaches side-by-side.

```json
{
  "sceneNumber": 4,
  "title": "Comparison",
  "durationInSeconds": 12,
  "visuals": {
    "background": "#F5F5F5",
    "elements": [
      {
        "type": "text",
        "content": "Before vs After",
        "fontSize": 48,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#333333",
        "position": { "x": "center", "y": "10%" },
        "animation": {
          "type": "fade-in",
          "durationInSeconds": 0.5
        }
      },
      {
        "type": "container",
        "position": { "x": "10%", "y": "30%" },
        "width": "35%",
        "elements": [
          {
            "type": "text",
            "content": "Before",
            "fontSize": 32,
            "fontWeight": "bold",
            "color": "#E74C3C"
          },
          {
            "type": "text",
            "content": "Old approach description",
            "fontSize": 18,
            "color": "#666666"
          }
        ],
        "animation": {
          "type": "slide-in",
          "direction": "from-left",
          "delay": 0.5,
          "durationInSeconds": 0.8
        }
      },
      {
        "type": "container",
        "position": { "x": "55%", "y": "30%" },
        "width": "35%",
        "elements": [
          {
            "type": "text",
            "content": "After",
            "fontSize": 32,
            "fontWeight": "bold",
            "color": "#27AE60"
          },
          {
            "type": "text",
            "content": "New approach description",
            "fontSize": 18,
            "color": "#666666"
          }
        ],
        "animation": {
          "type": "slide-in",
          "direction": "from-right",
          "delay": 1,
          "durationInSeconds": 0.8
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Let's compare the old approach with our new solution. Before, [problem]. Now, with [solution], [benefit]."
  },
  "transitionToNextScene": {
    "type": "slide",
    "direction": "from-bottom",
    "durationInSeconds": 1
  }
}
```

### 5. Statistics/Data Scene

Display data or statistics with visual emphasis.

```json
{
  "sceneNumber": 5,
  "title": "Statistics",
  "durationInSeconds": 10,
  "visuals": {
    "background": "#FFFFFF",
    "elements": [
      {
        "type": "text",
        "content": "By the numbers",
        "fontSize": 48,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#333333",
        "position": { "x": "center", "y": "15%" },
        "animation": {
          "type": "fade-in",
          "durationInSeconds": 0.5
        }
      },
      {
        "type": "statistic",
        "value": "10,000+",
        "label": "Active Users",
        "fontSize": 64,
        "labelFontSize": 24,
        "color": "#007bff",
        "position": { "x": "25%", "y": "45%" },
        "animation": {
          "type": "counter",
          "from": 0,
          "to": 10000,
          "delay": 0.5,
          "durationInSeconds": 2
        }
      },
      {
        "type": "statistic",
        "value": "99.9%",
        "label": "Uptime",
        "fontSize": 64,
        "labelFontSize": 24,
        "color": "#27AE60",
        "position": { "x": "75%", "y": "45%" },
        "animation": {
          "type": "counter",
          "from": 0,
          "to": 99.9,
          "delay": 1,
          "durationInSeconds": 2
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Our platform is trusted by over 10,000 active users and maintains a 99.9% uptime."
  },
  "transitionToNextScene": {
    "type": "fade",
    "durationInSeconds": 1
  }
}
```

### 6. Call-to-Action Scene

End the video with a clear call to action.

```json
{
  "sceneNumber": 6,
  "title": "Call to Action",
  "durationInSeconds": 8,
  "visuals": {
    "background": "#007bff",
    "elements": [
      {
        "type": "text",
        "content": "Ready to get started?",
        "fontSize": 48,
        "fontFamily": "Roboto",
        "fontWeight": "bold",
        "color": "#FFFFFF",
        "position": { "x": "center", "y": "35%" },
        "animation": {
          "type": "scale-in",
          "springConfig": { "damping": 200 }
        }
      },
      {
        "type": "button",
        "text": "Sign Up Free",
        "fontSize": 28,
        "backgroundColor": "#FFFFFF",
        "textColor": "#007bff",
        "position": { "x": "center", "y": "55%" },
        "padding": "15px 40px",
        "borderRadius": "8px",
        "animation": {
          "type": "bounce-in",
          "delay": 0.8,
          "springConfig": { "damping": 8 }
        }
      },
      {
        "type": "text",
        "content": "www.yourwebsite.com",
        "fontSize": 20,
        "fontFamily": "Roboto",
        "color": "#FFFFFF",
        "opacity": 0.9,
        "position": { "x": "center", "y": "75%" },
        "animation": {
          "type": "fade-in",
          "delay": 1.2,
          "durationInSeconds": 1
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Ready to get started? Sign up for free today at [website]. Transform your workflow and boost your productivity."
  },
  "transitionToNextScene": null
}
```

## Scene Composition Guidelines

When composing scenes:

1. **Start with context**: Introduce what the viewer will see
2. **Build progressively**: Add elements one at a time, not all at once
3. **Use visual hierarchy**: Most important elements should be largest and most prominent
4. **Maintain consistency**: Use the same fonts, colors, and animation styles throughout
5. **Time voiceover carefully**: Ensure voiceover matches visual elements
6. **End with clarity**: Make sure the scene's message is clear before transitioning

## Scene Duration Guidelines

- **Title scenes**: 3-5 seconds
- **Feature showcases**: 8-12 seconds
- **Code explanations**: 12-20 seconds (depending on complexity)
- **Comparisons**: 10-15 seconds
- **Statistics**: 8-12 seconds
- **Call-to-action**: 6-10 seconds

## Transition Selection

Choose transitions based on scene relationship:

- **Fade**: Neutral, works for any scene transition
- **Wipe**: Good for moving between related topics
- **Slide**: Emphasizes progression or sequence
- **Flip**: Dramatic change or reveal
- **Clock Wipe**: Time-based or circular concepts
