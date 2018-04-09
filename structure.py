#python sets
import random

setA = set((10,30,13,10))
setB = set((random.randrange(100) for x in range(100)))
print(setB)

#double underscore methods

class poly():
	def __init__(self, *coeff): #*coeff means that it takes in multiple args
		self.coeff = coeff
	def __repr__(self):
		return "Poly({})".format(self.coeff)

	def __add__(self, other): #other is another poly class that it takes in to add
		return poly(*(x + y for x, y in zip(self.coeff, other.coeff))) #adding the star will take the generator out of the generator

p1 = poly(1,2,3)
p2 = poly(4,5,6)

print(p1) #used by repr double underscore methods
print(p1 + p2)


print(*zip(p1.coeff, p2.coeff))