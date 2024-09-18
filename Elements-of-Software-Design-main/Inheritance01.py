class Item:
   def __init__(self):
       self.name = ''
       self.quantity = 0

   def set_name(self, nm):
       self.name = nm

   def set_quantity(self, qnty):
       self.quantity = qnty

   def display(self):
       print(self.name, self.quantity)


class Produce(Item):  # Derived from Item
   def __init__(self):
       Item.__init__(self)  # Call base class constructor
       self.expiration = ''

   def set_expiration(self, expir):
       self.expiration = expir

   def get_expiration(self):
       return self.expiration

   def display(self):
       print(self.name, self.quantity, end=' ')
       print(f'  (Expires: {self.expiration})')


item1 = Item()
item1.set_name('Smith Cereal')
item1.set_quantity(9)
item1.display()  # Will call Item's display()

item2 = Produce()
item2.set_name('Apples')
item2.set_quantity(40)
item2.set_expiration('May 5, 2012')
item2.display()