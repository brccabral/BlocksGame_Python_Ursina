import ursina as ur
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(ur.Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
                parent = ur.scene,
                position = position,
                model = 'cube',
                origin_y = 0.5,
                texture = 'white_cube',
                color = ur.color.white,
                highlight_color = ur.color.lime)
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # ur.mouse.normal is the surface where mouse is pointing at
                voxel = Voxel(position= (self.position + ur.mouse.normal))
            
            if key == 'right mouse down':
                ur.destroy(self)

app = ur.Ursina()

for z in range(8):
    for x in range(8):
        voxel = Voxel( position = (x, 0, z) )
player = FirstPersonController()

app.run()