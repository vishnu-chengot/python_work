class products():
  def __init__(self,name,price,color):
    self.name = name
    self.price = price
    self.color = color

  def displayproducts(self):
    print(self.name)
    print(self.price)
    print(self.color)  




p1 = products('pen',10,'black')
p2 = products('marker',15,'red')

p1.displayproducts()
p2.displayproducts()



