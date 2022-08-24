from abc import ABC, abstractmethod


class Stock:
    def __init__(self):
        self.__lst = []

    def __str__(self):
        return "\n".join([f"{i}) {k[0]} - в наличие {k[1]}" for i, k in enumerate(self.__lst)])

    def add(self, *lst_equipment):
        count = list(map(lambda x: type(x[1]) == int, lst_equipment))
        if False in count:
            print("Число товаров должно быть целым числом")
            return None
        [self.__lst.append(i) for i in lst_equipment]

    def to_company(self, company, *lst_equipment):
        flag = True
        lst_equipment = sorted(lst_equipment)
        index = list(map(lambda x: x[0], lst_equipment))
        count = list(map(lambda x: type(x[1]) == int, lst_equipment))
        if False in count:
            print("Число товаров должно быть целым числом")
            return None
        has_dublicate = {i: index.count(i) for i in index if index.count(i) > 1}
        if has_dublicate:
            print(f"Обнаружены повторения {has_dublicate}")
            flag = False
        else:
            change = [value for i, value in enumerate(self.__lst) if i in index]
            lst_change = []
            lst_dublicate = []
            lst_dublicate.extend(self.__lst)
            for x, y in zip(change, lst_equipment):
                if x[1] >= y[1]:
                    lst_dublicate[y[0]] = [x[0], x[1] - y[1]]
                    lst_change.append([x[0], y[1]])
                else:
                    print(f"Число запрашиваемого {x[0]} товара больше {x[1]},чем есть на складе {y[1]}")
                    flag = False
        if flag:
            self.__lst = lst_dublicate
            company.add(lst_change)


class Company:
    def __init__(self):
        self.__lst = []

    def __str__(self):
        return "\n".join([f"{i}) {k[0]} - в наличие {k[1]}" for i, k in enumerate(self.__lst)])

    def add(self, *lst_equipment):
        [self.__lst.extend(i) for i in lst_equipment]


class OfficeEquipment(ABC):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.specifications = {}

    def __str__(self):
        return f"{self.brand} {self.model}"

    @abstractmethod
    def get_specifications(self, max_format_print, speed, dpi):
        self.specifications = {"speed": speed, "dpi": dpi}

    def info(self):
        print(
            f"{self.brand} {self.model} c ценой {self.price} c характеристиками {self.specifications}")


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.specifications = {}

    def get_specifications(self, color, speed, dpi):
        self.specifications = {"printing color": color, "speed": speed, "dpi": dpi}


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.specifications = {}

    def get_specifications(self, speed, dpi):
        self.specifications = {"speed": speed, "dpi": dpi}


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.specifications = {}

    def get_specifications(self, color, speed, dpi):
        self.specifications = {"printing color": color, "speed": speed, "dpi": dpi}


xerox = Xerox("HP", "kL23", 10000)
printer = Printer("HP", "231NL", 14000)
scanner = Scanner("Canon", "2a2aL", 12000)
printer.get_specifications("чб", 5, 300)
printer.info()
print("-" * 20)

stock = Stock()
stock.add([xerox, 3], [printer, 4], [scanner, 5])
print(stock)
print("-" * 20)

company = Company()
stock.to_company(company, [2, 3], [1, 5], [0, 4])
print("-" * 20)
print(stock)
print("-" * 20)
stock.to_company(company, [0, 2], [1, 2])
print(stock)
print("-" * 20)
print(company)
