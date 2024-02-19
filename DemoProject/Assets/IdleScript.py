class IdleScript(engine.Method):
	counter = 0
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		if self.counter == 120:
			self.object.apply_force([0,-3.5])
			self.counter = 0
		self.counter += 1
		
		if self.engine.key_pressed("space"):
			self.engine.loadScene("Level01")


