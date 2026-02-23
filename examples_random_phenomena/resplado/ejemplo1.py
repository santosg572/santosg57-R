#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import time
import pyglet
from pyglet import shapes
import numpy as np

tt = ['Se anota el número de la bola y esta se devuelve a la caja.',
'El resultado del experimento es el número',
'de la bola seleccionada.']

window = pyglet.window.Window(800, 600)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20
filename = 'experimento_01.png'
# color=(50, 225, 30)

def Label(x0=0, y0=0, let='', sizef=24):
  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=sizef,
    color=(255, 255, 255),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  label.draw()


def Circulo(x0=0, y0=0, let=''):
  circle = shapes.Circle(x0, y0, radio, color=(50, 225, 30), batch=batch)

  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(0, 0, 0),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  batch.draw()
  label.draw()

  
@window.event

def on_draw():
    window.clear()
    Label(150, 550, 'Experimento: ', 30)
#    Label(400,500, 'Una caja tiene s bolas', 24)
    x0 = 200
    y0 = 300
    dx = 50
    nc = 10
    x0 = np.random.uniform(low=100, high=700, size=nc)
    y0 = np.random.uniform(low=200, high=500, size=nc)

    for i in range(nc):
      j=i+1
      let = str(j)
      if j == 10:
        let='s'
      Circulo(x0[i], y0[i], let)
    
    x0 = 400 
    y0 = 150
    dy = 50
    for ss in tt:
      Label(x0, y0, ss)
      y0 = y0-dy
    color_buffer = pyglet.image.get_buffer_manager().get_color_buffer()
    color_buffer.save(filename)
    time.sleep(10)

pyglet.app.run()

