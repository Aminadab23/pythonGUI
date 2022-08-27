import PySimpleGUI as sg
layout = [[sg.Input(key='inp'),sg.Spin(["KM - mile", "KG- Pounds", "Sec - min"], key='units'), sg.Button('Convert', key="conv")],[sg.Text('output', key='result')]]
window = sg.Window("Converter app", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'conv':
        input_value =values['inp']
        if input_value.isnumeric():
            val = float(input_value)
            match values['units']:
                case 'KM - mile':
                    window['result'].update((round(val * 0.6214,2)))
                case 'KG- Pounds':
                    window['result'].update(round(val * 2.20462,2))
                case 'Sec - min':
                   window['result'].update(round((val/60), 3))
        else:
            window['result'].update('Please enter a number')
window.close()