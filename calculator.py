import PySimpleGUI as sg

def create_window(theme):
        sg.theme(theme)
        sg.set_options(font='Franklin 12', button_element_size = (6,3))
        button_size= (6,3)
        layout = [
            [sg.Text('',
                     font='Franklin 30',
                     justification= 'right',
                     expand_x=True,
                     pad=(10,20),
                     right_click_menu= theme_menu,
                     key='text'
                     )],
            [sg.Button('C' ,size=(14,3)),sg.Button('Enter', size=(14,3))],
            [sg.Button('7', size = button_size),sg.Button('8', size = button_size),sg.Button('9', size = button_size), sg.Button('*', size = button_size)],
        [sg.Button('4', size = button_size),sg.Button('5', size = button_size),sg.Button('6', size = button_size),sg.Button('/', size = button_size)  ],
        [sg.Button('1', size = button_size),sg.Button('2', size = button_size),sg.Button('3', size = button_size),sg.Button('-', size = button_size)],
            [sg.Button('0', size = (14,3)),sg.Button('.', size = button_size),sg.Button('+', size = button_size)]
        ]
        return sg.Window("Calculator", layout)

theme_menu = ['menu',['lightgraay1','dark','darkgray8', 'random']]
window = create_window("dark")

current_num = []
full_operation = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window= create_window(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['text'].update(num_string)
    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['text'].update('')
    if event == 'Enter':
        full_operation.append(''.join(current_num))
        window['text'].update(eval(''.join(full_operation)))
    if event == 'C':
        full_operation = []
        current_num = []
        window['text'].update('')

