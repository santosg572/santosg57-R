#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import numpy as np
import pyglet
from pyglet import shapes

window = pyglet.window.Window(850, 650)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)

def Label(x0=0, y0=0, let=''):
  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(255, 255, 255),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  label.draw()


def Circulo(x0=0, y0=0, let='', coli=(0,0,0), sizef=24):
#  print(coli)
  circle = shapes.Circle(x0, y0, radio, color=coli, batch=batch)

  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=sizef,
    color=(0, 0, 0),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  batch.draw()
  label.draw()

  
@window.event

def on_draw():
    window.clear()
    Label(400,550, 'Una caja tiene s bolas')
    coli = (255,0,0)
    x0 = 100
    y0 = 300
    nc = 13
    x0 = np.random.uniform(low=150, high=700, size=nc)
    y0 = np.random.uniform(low=200, high=500, size=nc)

    dx = 50
    for i in range(4):
      j=i+1
      let = str(j)
      Circulo(x0[i], y0[i], let, coli, 18)
    Circulo(x0[i+1], y0[i+1], 'r', coli, 18)
    k = i+2
    coli = (0, 255,0)
    for i in range(7):
      j=i+1
      let = 'r+'+str(j)
      Circulo(x0[i+k], y0[i+k], let, coli, 16)
    Circulo(x0[i+1], y0[i+1], 's', coli, 16)

    color_buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        # Save to file
    color_buffer.save('circulos_rojos_verdes_aleatorios.png')



pyglet.app.run()

