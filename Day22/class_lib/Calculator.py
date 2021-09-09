class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

"""
cal1 = Calculator()
print(calc.add(10))
"""

# UpgradeCalculator() 텍스트
cal2 = UpgradeCalculator()
print(cal2.add(10))
print(cal2.minus(7))
print("결과 :", cal2.value)
