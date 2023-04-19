# ------------- Custom Exceptions -------------

class FahrenheitError(Exception):
  
  def __init__(self, temp, *args):
    super().__init__(args)

    self.min_temp = 32
    self.max_temp = 212
    self.temp = temp

  def __str__(self):
    return f'El valor {self.temp} no está entre {self.min_temp} y {self.max_temp}'
  
def fahrenheit_to_celsius(temp):
  if temp < FahrenheitError.min_temp or temp > FahrenheitError.max_temp:
    raise FahrenheitError(temp)

  return (temp - 32) * 5 / 9