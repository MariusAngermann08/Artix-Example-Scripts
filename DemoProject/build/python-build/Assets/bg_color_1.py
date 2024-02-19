class bg_color_1(engine.Method):
	color = False
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		if not self.color:
			self.scene.bgcolor = (211, 237, 242)
			self.color = True
