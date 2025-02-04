from nicegui import app, ui

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)

ui.run()
