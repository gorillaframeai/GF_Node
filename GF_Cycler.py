class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

class GF_Cycler:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text": ("STRING", {"multiline": True, "default": ""}),
            "repeats": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "loops": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "strings_in_block": ("INT", {"default": 1, "min": 1, "max": 99999}),
            "string_start": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = (any_type, "STRING")
    RETURN_NAMES = ("STRING", "show_text")
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "cycle"
    CATEGORY = "GF/List"    

    def cycle(self, text, repeats, loops=1, strings_in_block=1, string_start=""):
        show_help = "https://github.com/gorillaframeai/GF_Nodes"

        if string_start:
            lines = text.split(string_start)
            lines = [line for line in lines if line.strip()]
        else:
            lines = text.splitlines()

        list_out = []

        for _ in range(loops):
            for i in range(0, len(lines), strings_in_block):
                string_block = ""
                for text_item in lines[i:i+strings_in_block]:
                    if string_start:
                        string_block += f"{string_start}{text_item}\n"
                    else:
                        string_block += f"{text_item}\n"

                string_block = string_block.strip()

                for _ in range(repeats):
                    list_out.append(string_block)
        
        return (list_out, show_help)

NODE_CLASS_MAPPINGS = {
    "GF_Cycler": GF_Cycler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GF_Cycler": "GF Cycler"
}
