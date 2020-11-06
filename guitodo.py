import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name", font=("Arial",16))],
    [sg.Button("ok")]
]

window = sg.Window("First App", layout)
event, values = window.Read()
window.close()

