"""This module provides
  an interface for area of
  2D shapes like circle,
  square, rectangle.
  """
import math
pi = math.pi

def circle(radius):
	""" input: radius
		output: pi*r**2"""
	return pi*radius**2

def square(side):
	""" input: side
		output: side*side
		"""
	return side**2

def rectangle(length, breadth):
	"""input: l and b
		output: l*b"""
	return length * breadth


if __name__ == '__main__':
    import sys
    print(sys.argv)
