#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600)

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
    Label(400,500, 'Una caja tiene s bolas')
    coli = (255,0,0)
    x0 = 100
    y0 = 300
    dx = 50
    for i in range(3):
      j=i+1
      let = str(j)
      Circulo(x0, y0, let, coli, 18)
      x0 = x0 + dx
    Label(x0, y0, '...')
    coli = (255,0,0)
    Circulo(x0+dx, y0, 'r', coli, 18)
    
    x0 = x0+3*dx
    coli = (0, 255,0)
    for i in range(3):
      j=i+1
      let = 'r+'+str(j)
      Circulo(x0, y0, let, coli, 16)
      x0 = x0 + dx
    Label(x0, y0, '...')
    Circulo(x0+dx, y0, 's', coli, 16)



pyglet.app.run()

