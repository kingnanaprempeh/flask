class Add:
	def __init__ (self, x, y):
		self.x = x
		self.y = y
		self.Sum = x + y
		self.Mult = x * y
		self.Sub  =	 x - y

Total = Add(40,22)
print(Total.x)
print(Total.y)
print(Total.Sum)
print(Total.Mult)
print(Total.Sub)
