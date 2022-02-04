import random
import ursina as ur
from ursina.prefabs.first_person_controller import FirstPersonController

app = ur.Ursina()

grass_texture = ur.load_texture('assets/grass_block.png')
stone_texture = ur.load_texture('assets/stone_block.png')
brick_texture = ur.load_texture('assets/brick_block.png')
dirt_texture = ur.load_texture('assets/dirt_block.png')

class Voxel(ur.Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
                parent = ur.scene,
                position = position,
                model = 'assets/block',
                origin_y = 0.5,
                texture = grass_texture,
                color = ur.color.color(0,0,random.uniform(0.9,1)), # color default is HSV format
                scale = 0.5)
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # ur.mouse.normal is the surface where mouse is pointing at
                voxel = Voxel(position= (self.position + ur.mouse.normal))
            
            if key == 'right mouse down':
                ur.destroy(self)


for z in range(20):
    for x in range(20):
        voxel = Voxel( position = (x, 0, z) )
player = FirstPersonController()

app.run()