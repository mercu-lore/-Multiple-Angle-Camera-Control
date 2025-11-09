"""
Camera Control Prompt Node for ComfyUI
Optimized for dx8152's MultiAngle LoRA

Author: Lorenzo Mercu
Description: Advanced camera control prompt generator
Features: Multi-directional camera movements, rotations, and special views
Optimized for: dx8152's MultiAngle LoRA
"""


class CameraControlPromptNode:
    """
    Advanced camera control prompt generator for ComfyUI.
    Converts camera parameters into bilingual prompts (Chinese + English).
    Optimized for dx8152's MultiAngle LoRA workflow.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # MOVIMENTO ORIZZONTALE (left/right) - Dropdown
                "move_horizontal": ("COMBO", {
                    "default": "none",
                    "options": ["none", "left", "right"]
                }),

                # MOVIMENTO VERTICALE (up/down) - Dropdown
                "move_vertical": ("COMBO", {
                    "default": "none",
                    "options": ["none", "up", "down"]
                }),

                # MOVIMENTO FORWARD - Dropdown
                "move_forward": ("COMBO", {
                    "default": "no",
                    "options": ["no", "yes"]
                }),

                # ROTATE SLIDER (-90 a 90, step 45)
                "rotate": ("INT", {
                    "default": 0,
                    "min": -90,
                    "max": 90,
                    "step": 45,
                    "display": "slider"
                }),

                # VISTE SPECIALI - Bottoni On/Off
                "view_top_down": ("BOOLEAN", {
                    "default": False
                }),
                "view_wide_angle": ("BOOLEAN", {
                    "default": False
                }),
                "view_close_up": ("BOOLEAN", {
                    "default": False
                }),
                "view_bottom_up": ("BOOLEAN", {
                    "default": False
                }),

            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "prompt/camera"

    def generate_prompt(self, move_horizontal, move_vertical, move_forward, rotate, view_top_down, view_wide_angle, view_close_up, view_bottom_up):
        """Genera il prompt basato sui parametri camera"""

        prompt_parts = []

        # MOVIMENTO ORIZZONTALE (Dropdown: none, left, right)
        if move_horizontal == "left":
            prompt_parts.append("将镜头向左移动 Move the camera left.")
        elif move_horizontal == "right":
            prompt_parts.append("将镜头向右移动 Move the camera right.")

        # MOVIMENTO VERTICALE (Dropdown: none, up, down)
        if move_vertical == "up":
            prompt_parts.append("将镜头向上移动 Move the camera up.")
        elif move_vertical == "down":
            prompt_parts.append("将镜头向下移动 Move the camera down.")

        # MOVIMENTO FORWARD (Dropdown: no, yes)
        if move_forward == "yes":
            prompt_parts.append("将镜头向前移动 Move the camera forward.")

        # ROTATE SLIDER (dynamic label based on value)
        if rotate < 0:
            degrees = abs(rotate)
            prompt_parts.append(f"将镜头向左旋转{degrees}度 Rotate the camera {degrees} degrees to the left.")
        elif rotate > 0:
            degrees = rotate
            prompt_parts.append(f"将镜头向右旋转{degrees}度 Rotate the camera {degrees} degrees to the right.")
        # Se rotate == 0, non aggiunge niente

        # VISTE SPECIALI (Bottoni On/Off)
        if view_top_down:
            prompt_parts.append("将镜头转为俯视 Turn the camera to a top-down view.")

        if view_wide_angle:
            prompt_parts.append("将镜头转为广角镜头 Turn the camera to a wide-angle lens.")

        if view_close_up:
            prompt_parts.append("将镜头转为特写镜头 Turn the camera to a close-up.")

        if view_bottom_up:
            prompt_parts.append("將相機方向調整為由下而上的視角 Turn the camera to a bottom-up view.")

        # Concatena tutte le parti con spazio
        final_prompt = " ".join(prompt_parts)

        return (final_prompt,)


# Mappings per ComfyUI
NODE_CLASS_MAPPINGS = {
    "CameraControlPromptNode": CameraControlPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CameraControlPromptNode": "Camera Control Prompt Generator"
}
