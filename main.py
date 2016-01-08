import Robot,Grid
robots = []
#instantiates the grid
mars = Grid.Grid()

#lets you choose how many robots to make
input = raw_input('How many Robots do you wish to make? ')

#creates the desired number of robots
for i in range(int(input)):
	robot = Robot.Robot(mars)
	robots.append(robot)

#makes robots move and then prints the results
for robot in robots:
	robot.move()
	robot.updateDir()
	print robot.coords
