import PySimpleGUI as sg
import cv2
import numpy as np
import os
import fnmatch
from ultralytics import YOLO
def createMenus():
    training_results_menu = [[], ['F1', 'Labels', 'Results', 'Confusion Matrix', 'P Curve', 'PR Curve', 'R Curve']]
    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEME LISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]
    layout = [
        [sg.Image(filename='', key='-IMAGE-'), sg.Listbox(values=fnmatch.filter(os.listdir("testPictures/"), '*.jpg'), size=(50, 20), key="-imageLoader-",  enable_events=True)],
        [sg.Radio('Live Detection', "radioBTNS", default=False, size=(10, 10), k='-cam-'),
        sg.Radio('Image Detection', "radioBTNS", default=True, size=(20, 10), k='-img-')],
        [sg.ButtonMenu('Training Results', training_results_menu, key='-tres-')],
    ]

    window = sg.Window("Object Detection by Gherman Ovidiu", layout , location=(600,200))

    frame = np.zeros(shape=[480, 680, 3])
    model_path = os.path.join('runs', 'detect', 'train8', 'weights', 'best.pt')
    model = YOLO(model_path)
    camera = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-imageLoader-' and  values['-img-'] == True:
            framePath = os.path.join(".", "testPictures",values['-imageLoader-'][0])
            jpgFrame = cv2.imread(framePath)       

            results = model(jpgFrame)
            jpgFrame = results[0].plot()

            frame = cv2.cvtColor(jpgFrame, cv2.COLOR_BGR2BGRA)
            frame = cv2.resize(frame, (680, 480))
        elif values['-cam-'] == True:
            if camera is None or not camera.isOpened():
                values['-cam-'] = False
                values['-img-'] = True
                window['-cam-'].update(value=False)
                window['-img-'].update(value=True)
            else:
                succes, camFrame = camera.read()
                if succes:
                    results = model(camFrame)
                    jpgFrame = results[0].plot()

                frame = cv2.cvtColor(jpgFrame, cv2.COLOR_BGR2BGRA)
        elif event == '-tres-' and values['-tres-'] == 'F1':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'F1_curve.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("F1",image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'Labels':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'labels.jpg')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.cvtColor(tempFrame, cv2.COLOR_BGR2BGRA)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("Labels", image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'Confusion Matrix':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'confusion_matrix.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("Confusion Matrix", image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'P Curve':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'P_curve.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("P Curve", image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'PR Curve':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'PR_curve.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("PR Curve", image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'R Curve':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'R_curve.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("R Curve", image=tempFrameBytes, keep_on_top=True)
        elif event == '-tres-' and values['-tres-'] == 'Results':
            tempPath = os.path.join('.', 'runs', 'detect', 'train8', 'Results.png')
            tempFrame = cv2.imread(tempPath)
            tempFrame = cv2.resize(tempFrame, (1280, 960))
            tempFrameBytes = cv2.imencode('.png', tempFrame)[1].tobytes()
            sg.popup("Results", image=tempFrameBytes, keep_on_top=True)
        framebytes = cv2.imencode('.png', frame)[1].tobytes()
        window['-IMAGE-'].update(data=framebytes)
    window.close()
