class employee():
    def realse_amount(self):
      print("release 1 lakh")

class manager(employee):
    def realse_amount(self):
      print("release 5 lakh")

manager1 = manager()

manager1.realse_amount()