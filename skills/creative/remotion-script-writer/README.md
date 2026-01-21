# Remotion Script Writer - Agent Skill

A comprehensive agent skill for generating detailed video scripts for Remotion based on input requirements and codebase analysis.

## Overview

The **Remotion Script Writer** skill is designed to bridge the gap between conceptual video ideas and executable Remotion code. By analyzing codebases and understanding video requirements, this skill generates structured video scripts that can be directly used by Remotion's agent skills to create professional videos for product demos, coding tutorials, and various types of animations.

## Key Features

- **Codebase Analysis**: Automatically analyzes provided code to understand structure, functionality, and key features worth highlighting.
- **Structured Script Generation**: Produces detailed JSON-formatted scripts with scene breakdowns, animations, transitions, and timing.
- **Multiple Video Types**: Supports product demos, coding tutorials, data visualizations, and animated content.
- **Remotion Best Practices**: Incorporates Remotion's animation principles, sequencing patterns, and technical requirements.
- **Asset Management**: Identifies and lists all required assets (images, fonts, audio, etc.) for video production.

## When to Use

Use this skill when you need to:

1. **Create Product Demo Videos**: Showcase features of a web application or software product with professional animations and transitions.
2. **Generate Coding Tutorials**: Explain codebases or technical concepts with animated code snippets and visual explanations.
3. **Design Animated Content**: Create engaging animations with complex sequences, transitions, and effects.
4. **Automate Video Production**: Transform written requirements into executable video scripts without manual scene planning.

## Installation

To add this skill to your AI agent:

```bash
npx skills add remotion-script-writer
```

Or manually copy the skill files to your agent's skills directory.

## Usage

### Basic Usage

Provide a JSON input with your video requirements:

```json
{
  "goal": "Create a product demo video for our new task management app",
  "targetAudience": "Project managers and teams looking for productivity tools",
  "code": "/path/to/your/codebase",
  "language": "TypeScript",
  "videoType": "product-demo",
  "duration": 60,
  "style": "modern",
  "animations": ["fade", "slide", "typewriter"],
  "transitions": ["wipe", "fade"]
}
```

### Advanced Usage

For more complex videos, you can specify additional parameters:

```json
{
  "goal": "Create a coding tutorial explaining React hooks",
  "targetAudience": "Intermediate React developers",
  "code": "https://github.com/username/repo",
  "language": "JavaScript",
  "videoType": "coding-tutorial",
  "duration": 120,
  "style": "educational",
  "animations": ["typewriter", "fade", "slide"],
  "transitions": ["slide", "wipe"],
  "branding": {
    "primaryColor": "#007bff",
    "secondaryColor": "#6c757d",
    "logo": "/path/to/logo.png"
  },
  "voiceoverScript": "Auto-generate based on code analysis"
}
```

## Output Format

The skill generates a comprehensive JSON script with the following structure:

### Video Metadata

```json
{
  "videoMetadata": {
    "title": "Product Demo: Task Manager Pro",
    "durationInSeconds": 60,
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "videoType": "product-demo"
  }
}
```

### Scene Breakdown

Each scene includes:

- **Scene number and title**: For organization and reference
- **Duration**: Precise timing in seconds
- **Visuals**: Background, text elements, code snippets, images
- **Animations**: Type, duration, and easing functions
- **Audio**: Voiceover script synchronized with visuals
- **Transitions**: Smooth transitions to the next scene

Example scene:

```json
{
  "sceneNumber": 1,
  "title": "Introduction",
  "durationInSeconds": 10,
  "visuals": {
    "background": "#FFFFFF",
    "elements": [
      {
        "type": "text",
        "content": "Welcome to Task Manager Pro",
        "fontSize": 48,
        "fontFamily": "Roboto",
        "color": "#007bff",
        "position": { "x": "center", "y": "center" },
        "animation": {
          "type": "fade-in",
          "durationInSeconds": 1,
          "easing": "easeInOut"
        }
      }
    ]
  },
  "audio": {
    "voiceover": "Welcome to Task Manager Pro, the ultimate tool for managing your tasks and boosting your productivity."
  },
  "transitionToNextScene": {
    "type": "wipe",
    "direction": "from-left",
    "durationInSeconds": 1
  }
}
```

### Required Assets

```json
{
  "requiredAssets": {
    "images": [
      {
        "description": "App logo",
        "path": "/assets/logo.png"
      }
    ],
    "videos": [],
    "audio": [],
    "fonts": ["Roboto", "Montserrat"],
    "logos": ["/assets/logo.png"]
  }
}
```

### Technical Requirements

```json
{
  "technicalRequirements": {
    "remotionPackages": [
      "@remotion/transitions",
      "@remotion/google-fonts"
    ],
    "thirdPartyLibraries": []
  }
}
```

## Best Practices Incorporated

The Remotion Script Writer skill incorporates the following Remotion best practices:

### Animation Principles

- All animations use `useCurrentFrame()` hook for frame-based timing
- Animations are specified in seconds and converted to frames using fps
- CSS transitions and Tailwind animations are avoided
- Spring animations with natural motion (`damping: 200`) for smooth reveals
- Interpolation with proper easing functions for controlled animations

### Sequencing and Timing

