import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name", font=("Arial",16)), 
     sg.InputText("", font=("Arial",16), size=(40,1), key="name")],
    [sg.Button("ok")]
]

window = sg.Window("First App", layout)
event, values = window.Read()
if event == "ok":
    print(values["name"])
window.close()
"hello"

