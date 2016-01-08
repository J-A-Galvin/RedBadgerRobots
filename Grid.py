class Grid:
	def __init__(self):
		
		#Takes input in the same form that the problem specs says and puts it into an array, only allows dimensions up to 50
		input = raw_input('Enter size of grid in the form X Y: ')
		self.gridSize = []
		for i in input.split(' '):
			if int(i) <= 50:
				self.gridSize.append(int(i))
			else:
				self.gridSize.append(50)
		
		#Holds the coordinates of any tiles that have a robot scent on them
		self.scents = []


