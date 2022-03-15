import enum


class Pin(enum.Enum):
    a = enum.auto()
    b = enum.auto()


class LogicGate:
    def __init__(self, label):
        self.__set_label(label)

    def __set_label(self, label):
        self.__label = str(label)

    def __get_label(self):
        return self.__label

    label = property(__get_label, __set_label)


class Connector:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

        dest.set_next_pin(self)


class BinaryGate(LogicGate):

    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin(self, pin):
        if pin is Pin.a:
            if self.pin_a is None:
                return int(input("Enter pin A input for gate " + self.label + ": "))
            else:
                return self.pin_a.source.output
        elif pin is Pin.b:
            if self.pin_a is None:
                return int(input("Enter pin B input for gate " + self.label + ": "))
            else:
                return self.pin_b.source.output
        else:
            raise TypeError("Argument is neighter enum type Pin.a or Pin.b")

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: No empty pins")


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def __output(self):
        if self.get_pin(Pin.a) == 1 and self.get_pin(Pin.b) == 1:
            return 1
        return 0

    output = property(__output)


class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def __output(self):
        if self.get_pin(Pin.a) == 1 or self.get_pin(Pin.b) == 1:
            return 1
        return 0

    output = property(__output)


class NotGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter input for gate " + self.label + ": "))
        return self.pin.source.output

    def set_next_pin(self, source):
        if self.pin is not None:
            raise RuntimeError("Error: No empty pins")
        self.pin = source

    def __output(self):
        if self.get_pin() == 1:
            return 0
        return 1

    output = property(__output)


class NandGate(AndGate):
    def __init__(self, label):
        super().__init__(label)

    def __output(self):
        if super().output == 1:
            return 0
        return 1

    output = property(__output)


class NorGate(OrGate):
    def __init__(self, label):
        super().__init__(label)

    def __output(self):
        if super().output == 1:
            return 0
        return 1

    output = property(__output)
