from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, __V):
        self.__V = __V
        return self.__V

    @property
    def fabric_consumption(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, __H):
        self.__H = __H
        return self.__H

    @property
    def fabric_consumption(self):
        return 2 * self.H + 0.3


suit1 = Suit(1.8)
suit1.H = 1.4
print(suit1.H)

suit2 = Suit(1.78)
suit3 = Suit(1.76)

coat1 = Coat(54)
coat2 = Coat(52)
coat3 = Coat(50)

lst = [suit1, suit2, suit3,coat1, coat2, coat3]
print(sum(i.fabric_consumption for i in lst))
