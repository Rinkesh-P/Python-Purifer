# Python Purifier - Python Semantic Error Extension

## Project Management Tool
https://trello.com/b/D1Xp37O8/project-17 

<br>

## Set-up Instructions

### Extension Settings Set-up
1. Go to File -> Preferences -> Settings (Ctrl+) 
1. For User settings go the Extension dropdown and modify the Python Default Interpretor Path to the path python.exe is located on your local machine.
1. For Workspace settings go the Extension dropdown and modify the Python Default Interpretor Path to the path python.exe is located on your local machine.

### Install Virtual Enviroment

1. `python -m venv env` (for Windows)
1. `python -m pip install -e .` from root directory

### Activate Virtual Enviroment

1. `.env/Scripts/activate` (for Windows)

### Install Server Dependencies

1. `pip install pygls`
1. `pip install git+https://github.com/James-Ansley/qchecker@dev-0.0.0a4`

### Install Client Dependencies

Open terminal and execute following commands:

1. `npm install`
1. `cd client/ && npm install`

### Run Example

1. Open this directory in VS Code
1. Open debug view (`ctrl + shift + D`)
1. Select `Server + Client` and press `F5`

<br>

## Acknowledgemnts

### Projects:

The json-extension repository was a Python language server template we have based the Python-Purifier extension on, which has provided useful understanding of Languager Server Protocols and pygls implementation that we used as a point of reference.

https://github.com/openlawlibrary/pygls/tree/master/examples/json-extension 

### People: 

James Finnie-Ansley (Project Client)

Over the course of this project we have been in regular communication with James to ask for guidance whenever we had issues regarding our understanding of Python Language Servers (pygls).

