import random
import ursina as ur
from ursina.prefabs.first_person_controller import FirstPersonController

app = ur.Ursina()

grass_texture = ur.load_texture('assets/grass_block.png')
stone_texture = ur.load_texture('assets/stone_block.png')
brick_texture = ur.load_texture('assets/brick_block.png')
dirt_texture = ur.load_texture('assets/dirt_block.png')

block_pick = 1

def update():
    # this function gets called every frame
    global block_pick

    if ur.held_keys['1']: block_pick = 1
    if ur.held_keys['2']: block_pick = 2
    if ur.held_keys['3']: block_pick = 3
    if ur.held_keys['4']: block_pick = 4

class Voxel(ur.Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
                parent = ur.scene,
                position = position,
                model = 'assets/block',
                origin_y = 0.5,
                texture = texture,
                color = ur.color.color(0,0,random.uniform(0.9,1)), # color default is HSV format
                scale = 0.5)
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: texture = grass_texture
                if block_pick == 2: texture = stone_texture
                if block_pick == 3: texture = brick_texture
                if block_pick == 4: texture = dirt_texture
                # ur.mouse.normal is the surface where mouse is pointing at
                voxel = Voxel(
                            position = (self.position + ur.mouse.normal),
                            texture = texture)
            
            if key == 'right mouse down':
                ur.destroy(self)


for z in range(20):
    for x in range(20):
        voxel = Voxel( position = (x, 0, z) )
player = FirstPersonController()

app.run()