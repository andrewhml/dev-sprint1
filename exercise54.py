# This is where Exercise 5.4 goes
# Name: Andrew Lee

def is_triangle (a, b, c):
	if a > c + b:
		print 'No'
	elif b > c + a:
		print 'No'
	elif c > b + a:
		print 'No'
	else:
		print 'Yes'


def input_triangle():
	side1 = int ( raw_input('How long is side 1?\n') )
	side2 = int (raw_input('How long is side 2?\n'))
	side3 = int(raw_input('How long is side 3?\n')	)
	is_triangle(side1, side2, side3)

input_triangle()