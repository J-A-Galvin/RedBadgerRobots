class Robot:
	def __init__(self,grid):
		#takes two courdinates and a direction and splits them into an array called coords
		input = raw_input('Enter starting coords and a direction in the form X Y D for this robot: ')
		self.coords = []
		for i in input.split(' '):
			try:
				self.coords.append(int(i))
			except ValueError:
				self.coords.append(i)

		#user can then specify the sequence of moves that the robot will execute
		#only takes first 100 moves
		input = raw_input('Enter sequence of steps to move in for this robot: ').upper()
		if len(input)<100:
			self.sequence = input
		else:
			self.sequence = input[0:100]

		#the grid the robot belongs to is specified in the constructor, every robot must be on a grid
		self.grid = grid
		self.gridSize = grid.gridSize

	


		#asigns a number to each direction
		if self.coords[2].upper() == 'N':
			self.dir = 1
		elif self.coords[2].upper() == 'E':
			self.dir = 2
		elif self.coords[2].upper() == 'S':
			self.dir = 3
		elif self.coords[2].upper() == 'W':
			self.dir = 4

	#adds current position to the grids scent list
	def leaveScent(self):
		self.grid.scents.append([self.coords[0],self.coords[1]])

	#adds or subtracts 1 based on direction turning
	def turnRight(self):
		self.dir += 1
	def turnLeft(self):
		self.dir -= 1
	
	#When going forward the modulo of the direction number is calculated and that will correspond to a direction to move forward in
	#first the robot checks if a move would make it lost and there is no scent then leaves a scent and goes off, then checks if the move is within the grid. If the move would make the robot lost but there is a scent the robot wont move
	def goForward(self):		
		if self.dir % 4 == 1:
			if self.coords[1] + 1 > self.gridSize[1] and [self.coords[0],self.coords[1]] not in self.grid.scents:
				self.leaveScent()
				self.coords[1]+=1
				self.coords.append('LOST')
			elif self.coords[1] + 1 <= self.gridSize[1]:
				self.coords[1]+=1
		
		elif self.dir % 4 == 2:
			if self.coords[0] + 1 > self.gridSize[0] and [self.coords[0],self.coords[1]] not in self.grid.scents:
				self.leaveScent()
				self.coords[0]+=1
				self.coords.append('LOST')
			elif self.coords[0] + 1 <= self.gridSize[0]:
				self.coords[0]+=1
		
		elif self.dir % 4 == 3:
			if self.coords[1] - 1 < 0 and [self.coords[0],self.coords[1]] not in self.grid.scents:
				self.leaveScent()
				self.coords[1]-=1
				self.coords.append('LOST')
			elif self.coords[1] - 1 >= 0:
				self.coords[1]-=1
		
		elif self.dir % 4 == 0:
			if self.coords[0] - 1 > 0 and [self.coords[0],self.coords[1]] not in self.grid.scents:
				self.leaveScent()
				self.coords[1]-=1
				self.coords.append('LOST')
			elif self.coords[0] - 1 >= 0:
				self.coords[0]-=1
	

	#reads the sequence of moves and determines which functions to execute
	#this is what makes the moveset extensible because you just have to add new letters that correspond to moves.
	def move(self):
		for move in self.sequence:
			if move == 'F':
				self.goForward()
			elif move == 'R':
				self.turnRight()
			elif move == 'L':
				self.turnLeft()

	#updates the letter direction of the robot for when a human wants to read it
	def updateDir(self):
		if self.dir % 4 == 1:
			self.coords[2] = 'N'
		elif self.dir % 4 == 2:
			self.coords[2] = 'E'
		elif self.dir % 4 == 3:
			self.coords[2] = 'S'
		elif self.dir % 4 == 0:
			self.coords[2] = 'W'



