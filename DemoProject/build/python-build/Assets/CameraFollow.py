class CameraFollow(engine.Method):
	mode = "both"
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		screen_width = self.engine.res[0]
		screen_height = self.engine.res[1]
		object_x = self.object.position.x 
		object_y = self.object.position.y
		object_width = self.object.scale.x
		object_height = self.object.scale.y
		camx = object_x-(screen_width/2)-(object_width/2)
		if self.mode == "both":
			camy = object_y-(screen_height/2)-(object_height/2)
		else:
			camy = self.scene.camera_pos[1]
		self.scene.camera_pos = (camx,camy)


