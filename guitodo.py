import PySimpleGUI as sg

layout = [
    [sg.Listbox(["app","games","movies"], font=("Arial",16), size =(40,5))],
    [sg.InputText("", font=("Arial",16),size=(40,1), key = "list1")],
    [sg.Button("Ok"), sg.Button("Exit")]
]


window = sg.Window("First App", layout)
event, values = window.Read()


if event == "Exit":
    window.close()