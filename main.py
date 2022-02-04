import ursina as ur

class Voxel(ur.Button):
    def __init__(self):
        super().__init__(
                parent = ur.scene,
                position = (0,0,0),
                model = 'cube',
                origin_y = 0.5,
                texture = 'white_cube',
                color = ur.color.white,
                highlight_color = ur.color.lime)
        pass

app = ur.Ursina()
voxel = Voxel()
app.run()