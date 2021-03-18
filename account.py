# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         return "Amount exceeded balance"
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
#
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())

dict_of_dict = {"Pesho": {"kniga1": 1, "kniga2": 2, "kniga3": 3, "kniga4": 4}}

dict_of_dict["Pesho"].pop("kniga1")
print(dict_of_dict["Pesho"])
