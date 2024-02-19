import pygame
import pymunk
import sys
import math
import pymunk.pygame_util
from InputMap import input_map
from Engine import Engine

engine = Engine("JugendForscht_Demo1", [800,600], 60)

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




class bg_color_1(engine.Method):
	color = False
	def __init__(self, engine, scene, object):
		super().__init__(engine, scene, object)

	def update(self):
		if not self.color:
			self.scene.bgcolor = (211, 237, 242)
			self.color = True


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




main_menu = engine.Scene("main_menu", (255,255,255))
engine.addScene(main_menu)

Level01 = engine.Scene("Level01", (255,255,255))
engine.addScene(Level01)

End = engine.Scene("End", (255,255,255))
engine.addScene(End)

ground1 = engine.GameObject("ground1", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
ground1.position.x = 21
ground1.position.y = 525
ground1.scale.x = 200
ground1.scale.y = 50
main_menu.addObject(ground1)
ground1.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
ground2 = engine.GameObject("ground2", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
ground2.position.x = 281
ground2.position.y = 480
ground2.scale.x = 200
ground2.scale.y = 50
main_menu.addObject(ground2)
ground2.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
ground3 = engine.GameObject("ground3", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
ground3.position.x = 542
ground3.position.y = 525
ground3.scale.x = 200
ground3.scale.y = 50
main_menu.addObject(ground3)
ground3.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
CloudSpawner = engine.GameObject("CloudSpawner", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\cloud.png"])
CloudSpawner.position.x = -300
CloudSpawner.position.y = 50
CloudSpawner.scale.x = 200
CloudSpawner.scale.y = 250
main_menu.addObject(CloudSpawner)
CloudSpawner.addMethod(CloudSpawn)
Apple = engine.GameObject("Apple", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\apple.png"])
Apple.position.x = 356
Apple.position.y = 441
Apple.scale.x = 55
Apple.scale.y = 75
main_menu.addObject(Apple)
Apple.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"dynamic","collider":"box"})
Apple.addMethod(IdleScript)
Apple.addMethod(bg_color_1)
Headline = engine.GameObject("Headline", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\label.png"])
Headline.position.x = 200
Headline.position.y = 21
Headline.scale.x = 400
Headline.scale.y = 100
main_menu.addObject(Headline)
Headline.addMethod(label_animation)
StartLabel = engine.GameObject("StartLabel", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\startlabel.png"])
StartLabel.position.x = 250
StartLabel.position.y = 195
StartLabel.scale.x = 300
StartLabel.scale.y = 50
main_menu.addObject(StartLabel)
Plat1 = engine.GameObject("Plat1", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
Plat1.position.x = 70
Plat1.position.y = 455
Plat1.scale.x = 300
Plat1.scale.y = 75
Level01.addObject(Plat1)
Plat1.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
Plat2 = engine.GameObject("Plat2", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
Plat2.position.x = 305
Plat2.position.y = 431
Plat2.scale.x = 300
Plat2.scale.y = 75
Level01.addObject(Plat2)
Plat2.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
Tree = engine.GameObject("Tree", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\tree.png"])
Tree.position.x = 44
Tree.position.y = 160
Tree.scale.x = 300
Tree.scale.y = 300
Level01.addObject(Tree)
Apple = engine.GameObject("Apple", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\apple.png"])
Apple.position.x = 203
Apple.position.y = 232
Apple.scale.x = 55
Apple.scale.y = 75
Level01.addObject(Apple)
Apple.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"dynamic","collider":"box"})
Apple.addMethod(bg_color_1)
Apple.addMethod(AppleController)
Apple.addMethod(CameraFollow)
Plat3 = engine.GameObject("Plat3", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
Plat3.position.x = 738
Plat3.position.y = 467
Plat3.scale.x = 200
Plat3.scale.y = 50
Level01.addObject(Plat3)
Plat3.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
Barrier = engine.GameObject("Barrier", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\rock.png"])
Barrier.position.x = 40
Barrier.position.y = 404
Barrier.scale.x = 100
Barrier.scale.y = 100
Level01.addObject(Barrier)
Barrier.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
Plat4 = engine.GameObject("Plat4", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
Plat4.position.x = 1038
Plat4.position.y = 416
Plat4.scale.x = 200
Plat4.scale.y = 50
Level01.addObject(Plat4)
Plat4.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})
key = engine.GameObject("key", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\key.png"])
key.position.x = 1113
key.position.y = 352
key.scale.x = 60
key.scale.y = 45
Level01.addObject(key)
Door = engine.GameObject("Door", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\door.png"])
Door.position.x = 1447
Door.position.y = 249
Door.scale.x = 150
Door.scale.y = 200
Level01.addObject(Door)
Plat5 = engine.GameObject("Plat5", ["C:\\Users\\xdgam\\Documents\\ArtixEngine-main\\projects\\JugendForscht_Demo1\\build\\python-build\\Assets\\ground1.png"])
Plat5.position.x = 1383
Plat5.position.y = 443
Plat5.scale.x = 300
Plat5.scale.y = 50
Level01.addObject(Plat5)
Plat5.addAttribute("PhysicsObject", {"mass":1,"inertia":100,"physics_type":"static","collider":"box"})

engine.loadScene("main_menu")
engine.run()