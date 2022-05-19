# Python Language Server 

## Install Server Dependencies

1. `python -m venv env`
2. `.env/Scripts/activate`
3. `pip install pygls`
4. `pip install git+https://github.com/James-Ansley/qchecker@dev-0.0.0a4` (will change)
5. Create `.vscode/settings.json` file and set `python.pythonPath` -->  `{"python.defaultInterpreterPath": " ${workspaceFolder}/.env/Scripts/python.exe"}`

1. Create `.vscode/settings.json` file and set `python.pythonPath` to point to your python environment where `pygls` is installed

## Install Client Dependencies

Open terminal and execute following commands:

1. `npm install`
2. `cd client/ && npm install`

## Run Example

1. Open this directory in VS Code
2. Open debug view (`ctrl + shift + D`)
3. Select `Server + Client` and press `F5`
