import PySimpleGUI as pg
import download as dl
import os


# set theme
pg.theme("DarkBlue12")

# Create Layout
layout = [
  [pg.Text("Choisissez un fichier: ")], 
  [[pg.Input(key="-IN2-" ,change_submits=True, size=(34,5)), pg.FolderBrowse(key="-IN-")]],
  [pg.Text("Entrer Url de la vidéo")],
  [pg.InputText()],
  [pg.T("")], 
  [pg.Button("Télécharger"), pg.Button("Quitter")],
]
# Create Window
window = pg.Window('Converter Music',
                   no_titlebar=False,
                   border_depth=0,
                   grab_anywhere=True,
                   element_justification='c',
                   right_click_menu=pg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                   ).Layout(layout)
# Event Loop
while True:
  event, values = window.read()
  if event == "Quitter" or event == pg.WIN_CLOSED:
    break
  elif event == "Télécharger":
    try:
      dl.extract(values[0], values["-IN2-"])
    except:
      pg.Popup('URL Inconnu\n')
    else:
      pg.Popup('Téléchargé avec succès\n')
    print("Url: "+values[0]+" Folder: "+values["-IN2-"])
window.close()