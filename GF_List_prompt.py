import random

class GF_List_prompt_Separator:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text": ("STRING", {"multiline": True, "default": ""}),
            "separators": ("STRING", {"default": ","}),
            "line_separator": ("STRING", {"default": ","}),  # Вернули на запятую
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "GF/prompt"

    def process(self, text, separators, line_separator, seed=0):
        lines = [line.strip() for line in text.splitlines() if line.strip()][:50]
        sep_list = separators.split(',')[:50]
        
        outputs = []
        for i, line in enumerate(lines):
            elements = [elem.strip() for elem in line.split(line_separator) if elem.strip()]
            if elements:
                if i < len(sep_list):
                    outputs.append(sep_list[i])
                index = seed % len(elements)
                selected = elements[index]
                outputs.append(selected)
        
        # Добавляем оставшиеся сепараторы в конец
        if len(lines) < len(sep_list):
            outputs.extend(sep_list[len(lines):])
        
        result = ''.join(outputs)
        return (result,)

# Обновляем отображения для ComfyUI
NODE_CLASS_MAPPINGS = {
    "GF_List_prompt_Separator": GF_List_prompt_Separator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GF_List_prompt_Separator": "GF List Prompt Separator"
}
