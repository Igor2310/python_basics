class Error(Exception):
    def __init__(self):
        super().__init__("Должно быть введено число")


class Numbers:
    def __init__(self):
        self.lst = []

    def __str__(self):
        return f"{self.lst}"

    def input_data(self):
        while True:
            try:
                text = input()
                if text.lower() == "stop":
                    break
                if text.count(".") > 1 or text == '' or text[0] == ".":
                    raise Error
                for i in text:
                    if i.isdigit() or i == ".":
                        continue
                    else:
                        raise Error()
                self.lst.append(float(text))
            except Exception as err:
                print(err)


number = Numbers()
number.input_data()
print(number)
