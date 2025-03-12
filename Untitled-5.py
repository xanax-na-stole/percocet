class House():
  """описание дома"""
  def __init__(self, street, number):
    """свойства дома"""
    self.street = street
    self.number = number

    def build(self):
        """строит дом"""
        print("дом на улице " + self.street + " под номером " str(self.number) + " построен.")
House1 = House("Гетьманська", 49)      
House1 = House("Гетьманська", 48)

House1.build()

  