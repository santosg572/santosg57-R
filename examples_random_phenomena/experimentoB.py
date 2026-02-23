#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(850, 650)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)

ll = ['Supongamos que repetimos el experimento anterior n veces',
'Sea Nn(k) el número de veces que se extrajo la bola etiquetada',
'como k durante estos n ensayos del experimento.',
'Supongamos que tuviéramos', 'digamos, s=3 bolas y n=20 ensayos',
'Un resultado tipico podría ser',
'1, 1, 3,2,1,2,2,3,2,3,3,2,1,2,3,3,1,3,2,2',
'En cuyo caso',
'N20(1) = 5,   N20(2) = 8,   y   N20(3) = 7',
'Las frecuencias relativas (i.e. Proporción de veces) de los',
'resultados 1, 2, y 3 son entonces:',
'N20(1)/20 = .25,   N20(2)/20 = .40,   y   N20(3)/20 = .35']


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

