class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


my_complex_number_1 = ComplexNumber(9, 5)
my_complex_number_2 = ComplexNumber(-5, 6)
print(f"Сумма: {my_complex_number_1 + my_complex_number_2}")
print(f"Произведение: {my_complex_number_1 * my_complex_number_2}")

