import PySimpleGUI as sg
from utils import get_meaning, get_antonyms, get_synonyms

sg.theme('DarkBlue9')

greeting = "Hi. I am word bot. I can help you with words.\n\n"

layout = [
    [sg.Multiline(greeting, font=("Arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key="meaning",disabled=True),
     sg.Button("Synonyms", font=("Arial", 14), key='synonyms',disabled=True),
     sg.Button("Antonyms", font=("Arial", 14), key='antonyms',disabled=True),
     sg.Button("Clear", font=("Arial", 14), key='clear')
    ]
]

def check_enable():
    if values["input"].strip() != '':
        window.FindElement('meaning').Update(disabled=False)
        window.FindElement('synonyms').Update(disabled=False)
        window.FindElement('antonyms').Update(disabled=False)

def display_meaning(word):
    meaning = get_meaning(word)
    window['output'].print("WORD : " + word)
    if meaning:
        window['output'].print("MEANING : ", meaning,"\n")
    else:
        display_error("Word is not found in corpus")

def display_synonyms(word):
    synonyms = get_synonyms(word)
    window['output'].print("WORD : " + word,)
    if synonyms:
        window['output'].print("SYNONYMS : ", synonyms,"\n")
    else:
        display_error("Word is not found")

def display_antonyms(word):
    antonyms = get_antonyms(word)
    window['output'].print("WORD : " + word)
    if antonyms:
        window['output'].print("ANTONYMS : ", antonyms,"\n")
    else:
        display_error("Unable to find antonym of "+word)

def display_error(message):
    window['output'].print("Error : " +message, text_color='red')

if __name__ == '__main__':
    window = sg.Window('words', layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        else:
            check_enable()
        if event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonyms':
            display_synonyms(values['input'])
        elif event == 'antonyms':
            display_antonyms(values['input'])
        elif event == 'clear':
            window.FindElement('output').Update(greeting)

    window.Close()