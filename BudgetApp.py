class Budget:

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def deposit(self, amount):
      previousBalance = self.balance
      self.balance = self.balance + amount

      return f"Previous: {previousBalance}, Current: {self.balance}"  

  def withdaw(self, amount):
      if self.balance < amount:
         return "Insufficient Funds" 
      else:
          previousBalance = self.balance
          self.balance = self.balance - amount

          return f"Previous: {previousBalance}, Current: {self.balance}"       

  def getBalance(self):
       feedback = f"your balance is {self.balance} in {self.name} Budget"
       
       return feedback

  def transfer(self, amount, transferTo):
      if self.balance < amount:
        return "Insufficient Funds"
      else:
          self.balance = self.balance - amount
          transferTo.balance = transferTo.balance + amount

          feedback = f"you transfered ${amount} to {transferTo.name} budget\n"
          feedback += f"The balance for {self.name} is now {self.balance} while\n"
          feedback += f"The balance for {transferTo.name} is now {transferTo.balance}"

          return feedback  


foodBudget = Budget("food", 3600)
print(f"you have created a {foodBudget.name} budget with ${foodBudget.balance}")
print(foodBudget.deposit(1000))
print(foodBudget.withdaw(2000))
print(foodBudget.getBalance())

print("==============================")

clothingBudget = Budget("clothing", 36000)
print(f"you have created a {clothingBudget.name} budget with ${clothingBudget.balance}")
print(clothingBudget.deposit(1000))
print(clothingBudget.withdaw(2000))
print(clothingBudget.getBalance())
print(clothingBudget.transfer(1000, foodBudget))
print("=============================")


entertainmentBudget = Budget("entertainment", 360000)
print(f"you have created an {entertainmentBudget.name} budget with ${entertainmentBudget.balance}")
print(entertainmentBudget.deposit(1000))
print(entertainmentBudget.withdaw(2000))
print(entertainmentBudget.getBalance())
print(entertainmentBudget.transfer(500, clothingBudget))











