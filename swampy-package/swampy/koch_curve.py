# Koch Curve excercise from Week 1

# Name: Andrew Lee

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()		
bob.color = 'purple'
bob.delay = 0.01

def draw(t, length, n):
	if n == 0:
		return
	angle = 60
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)


def koch_curve(t, length):

	if length < 3:
		fd(t, length)
		return
	else:	
		n = length/3.0
		koch_curve(t, n)
		lt(t, 60)
		koch_curve(t, n)
		rt(t, 120)
		koch_curve(t, n)
		lt(t, 60)
		koch_curve(t, n)

koch_curve(bob, 100)



#draw(bob, 25, 3)
#eq_triangle(bob, 25)

wait_for_user()