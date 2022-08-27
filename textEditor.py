import PySimpleGUI as sg
from pathlib import Path
sg.theme('graygraygray')

smileys = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]
menu_layout = [
    ['File', ['open','save','---','exit']],
    ['Tools', ['Word count']],
    ['Add', smileys]
]

smileys_event = smileys[1] + smileys[3] + smileys[5]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size = (40, 30), key='TextBox')]

]

window = sg.Window('pYText', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Word count':
        full_text = values['TextBox']
        clean_text = full_text.replace('\n',' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'words{word_count}\n characters {char_count}')
    if event in smileys_event:
        current_text = values['TextBox']
        new_text = current_text + ' ' +  event
        window['TextBox'].update(new_text)
    if event == 'open':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['TextBox'].update(file.read_text())
            window['-DOCNAME-'].update(file.name)
    if event == 'save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True)+ '.txt'
        file = Path(file_path)
        file.write_text(values['TextBox'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'exit':
        pass



window.close()