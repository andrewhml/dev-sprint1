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



def eq_triangle(t, length):
	fd(t, length)
	lt(t, 120)
	fd(t, length)
	lt(t, 120)
	fd(t, length)

def koch_curve(t, length):
	if length < 3:
		fd(t, length)
	angle = 60
	fd(t, length/3)
	lt(t, 60)
	fd(t, length/3)
	rt(t, 120)
	fd(t, length/3)
	lt(t, 60)

koch_curve(bob, 100)



#draw(bob, 25, 3)
#eq_triangle(bob, 25)

wait_for_user()