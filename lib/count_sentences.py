class MyString:
    def __init__(self, value=""):  # default to empty string, not None
        self._value = ""
        self.value = value  # Use the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ""  # fallback to empty string to avoid errors

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        if not self.value:
            return 0
        sentences = re.findall(r'[^.!?]+[.!?]', self.value)
        return len(sentences)
