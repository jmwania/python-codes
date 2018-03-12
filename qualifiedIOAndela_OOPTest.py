class ShoppingCart(object):
  """Creates class ShoppingCart for adding and removing items"""
  def __init__(self):
    self.total = 0
    self.items = {}
  def add_item(self,item_name,quantity,price):
    self.total += quantity*price
    self.items[item_name] = quantity
  def remove_item(self,item_name,quantity,price):
    if self.items[item_name] < quantity:
      del self.items[item_name]
      self.total -= price
    else:
      self.items[item_name] -= quantity
      self.total -= quantity*price
  def checkout(self,cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    return cash_paid - self.total
    
    
class Shop(ShoppingCart):
  """Creates a class Shop that inherits from ShoppingCart"""
  def __init__(self):
    self.quantity = 100
  def remove_item(self):
    self.quantity -= 1