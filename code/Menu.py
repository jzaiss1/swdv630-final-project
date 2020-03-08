# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 5 Assignment - Patterns (Iterator)

class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.quantity = 1
    # TODO: Increment the quantity
  
  def __str__(self):
        return "{}: $ {}".format(self.name, self.price)

class OrderIterator:
  def __init__(self, items):
    self.indx = 0
    self.items = items

  def has_next(self):
    return False if self.indx >= len(self.items) else True

  def next(self):
    item = self.items[self.indx]
    self.indx += 1
    return item

  def remove(self):
    return self.items.pop()

class Sale:
  def __init__(self):
    self.id = self.createId()
    self.items = []

  def createId(self):
    pass
  
  def add(self, item):
    self.items.append(item)
  
  def iterator(self):
    return OrderIterator(self.items)

  # TODO: Figure out a total sale calculator

if __name__ == '__main__':
  i1 = Item("hammer", 14.95)
  i2 = Item("wrench", 11.45)
  i3 = Item("box of nails", 8.25)
  
  sale = Sale()
  sale.add(i1)
  sale.add(i2)
  sale.add(i3)

  print("\nItems Sold:")
  iterator = sale.iterator()

  while iterator.has_next():
    item = iterator.next()
    print(item)

  print("\nRemoving last item returned")
  iterator.remove() 
  # TODO: how to remove from inside of the list not only the last item

  print("\nItems Sold:")
  iterator = sale.iterator()
  while iterator.has_next():
    item = iterator.next()
    print(item)