- Proper use of `<Sequence>` for delayed element appearance
- `<Series>` for sequential playback without overlap
- `<TransitionSeries>` for scene transitions with effects
- Premounting sequences with `premountFor` prop for performance
- Accurate duration calculation accounting for transition overlaps

### Text Animations

- Typewriter effects using string slicing (not per-character opacity)
- Word highlighting animations like highlighter pen
- Caption support with TikTok-style pages
- Proper text measurement and fitting

### Media Handling

- `<Video>` components with `trimBefore`, `trimAfter`, and `volume` props
- `<Audio>` components for background music and sound effects
- `<Img>` for static images
- `<Gif>` from `@remotion/gif` for animated GIFs
- `staticFile()` for local assets in the public folder

### Composition Structure

- Proper composition definition with id, component, duration, dimensions, and fps
- Default values: 30fps, 1920x1080, meaningful composition IDs
- Type-safe default props using `satisfies` keyword
- Dynamic metadata with `calculateMetadata` when needed

## Video Types Supported

### 1. Product Demo Videos

Showcase features of web applications with:
- Feature walkthroughs with screen recordings
- UI element highlights and annotations
- Smooth transitions between features
- Professional voiceover scripts
- Call-to-action endings

### 2. Coding Tutorials

Explain code with:
- Syntax-highlighted code snippets
- Step-by-step code explanations
- Animated code changes
- Visual diagrams and flowcharts
- Progressive disclosure of concepts

### 3. Data Visualizations

Present data with:
- Animated charts and graphs
- Map animations with routes
- Statistical animations
- Real-time data updates
- Interactive elements

### 4. Social Media Content

Create engaging content with:
- Short-form vertical videos
- Captions and text overlays
- Music synchronization
- Trending effects and transitions
- Platform-specific optimizations

### 5. Animations and Effects

Design creative animations with:
- 3D content using Three.js
- Lottie animations
- Particle effects
- Background animations
- Custom shader effects

## Workflow Integration

The Remotion Script Writer skill is designed to work seamlessly with Remotion's agent skills:

1. **Script Generation**: Use this skill to generate a detailed video script
2. **Code Generation**: Pass the script to Remotion agent skills to generate React components
3. **Preview**: Use Remotion Studio to preview the video
4. **Refinement**: Iterate on the script based on preview feedback
5. **Rendering**: Render the final video using Remotion's rendering pipeline

## Example Use Cases

### Use Case 1: SaaS Product Demo

**Input:**
```json
{
  "goal": "Create a 60-second product demo for our project management SaaS",
  "targetAudience": "Small business owners and team leads",
  "code": "https://github.com/company/project-manager",
  "videoType": "product-demo",
  "duration": 60,
  "style": "professional"
}
```

**Output:** A structured script with 5-6 scenes showcasing key features like task creation, team collaboration, deadline tracking, and reporting.

### Use Case 2: React Hooks Tutorial

**Input:**
```json
{
  "goal": "Explain useState and useEffect hooks to beginners",
  "targetAudience": "Junior React developers",
  "code": "/examples/hooks-demo.jsx",
  "videoType": "coding-tutorial",
  "duration": 120,
  "style": "educational"
}
```

**Output:** A detailed tutorial script with code snippets, animations showing state changes, and clear explanations of hook behavior.

### Use Case 3: Animated Infographic

**Input:**
```json
{
  "goal": "Create an animated infographic about climate change statistics",
  "targetAudience": "General public",
  "videoType": "animation",
  "duration": 90,
  "style": "modern"
}
```

**Output:** A script with data visualizations, animated charts, and smooth transitions between statistics.

## Customization

The skill can be customized by modifying the rule files:

- **`prompt-structure.md`**: Adjust input requirements and validation
- **`script-generation.md`**: Modify the core generation prompt and output format
- **`animation-patterns.md`**: Add new animation patterns and effects
- **`scene-templates.md`**: Define reusable scene templates for common scenarios

## Technical Details

### Dependencies

- Remotion core framework
- Optional: `@remotion/transitions`, `@remotion/google-fonts`, `@remotion/gif`
- Node.js 16+ or Bun 1.0.3+

### Performance Considerations

- Scene duration optimization for smooth playback
- Asset preloading and caching strategies
- Efficient animation calculations
- Memory management for long videos

### Limitations

- Maximum recommended video duration: 5 minutes (for performance)
- Code complexity analysis works best with well-documented code
- Voiceover scripts are auto-generated and may require manual refinement
- Asset generation (images, icons) is not included - assets must be provided

## Contributing

To contribute to this skill:

1. Fork the repository
2. Create a feature branch
3. Add new rule files or modify existing ones
4. Test with various video types and codebases
5. Submit a pull request with detailed description

## License

This skill is open-source and available under the MIT License.

## Support

For issues, questions, or feature requests:

- Open an issue on GitHub
- Join the Remotion Discord community
- Consult the Remotion documentation at [remotion.dev](https://www.remotion.dev)

## Acknowledgments

This skill was created by studying:

- Remotion's official documentation and best practices
- Community examples and templates
- Real-world video production workflows
- Agent skills framework by Remotion team

Special thanks to the Remotion community for their contributions and feedback.

---

**Created by**: Manus AI  
**Version**: 1.0.0  
**Last Updated**: January 2026
