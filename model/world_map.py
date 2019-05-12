

class world_map():
	# constant
	X_LENGTH = 6
	Y_LENGTH = 20

	# variable
	map = []
	hero_pos = {'x':1, 'y':1}


	"""docstring for world_map"""
	def __init__(self):
		super(world_map, self).__init__()

		# init map
		for i in range(self.X_LENGTH):
			temp = ['-' for x in range(1000)]
			if i == 0 or i == self.X_LENGTH-1:
				temp = ['=' for x in range(1000)]

			temp[0] = '|'
			temp[self.Y_LENGTH-1] = '|'
			
			
			self.map.append(temp)

		# init hero position
		x = self.hero_pos['x']
		y = self.hero_pos['y']
		self.map[x][y] = '1'


	def print_world(self):
		X_LEN = self.X_LENGTH
		Y_LEN = self.Y_LENGTH

		for x in range(X_LEN):
			for y in range(Y_LEN):
				print(self.map[x][y], end = '')
			print()