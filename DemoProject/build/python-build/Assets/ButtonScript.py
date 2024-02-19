class ButtonScript(engine.Method):
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		mouse_pos = self.engine.getMousePosTuple()
		button_rect = self.object.surface.get_rect()
		if button_rect.collidepoint(mouse_pos):
			self.object.scale.set([400,133])
		else:
			self.object.scale.set([300,100])

