class CounterMachine: # Итератор
    def __init__(self, limit):
        self.UpTo = limit
        self.Current = 0

    def iterate(self):
        if self.Current < self.UpTo:
            self.Current = self.Current + 1
            return 1
        else:
            raise StopIteration

    def autoIterations(self):
        try:
            while True:
                self.iterate()
                print("Successful iteration. Value is: " + str(self.Current))
        except StopIteration:
            print("End of iterations")

class Inverter: # Инвертор
    def invertInteger(self, n):
        return -n

    def invertString(self, charArray):
        i = 0
        result = ""
        while i < len(charArray):
            result = charArray[i] + result
            i = i+1
        return result

if __name__ == "__main__":
    val = input()
    CM = CounterMachine(int(val))
    CM.autoIterations()

    inverter = Inverter()
    val = input()
    print(inverter.invertString(val))