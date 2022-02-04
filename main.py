import ursina as ur

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
        pass

app = ur.Ursina()

for z in range(8):
    for x in range(8):
        voxel = Voxel( position = (x, 0, z) )

app.run()