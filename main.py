import random
import ursina as ur
from ursina.prefabs.first_person_controller import FirstPersonController

app = ur.Ursina()

grass_texture = ur.load_texture('assets/grass_block.png')
stone_texture = ur.load_texture('assets/stone_block.png')
brick_texture = ur.load_texture('assets/brick_block.png')
dirt_texture = ur.load_texture('assets/dirt_block.png')
sky_texture = ur.load_texture('assets/skybox.png')
arm_texture = ur.load_texture('assets/arm_texture.png')
punch_sound = ur.Audio('assets/punch_sound', loop=False, autoplay=False)

ur.window.fps_counter.enabled = False
ur.window.exit_button.visible = False

block_pick = 1


def update():
    # this function gets called every frame
    global block_pick

    if ur.held_keys['1']:
        block_pick = 1
    if ur.held_keys['2']:
        block_pick = 2
    if ur.held_keys['3']:
        block_pick = 3
    if ur.held_keys['4']:
        block_pick = 4

    if ur.held_keys['left mouse'] or ur.held_keys['right mouse']:
        hand.active_state()
    else:
        hand.passive_state()


class Voxel(ur.Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=ur.scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            # color default is HSV format
            color=ur.color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    texture = grass_texture
                if block_pick == 2:
                    texture = stone_texture
                if block_pick == 3:
                    texture = brick_texture
                if block_pick == 4:
                    texture = dirt_texture
                # ur.mouse.normal is the surface where mouse is pointing at
                voxel = Voxel(
                    position=(self.position + ur.mouse.normal),
                    texture=texture)
                punch_sound.play()

            if key == 'right mouse down':
                ur.destroy(self)
                punch_sound.play()


class Sky(ur.Entity):
    def __init__(self):
        super().__init__(
            parent=ur.scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )


class Hand(ur.Entity):
    def __init__(self):
        super().__init__(
            parent=ur.camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=ur.Vec3(150, -10, 0),
            position=ur.Vec2(0.4, -0.6)
        )

    def active_state(self):
        self.position = ur.Vec2(0.3, -0.5)

    def passive_state(self):
        self.position = ur.Vec2(0.4, -0.6)


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
