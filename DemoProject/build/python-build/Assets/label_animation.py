class label_animation(engine.Method):
	mode = "+"
	speed = 0.5
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		if self.object.position.y <= 20 and self.mode == "-":
			self.mode = "+"
		elif self.object.position.y >= 45 and self.mode == "+":
			self.mode = "-"

		if self.mode == "+":
			self.object.position.y += self.speed
		elif self.mode == "-":
			self.object.position.y -= self.speed
	

