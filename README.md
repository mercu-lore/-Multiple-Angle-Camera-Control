# Camera Control Prompt Node

Advanced camera control prompt generator for ComfyUI, optimized for **dx8152's MultiAngle LoRA**.

## Author
**Lorenzo Mercugliano**

## Description
A powerful ComfyUI custom node that converts camera control parameters into bilingual prompts (Chinese + English). Designed to work seamlessly with dx8152's MultiAngle LoRA for precise camera control in image generation workflows.

## Features
- **Multi-directional camera movements** (horizontal, vertical, forward)
- **Camera rotation** with precise angle control (-90° to 90°)
- **Special view modes** (top-down, wide-angle, close-up)
- **Bilingual output** (Chinese + English prompts)
- **Optimized interface** with sliders and toggle controls
- **No redundancy** - smart parameter organization

## Installation
1. Clone or download this folder to: `ComfyUI/custom_nodes/`
2. The folder structure should be: `ComfyUI/custom_nodes/camera_control_prompt/`
3. Restart ComfyUI

## Node Inputs

### Sliders (0-1 or Range Values)
- **move_horizontal** (-1 to 1): Left/Right camera movement
  - -1 = Move left
  - 0 = No movement
  - 1 = Move right

- **move_vertical** (-1 to 1): Up/Down camera movement
  - -1 = Move down
  - 0 = No movement
  - 1 = Move up

- **move_forward** (0 to 1): Forward camera movement (toggle)
  - 0 = No movement
  - 1 = Move forward

- **rotate** (-90 to 90, step 45): Camera rotation
  - -90 = Rotate 90° left
  - -45 = Rotate 45° left
  - 0 = No rotation
  - 45 = Rotate 45° right
  - 90 = Rotate 90° right

### Buttons (Boolean)
- **view_top_down**: Enable top-down view
- **view_wide_angle**: Enable wide-angle lens
- **view_close_up**: Enable close-up view

## Output
Single STRING output containing the complete bilingual camera control prompt, ready to use with dx8152's MultiAngle LoRA.

## Example Usage
**Inputs:**
- move_horizontal: 1 (right)
- move_vertical: 0
- move_forward: 1
- rotate: 45 (right rotation)
- view_top_down: False
- view_wide_angle: True
- view_close_up: False

**Output:**
```
将镜头向右移动 Move the camera right. 将镜头向前移动 Move the camera forward. 将镜头向右旋转45度 Rotate the camera 45 degrees to the right. 将镜头转为广角镜头 Turn the camera to a wide-angle lens.
```

## Compatibility
- **ComfyUI**: Latest versions
- **LoRA**: Optimized for dx8152's MultiAngle LoRA
- **Language**: Python 3.8+

## License
MIT

## Credits
- **Node Author**: Lorenzo Mercu
- **Optimized for**: dx8152's MultiAngle LoRA
