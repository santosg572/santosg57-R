#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(850, 650)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)

ll = ['A medida que el número de ensayos aumenta,',
'esperaríamos que las frecuencias relativas',
'Nn(1)/n, ..., Nn(s)/n se establecieran en algunos',
' números fijos p1, p2, ..., ps',
'(que según nuestra intuición en este caso deberían ser todos 1/s).',
'Según la interpretación de frecuencia relativa, el número pi ',
'se denominaría la probabilidad de que se extraiga la i-ésima bola',
'cuando el experimento se realiza una vez (i=1,2, ..., s).']


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
    del1 = 40
    y0 = 500
    delx = 100
    x0=300
    n = len(ll)
    for i in range(n):
      Label(x0+delx, y0, ll[i])
      y0 = y0-del1

pyglet.app.run()

