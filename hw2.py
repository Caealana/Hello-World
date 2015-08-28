#Sabrina Sayasith
#HW 2
#9/17/14

import math

def distance(x1, y1, x2, y2):
    """output: the distance between 2 points
    input: the coordinates of the two points(x1, y1) and (x2, y2)
    """
    return math.sqrt( ((x1-x2) **2) + ( (y1-y2)**2))


def isInside(x1, y1, r, x2, y2):
	"""output: true if point is within circle, false otherwise
	input: coordinates of circle center(x1,x2), coordinates of point(x2,y2), radius
	"""

	return math.sqrt( ((x1 - x2) **2) + ( (y1 - y2)**2) ) < r


def sq(x):
	"""output: the square of x
	input x = integer to be squared
	"""
	return x**2


def interp(low, hi, fraction):
	"""output: linear interpolation between low and hi numbers by fraction
	input: low and hi - integers/floats + fraction you want to interpolate by
	"""
	x= hi - low
	x = fraction*x
	x = low + x
	return x


def checkends(s):
	"""Output: returns True if first and last letter of string match. Otherwise: false
	input: s = a string
	"""
	return s[0] == s[-1]


def flipside(s):
	"""output: last half of string becomes first half of string
	input: s= a string
	"""
	x = len(s)//2
	return s[x::] + s[0:x]
