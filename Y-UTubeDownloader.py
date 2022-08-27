import PySimpleGUI as sg
from pytube import YouTube

sg.theme('darkred1')

start_layout = [
    [sg.Input(key='Link'), sg.Button('Submit', key='Submit')]
]


info_tab=[
    [sg.Text('Title: '), sg.Text('', key='Title')],
    [sg.Text('Length: '), sg.Text('', key='Length')],
    [sg.Text('Views: '), sg.Text('', key='Views')],
    [sg.Text('Author: '), sg.Text('', key='Author')],
    [sg.Text('Description: '), sg.Multiline('', key='Description', size=(40,20), no_scrollbar=True, disabled= True )],
]
download_tab =[
    [sg.Frame('Best Quality', [[sg.Button('download', key='BEST'),
                                sg.Text('', key='BESTRES'), sg.Text('', key='BESTSIZE')]])],
    [sg.Frame('Low Quality', [[sg.Button('download', key='LOW'),
                                sg.Text('', key='LOWRES'), sg.Text('', key='LOWSIZE')]])],
    [sg.Frame('Audio', [[sg.Button('download', key='AUDIO'),
                                sg.Text('', key='AUDIOSIZE')]])],

    [sg.VPush()],
    [sg.Progress(100, size=(20,20), expand_x=True,  key='ProgressBar')]
]

layout =[
    [sg.TabGroup([[
        sg.Tab('info', info_tab),sg.Tab('download', download_tab)
    ]])]
]

window = sg.Window('Y-UTube', start_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        if values['Link'] != '':
            window.close()

            video_object = YouTube(values['Link'],on_progress_callback=progress_check, on_complete_callback= on_complete)

            window = sg.Window('Y-UTube', layout, finalize=True)
            window['Title'].update(video_object.title)
            window['Length'].update(f'{round(video_object.length/60,2)}minutes')
            window['Views'].update(video_object.views)
            window['Author'].update(video_object.author)
            window['Description'].update(video_object.description)

            #download
            window['BESTRES'].update(video_object.streams.get_highest_resolution())
            window['BESTSIZE'].update(f'{round(video_object.streams.get_highest_resolution().filesize/1048576,1)} MB')

            window['LOWRES'].update(video_object.streams.get_lowest_resolution())
            window['LOWSIZE'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576, 1)} MB')

            window['AUDIOSIZE'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576, 1)} MB')
    if event == 'BEST':
        video_object.streams.get_highest_resolution().download()
    if event == 'LOW':
        video_object.streams.get_lowest_resolution().download()
    if event == 'AUDIO':
        video_object.streams.get_audio_only().download()

window.close()