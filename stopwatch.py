import PySimpleGUI as sg
from time import time

def create_window():
        sg.theme('black')
        layout = [
            [sg.Push(),sg.Image('close.png',enable_events=True, key='close', size= (30,30),pad=0)],
            [sg.VPush()],
            [sg.Text('time', font='Young 50', key='-time-')],
            [sg.Button('Start', button_color=('#fff','#f00'), border_width= 0 , key='-STARTSTOP-' ),
             sg.Button('Lap',border_width= 0,button_color=('#fff','#f00') , key='-LAP-', visible=False)],
            [sg.Column([[]], key='-LAPS-')],
            [sg.VPush()]
        ]
        return sg.Window("Stopwatch",
                   layout,
                   size= (300,300),
                   no_titlebar=True,
                   element_justification= 'center'
                   )

window = create_window()
start_tome = 0
active = False
while True:
    event, values =  window.read(timeout = 10)
    if event in [sg.WIN_CLOSED, 'close']:
        break
    if event == "-STARTSTOP-":
        if active:
           active = False
           window['-STARTSTOP-'].update('Reset')
           window['-LAP-'].update(visible=False)
        else:
            if start_tome > 0:
                window.close()
                window = create_window()
                start_tome = 0
            else:
                start_tome = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)

    if active:
        elapse_time = round(time()- start_tome,1)
        window['-time-'].update(elapse_time)
    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'],[[sg.Text('1'),sg.VSeparator, sg.Text('time')]])