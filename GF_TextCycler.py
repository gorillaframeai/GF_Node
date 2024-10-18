import random

class GF_TextCycler:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text": ("STRING", {"multiline": True, "default": ""}),
            "repeats": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "loops": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "string_block_number": ("INT", {"default": 0, "min": 0, "max": 100}),
            "cycle_index": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "random_order": ("BOOLEAN", {"default": False}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("STRING", "show_text")
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "gfcycle"
    CATEGORY = "GF/utils"

    def gfcycle(self, text, repeats, loops=1, string_block_number=0, cycle_index=1, random_order=False, seed=0):
        lines = [line.strip() for line in text.splitlines() if line.strip()][:100]
        
        if random_order:
            random.Random(seed).shuffle(lines)

        total_blocks = len(lines) if string_block_number == 0 else min(string_block_number, len(lines))
        
        list_out = []
        start_index = (cycle_index - 1) * total_blocks
        for loop in range(loops):
            for i in range(total_blocks):
                current_index = (start_index + i) % len(lines)
                list_out.extend([lines[current_index]] * repeats)
            start_index = (start_index + total_blocks) % len(lines)

        return (list_out, "GF Text Cycler. Обрабатывает текст построчно.")

# Добавляем необходимые отображения для ComfyUI
NODE_CLASS_MAPPINGS = {
    "GF_TextCycler": GF_TextCycler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GF_TextCycler": "GF Text Cycler"
}
# Тестовая функция (не влияет на работу в ComfyUI)
def test_GF_TextCycler():
    cycler = GF_TextCycler()
    text = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
    result, help_text = cycler.gfcycle(text, repeats=2, loops=1, string_block_number=3, random_order=True, seed=42)
    print("Результат:")
    for item in result:
        print(item)
    print("\nСправка:", help_text)

if __name__ == "__main__":
    GF_TextCycler()
