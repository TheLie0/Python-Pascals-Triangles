from triangle import Triangle, BeautifyTri, FilterTri

print """Hi! I'm glad You chose me as your go to Pascal's Triangle software! You are currently running my main.py,
so I assume You're interested in using my friendly I/O access. Feel free to also implement my functions
in any of your own code. For now, I will just ask you for the numbers of lines you want and which filter
to apply. A filter usually applies some function to each number in the triangle. You can create your own
filters in custom_filters.py. If you don't know what to do use the filter "help" ;). Have Fun!"""

while True:
	error = False
	try:
		size = int(raw_input("Number of rows: "))
	except ValueError:
		print "Damn, I couldn't get that number. Please only use numerical characters here..."
		error = True
	if not error:
		filter = raw_input("Filter: ")
		if filter == "none":
			print BeautifyTri(Triangle(size))
		elif filter == "help" or filter == "Help" or filter == "HELP":
			print """Here are all the builtin filters, try them out as you like:
- Modulo2
- Modulo3
- Digits
- IsPrime
- Mod2Vis
- Mod3Vis
- PrimeVis

!The Prime family of filters might take a while for triangles over 20 rows!"""
		else:
			print BeautifyTri(FilterTri(Triangle(size), filter))