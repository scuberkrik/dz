class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}"


complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(4, 1)

result_add = complex1 + complex2
print(f"Сумма: {result_add}")

result_mul = complex1 * complex2
print(f"Произведение: {result_mul}")

correct_add = ComplexNumber(6, 4)
correct_mul = ComplexNumber(5, 14)
assert result_add.real == correct_add.real and result_add.imag == correct_add.imag, "Неверный результат сложения"
assert result_mul.real == correct_mul.real and result_mul.imag == correct_mul.imag, "Неверный результат умножения"
