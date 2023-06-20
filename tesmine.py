from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.enabled = False

grass_texture = load_texture('assets/grass_block.png')
dirt_texture = load_texture('assets/dirt_block.png')


app.run()