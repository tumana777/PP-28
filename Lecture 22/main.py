# Single Responsibility Principle
# Bad Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report for {self.data}"
#
#     def write_report(self, filename):
#         with open(filename, "w") as f:
#             f.write(self.generate_report())
#
# r = Report("Test")

# Good Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report for {self.data}"
#
# r = Report("Test")
#
# class ReportWriter:
#     @staticmethod
#     def write_to_file(report:Report, filename):
#         with open(filename, "w") as f:
#             f.write(report.generate_report())
#
# rw = ReportWriter()
#
# rw.write_to_file(r, "report.txt")


# Open/Close Principle
# Bad example

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def get_discounted_price(self, discount_type):
#         if discount_type == "VIP":
#             return self.price * 0.9
#         elif discount_type == "VIP+":
#             return self.price * 0.8
#         else:
#             return self.price

# Good Example
# from abc import ABC, abstractmethod
#
# class Discount(ABC):
#     def __init__(self, price):
#         self.price = price
#
#     @abstractmethod
#     def get_discount(self):
#         pass
#
# class VIPDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.9
#
# class VIPPlusDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.8
#
# class NormalDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.95


# Liskov Substitution Principle
# Bad Example

# class Bird:
#     def fly(self):
#         return "I can fly"
#
# class Penguin(Bird):
#     def fly(self):
#         return "I can't fly"

# Good Example

# class Bird:
#     @staticmethod
#     def move():
#         return "I can move"
#
# class FlyingBird(Bird):
#     @staticmethod
#     def fly():
#         return "I can fly"
#
# class Penguin(Bird):
#     @staticmethod
#     def swim():
#         return "I can swim"


# Interface Segregation Principle
# Bad Example

# class Worker:
#     def work(self):
#         pass
#
#     def eat(self):
#         pass
#
# class Manager:
#     def work(self):
#         return "I can work"
#
#     def eat(self):
#         return "I can eat"
#
# class Robot:
#     def work(self):
#         return "I can work"
#
#     def eat(self):
#         return "I can't eat"

# Good Exaple

# from abc import ABC, abstractmethod
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Chargeable(ABC):
#     @abstractmethod
#     def charge(self):
#         pass
#
# class Manager(Workable, Eatable):
#     def work(self):
#         return "I can work"
#
#     def eat(self):
#         return "I can eat"
#
# class Robot(Workable, Chargeable):
#     def work(self):
#         return "I can work"
#
#     def charge(self):
#         return "I can charge"


# Dependency Inversion Principle
# Bad Example

# class MySqlDatabase:
#     @staticmethod
#     def connect():
#         return "Connected to MySQL database"
#
# class Application:
#     def __init__(self):
#         self.db = MySqlDatabase()
#
#     def run(self):
#         return self.db.connect()
#
# app = Application()
#
# print(app.run())


# Good Example

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySqlDatabase(Database):
    def connect(self):
        return "Connected to MySQL database"

class PostgresDatabase(Database):
    def connect(self):
        return "Connected to Postgres database"

class OracleDatabase(Database):
    def connect(self):
        return "Connected to Oracle database"

class Application:
    def __init__(self, db:Database):
        self.db = db

    def run(self):
        return self.db.connect()

mysql_app = Application(MySqlDatabase())

postgres_app = Application(PostgresDatabase())

oracle_app = Application(OracleDatabase())

print(mysql_app.run())
print(postgres_app.run())







