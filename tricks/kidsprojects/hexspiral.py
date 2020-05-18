import turtle as tur

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t = tur.Pen()
tur.bgcolor('black')
for x in range(90):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

