import PySimpleGUI as myGUI


layout = [[myGUI.Text("TEST")], [myGUI.Button("EXIT")]]

window = myGUI.Window(title='uProc-ObjectDet', layout=layout, margins=(720, 460))

while True:
    event, values = window.read()

    if event == "EXIT" or event == myGUI.WIN_CLOSED:
        break

window.close()

