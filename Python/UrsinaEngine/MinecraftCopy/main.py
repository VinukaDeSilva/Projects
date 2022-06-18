# imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random

# Main game function
app = Ursina()

# Customizing the window
window.borderless = False
window.exit_button.visible = False

# Exit using the escape key
def input(key):
    if key == 'q' or key == 'escape':
        quit()

# Textures for the blocks
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
glass_texture = load_texture('assets/Glass_block.png')

# Block pick (To select which block to use)
block_pick = 1

# Always updated
def update():
    # Switching between block types
    global block_pick
    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys['5']:
        block_pick = 5

# A custom class for a block
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9, 1)),
            scale = 0.5
        )

    # Placing block
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down' or key == 'enter':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                
            # Destroying blocks
            if key == 'right mouse down':
                destroy(self)

# The sky of the world
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 160,
            double_sided = True
        )

# Using perlin noise
noise = PerlinNoise (octaves=2,seed=random.randint(1,1000000))

# Using perlin noise as well as creating the world
for z in range(-50,50):
    for x in range(-50,50):
        y = noise([x * .02,z * .02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x,y,z))


player = FirstPersonController()
player.gravity = 0.5
sky = Sky()

app.run()
