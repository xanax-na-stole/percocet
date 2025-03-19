def message(x):
  def print_message(y):
    return x, y
  return print_message

fresco = message(7)
print(fresco(3))
print(fresco(2))