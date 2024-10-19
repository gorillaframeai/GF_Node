import random

class GF_Node_Dynamic_Lines2:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "input_text": ("STRING", {"multiline": True, "default": cls.EXAMPLE()}),
            "line_separator": ("STRING", {"default": ","}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "GF"

    @staticmethod
    def EXAMPLE():
        return """boy with a dog
# this line is ignored
apple,banana,orange
red,blue,green
# another ignored line
girl with a cat
car,bicycle,scooter"""

    def process(self, input_text, line_separator, seed):
        outputs = []
        for index, line in enumerate(input_text.split('\n')):
            line = line.strip()
            if line and not line.startswith('#'):
                self.process_line(line, line_separator, outputs, seed + index)

        return (" ".join(outputs).strip(),)

    def process_line(self, line, line_separator, outputs, unique_seed):
        elements = [elem.strip() for elem in line.split(line_separator) if elem.strip()]
        if elements:
            random.seed(unique_seed)  # Устанавливаем уникальный seed для каждой строки
            selected = random.choice(elements)
            outputs.append(selected + " ")

# Обновляем отображения для ComfyUI
NODE_CLASS_MAPPINGS = {
    "GF_Node_Dynamic_Lines2": GF_Node_Dynamic_Lines2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GF_Node_Dynamic_Lines2": "🐵 GF node (Dynamic Lines2)"
}