from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z'] * 2
letters += [letter.lower() for letter in letters]  
state = {'mark': None}
hide = [True] * 64
won = False
tap_count = 0  

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  
    tap_count += 1  # Incrementa el contador de taps

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    ##Identifica que hayan tapeado todas las tiles
    global won
    if all(not hidden for hidden in hide):
        won = True

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y - 1) ##Modificar coordenadas para que el center funcione
        color('black')
<<<<<<< HEAD
        write(tiles[mark], align= "center", font=('Arial', 30, 'normal')) ##Agregar center

    ##Verifica que todas las tiles se hayan tapeado, así aparece un mensaje de ganar
    if won == True:
=======
        write(letters[mark], align="center", font=('Arial', 30, 'normal'))

    if won:
>>>>>>> 29cf8620967b1912ac9e9e3ff3b1848ba279329d
        up()
        goto(0, 100)
        color('green')
        write("You Won!!", align="center", font=('Arial', 40, 'normal'))

    up()
    goto(-170, 220)
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
