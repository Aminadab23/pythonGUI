import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key='IMAGE')],
    [sg.Text('People in picture', key='Text', expand_x=True, justification='c')]
]

window = sg.Window('Face Detection', layout)
video = cv2.VideoCapture(0)

#face_cascade =

while True:
    event, values = window.read(timeout= 0)
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['IMAGE'].update(data = imgbytes)


window.close()