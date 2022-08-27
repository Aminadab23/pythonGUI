import PySimpleGUI as sg
from time import time
def convet_pos_to_pixel(cell):
    tl = cell[0] * cell_size, apple_pos[1] * cell_size
    br = tl[0] + cell_size, tl[1] + cell_size

    return tl, br
FIWLD_SIZE = 400

Cell_num = 10
cell_size = FIWLD_SIZE/Cell_num
# the snack body

snake_body = [(4,4),(3,4),(2,4)]
Directions = {'left':(-1,0), 'right':(1,0),'up':(0,1), 'down':(0,-1)}
direction = Directions['up']
#apple
apple_pos= (0,0)


sg.theme('Green')

field = sg.Graph(
    canvas_size=(FIWLD_SIZE,FIWLD_SIZE),
    graph_bottom_left=(0,0),
    graph_top_right=(FIWLD_SIZE,FIWLD_SIZE),
    background_color='blaCK'

)

layout = [
    [field]
]

window = sg.Window('PySnake', layout, return_keyboard_events=True)
start_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Left:37':
        direction = Directions['left']

    if event == 'Right:39':
        direction = Directions['right']
    if event == 'Up:38':
        direction = Directions['up']
    if event == 'Down:40':
        direction = Directions['down']
    time_since_start = time()- start_time

    if time_since_start>= 0.5:
        start_time= time()
        #snake update
        new_head = (snake_body[0][0]+direction[0], snake_body[0][1]+ direction[1])
        snake_body.insert(0,new_head)
        snake_body.pop()


    tl, br = convet_pos_to_pixel(apple_pos)
    field.DrawRectangle(tl,br, 'red')

    field.DrawRectangle((0,0), (FIWLD_SIZE,FIWLD_SIZE), 'black')
    #draw snake
    for index,part in enumerate(snake_body):
        tl,br = convet_pos_to_pixel(part)
        color = 'yellow' if index == 0 else 'green'
        field.DrawRectangle(tl,br,color)

window.close()