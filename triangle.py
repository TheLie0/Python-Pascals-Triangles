from builtin_filters import *
from custom_filters import *

def Triangle(size):
	"""takes int size. Generates a pascals triangle with that number of rows."""
	if size == 1:
		return [[1]]
	else:
		rows = Triangle(size-1)
		newRow = [1]
		for index in range(len(rows[-1])-1):
			newRow.append(rows[-1][index] + rows[-1][index+1])
		newRow.append(1)
		rows.append(newRow)
		return rows

def BeautifyTri(triangle = Triangle(10)):
	"""takes triangle (default is normal Tri with length 10), returns middle-aligned tri."""
	rowStrList = []
	outStr = ""
	for row in triangle:
		rowStr = ""
		for num in row:
			rowStr += str(num) + " "
		rowStrList.append(rowStr[:len(rowStr)])
	for rowStr in rowStrList:
		while len(rowStr) < len(rowStrList[-1]):
			rowStr = " " + rowStr
			if len(rowStr) < len(rowStrList[-1]):
				rowStr += " "
		rowStr += "\n"
		outStr += rowStr
	return outStr

def FilterTri(inTri = Triangle(10), filterFunc = Modulo2):
	"""takes triangle inTri and/or function filterFunc (defaults are Triangle(10) and Modulo2).
	 Returns filtered Triangle."""
	failed = False
	if type(filterFunc) == str:
		try:
			filterFunc = eval(filterFunc)
		except NameError:
			failed = True
	if failed:
		print """This filter doesn't seem to exist :/ I imagine it would be really
cool if it did... Maybe create it? ^^ But since it would be really
boring if nothing happened, have a normal pascal's triangle."""
		return Triangle(10)
	outTri = []
	for row in inTri:
		outRow = []
		for num in row:
			try:
				outNum = filterFunc(num)
				outRow.append(outNum)
			except NameError:
				failed = True
		outTri.append(outRow)
	if failed:
		print """This filter doesn't seem to exist :/ I imagine it would be really
cool if it did... Maybe create it? ^^ But since it would be really
boring if nothing happened, have a normal pascal's triangle."""
		return Triangle(10)
	return outTri