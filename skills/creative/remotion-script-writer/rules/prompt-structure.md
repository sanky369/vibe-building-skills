---
name: prompt-structure
description: Defines the structure of the input prompt for the remotion-script-writer skill.
metadata:
  tags: prompt, input, structure, requirements
---

## Prompt Structure

To generate a high-quality video script, the `remotion-script-writer` skill requires a detailed prompt with the following sections:

### 1. Video Goal

-   **`goal`**: A clear and concise description of the video's purpose and what it should achieve.
-   **`targetAudience`**: A description of the intended audience for the video.

### 2. Codebase Information

-   **`code`**: The code to be featured in the video. This can be provided as a direct code block or a link to a GitHub repository.
-   **`language`**: The programming language of the code (e.g., `JavaScript`, `TypeScript`, `Python`).

### 3. Video Requirements

-   **`videoType`**: The type of video to be created (e.g., `product-demo`, `coding-tutorial`, `animation`).
-   **`duration`**: The desired duration of the video in seconds.
-   **`style`**: Any specific visual style or branding guidelines to follow (e.g., `modern`, `minimalist`, `playful`).

### 4. Animation and Transition Preferences

-   **`animations`**: A list of preferred animation types (e.g., `fade`, `slide`, `typewriter`).
-   **`transitions`**: A list of preferred transition types between scenes (e.g., `wipe`, `flip`, `clockWipe`).

### Example Prompt

```json
{
  "goal": "Create a product demo video for our new task management app.",
  "targetAudience": "Project managers and teams looking for a new productivity tool.",
  "code": "/path/to/your/codebase",
  "language": "TypeScript",
  "videoType": "product-demo",
  "duration": 60,
  "style": "modern",
  "animations": ["fade", "slide"],
  "transitions": ["wipe"]
}
```
