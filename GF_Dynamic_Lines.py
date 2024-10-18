import re
import random

class GF_Node:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "input_text": ("STRING", {"multiline": True, "default": s.EXAMPLE()}),
            "separators": ("STRING", {"default": ","}),
            "line_separator": ("STRING", {"default": ","}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            "show_help": ("BOOLEAN", {"default": False}),
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "GF"

    @staticmethod
    def EXAMPLE():
        return """boy with a dog
apple,banana,orange
R:2
red,blue,green
R:0
girl with a cat
car,bicycle,scooter"""

    @staticmethod
    def HELP():
        return """This node allows you to dynamically create and process text lines with randomization options.

Example usage:
boy with a dog
apple,banana,orange
R:2
red,blue,green
R:0
girl with a cat
car,bicycle,scooter

1. By default, a random choice (R:0) is applied to all lines.
2. Any line without separators is always added to the result in full.
3. Lines with separators are processed according to the randomization settings.
4. To change the randomization setting for the next line, specify:
   - R:0 - selects a random word (default setting)
   - R:1 - selects the first word
   - R:N - selects the N-th word (if N is greater than the number of words, selects the last one)
5. The randomization setting applies only to the next line, then returns to R:0.
6. The line separator (default ",") is used to separate words in a line.
7. Separators (default ",") are used between selected words from different lines.

For more information, visit the repository: https://github.com/gorillaframeai/GF_Node

Эта нода позволяет динамически создавать и обрабатывать строки текста с опциями рандомизации.

Пример использования:
мальчик с собакой
яблоко,банан,апельсин
R:2
красный,синий,зеленый
R:0
девочка с кошкой
машина,велосипед,самокат

1. По умолчанию ко всем строкам применяется случайный выбор (R:0).
2. Любая строка без разделителей всегда добавляется в результат целиком.
3. Строки с разделителями обрабатываются согласно настройкам рандомизации.
4. Чтобы изменить настройку рандомизации для следующей строки, укажите:
   - R:0 - выбирает случайное слово (настройка по умолчанию)
   - R:1 - выбирает первое слово
   - R:N - выбирает N-ное слово (если N больше количества слов, выбирает последнее)
5. Настройка рандомизации действует только на следующую строку, потом возвращается к R:0.
6. Разделитель строк (по умолчанию ",") используется для разделения слов в строке.
7. Сепараторы (по умолчанию ",") используются между выбранными словами из разных строк.

Для получения дополнительной информации посетите репозиторий: https://github.com/gorillaframeai/GF_Node"""

    def process(self, input_text, separators, line_separator, seed, show_help):
        if show_help:
            return (self.HELP(),)

        lines = input_text.split('\n')
        outputs = []
        random_pattern = re.compile(r'R:(\d+)')
        random.seed(seed)

        random_setting = 0  # По умолчанию R:0

        for line in lines:
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue

            random_match = random_pattern.match(line)

            if random_match:
                random_setting = int(random_match.group(1))
            else:
                self.process_line(line, random_setting, line_separator, outputs)
                random_setting = 0  # Сбрасываем на значение по умолчанию после обработки строки

        result = " ".join(outputs).strip()  # Объединяем с пробелами и убираем лишние пробелы в начале и конце
        return (result,)

    def process_line(self, line, random_setting, line_separator, outputs):
        if line_separator in line:
            elements = [elem.strip() for elem in line.split(line_separator) if elem.strip()]
            if elements:
                if random_setting == 0:
                    selected = random.choice(elements)
                elif random_setting > len(elements):
                    selected = elements[-1]
                else:
                    selected = elements[random_setting - 1]
                outputs.append(selected + " ")  # Добавляем пробел после каждого выбранного элемента
        else:
            outputs.append(line + " ")  # Добавляем строку без разделителей целиком с пробелом в конце

# Обновляем отображения для ComfyUI
NODE_CLASS_MAPPINGS = {
    "GF_Node": GF_Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GF_Node": "🐵 GF Node (Dynamic Lines)"
}
