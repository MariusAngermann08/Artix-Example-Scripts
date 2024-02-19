from random import randint

class CloudCloneScript(engine.Method):
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		self.object.move([self.object.speed,0])
		if self.object.position.x >= self.engine.res[0]+100:
			self.scene.game_objects.remove(self.object)

class CloudSpawn(engine.Method):
	counter = 0
	index = 0
	clouds = []
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		if self.counter == 120:
			self.counter = 0
			#Create Clone
			texture = self.object.image_textures
			pos = self.object.position.get()
			scale = self.object.scale.get()
			cloud = engine.GameObject("cloud"+str(self.index), texture)
			number = randint(0,1)
			cloud.position.set(pos)
			if number == 0: cloud.scale.set([200,250])
			else: cloud.scale.set([300,370])
			cloud.speed = randint(1,3)
			cloud.position.y = randint(-20,160)
			self.scene.addObject(cloud)
			cloud.addMethod(CloudCloneScript)
			self.clouds.append(cloud)
			self.index += 1
		self.counter += 1

