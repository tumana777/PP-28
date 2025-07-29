# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#
#     if b == 0:
#         raise ValueError("Can't divide by zero!")
#
#     return a / b
#
# def is_even(a):
#     return a % 2 == 0

# print(is_even(10))
# print(is_even(7))

# if __name__ == "__main__":
#     print(add(5, 2))


class Student:
    discount = 0.9

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def get_email(self, domain):
        return f"{self.first_name}.{self.last_name}@{domain}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self):
        self.pay *= self.discount


















