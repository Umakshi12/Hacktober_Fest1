# This is the registration form made by using python.

import PySimpleGUI as sg
import pandas as pd

sg.theme('BlueMono')

Excel_File='registration.xlsx'
df = pd.read_excel(Excel_File)

layout = [
    [sg.Text('Please fill out this form for registration:')],
    [sg.Text('Name', size=(15,1)),sg.InputText(key='Name')],
    [sg.Text('City',size=(15,1)), sg.InputText(key='City')],
    [sg.Text('Roll no.',size=(15,1)), sg.InputText(key='Roll no.')],
    [sg.Text('School',size=(15,1)),sg.InputText(key='School')],
    [sg.Submit(),sg.Button('Clear'),sg.Exit()]

]

window = sg.Window('Simple data entry form',layout)

def clear():
    for key in values:
        window[key]('')
    return None


while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear()

    if event == 'Submit':
        df = df.append(values,ignore_index=True)
        df.to_excel(Excel_File, index=False)
        sg.popup('Data saved!')
        clear()
window.close()
