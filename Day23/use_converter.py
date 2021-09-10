from Day24.classlib.converter import ScaleConverter

# SclaeConverter를 상속한 Converters 클래스 정의
# 화씨 온도(F) = 섭씨 온도 x 1.8 + 32
class Converters(ScaleConverter):
    def __init__(self, units_from, units_to, factor, factor2):
        super().__init__(units_from, units_to, factor)
        self.factor2 = factor2

    def converter(self, val):
        return super().convert(val) + self.factor2

conv = Converters("C", "F", 1.8, 32)
print("20C를 화씨 온도로 변환")
print(str(conv.converter(20)) + conv.units_to)


