import PySimpleGUI as sg
import cv2

layout = [
    [sg.Text('text label')]
]

window = sg.Window('object detection app', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


window.close()
