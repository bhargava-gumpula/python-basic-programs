class employee:
   def __init__(self, name, id, position, income):
      self.name = name
      self.id = id
      self.position = position
      self.income = income
      self.location = "San Jose"

   def set_name(self, name):
      self.name = name
   
   def get_name(self):
      return(self.name)
     

   def set_id(self, id):
      self.id = id

   def get_id(self):
      return(self.id)

emp_1 = employee("Bhargava", 758394, "Engineer 1", 10000) 						
emp_1.set_name("Suresh")
print ("Employe name:" + emp_1.get_name())		
