class AppleController(engine.Method):
	pick = False
	follow = False
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)
		
		#Add Tags
		self.scene.getObjectByName("Plat1").add_tag("ground")
		self.scene.getObjectByName("Plat2").add_tag("ground")

	def update(self):
		if self.engine.key_hold("a"):
			self.object.move([-3,0])
		elif self.engine.key_hold("d"):
			self.object.move([3,0])
		
		if self.engine.key_pressed("space"):
			self.object.apply_force([0,-5])
		
		if self.object.position.y >= 700:
			self.object.set_position([164,222])
		
		
		if not self.pick:
			key = self.scene.getObjectByName("key")
			if self.engine.rectangular_collision(self.object,key):
				self.follow = True
		
		if self.follow:
			key = self.scene.getObjectByName("key")
			key.position.set(self.object.position.get())
			key.move([0,-30])
		
		door = self.scene.getObjectByName("Door")
		if self.engine.rectangular_collision(self.object,door):
			if self.follow: self.engine.loadScene("End")
			


