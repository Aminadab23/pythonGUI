import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
def update_image(original, blur, contrast, embos, contour, flipX, flipY):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if embos:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())
    if flipX:
        image = ImageOps.mirror(image)
    if flipY:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format='PNG')
    window['Image'].update(data = bio.getvalue())

image_path = sg.popup_get_file('Open', no_window=True)
control_col= sg.Column([
    [sg.Frame('Contrast',layout=[[sg.Slider(range=(0,10), orientation= 'h', key='Contrast')]])],
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='BLUR')]])],

    [sg.Checkbox('Emboss', key='EMBOSS'),sg.Checkbox('Contour', key='CONTOUR')],
    [sg.Checkbox('Flip x', key='FlipX'), sg.Checkbox('Flip y', key='FlipY')],

    [sg.Button('Save', key='SAVE')],

])
image_col = sg.Column([[sg.Image(image_path, key='Image')]])
layout = [
    [control_col,image_col],
]

window =sg.Window('Image Editor', layout)
original = Image.open(image_path)
while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break
    update_image(original, values['BLUR'], values['Contrast'], values['EMBOSS'], values['CONTOUR'],values['FlipX'],values['FlipY'])

    if event == 'SAVE':
        save_path = sg.popup_get_file('save',save_as=True, no_window=True) + '.png'
        image.save(save_path,'PNG')
window.close()