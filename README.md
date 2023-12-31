# Python Purifier - Python Code Style Defect Extension

## Project Management Tool
https://trello.com/b/D1Xp37O8/project-17 

<br>

## Project Description
This project is a VS Code extension for Python that highlights code smells and anti-patterns in students’ code. This extenstion aims to provide suggestions of good coding practices when it detects semantically incorrect blocks of code. This is done by using our client, James' qChecker library. At a high-level, this project consists of a VS Code extension code base, that communicates with the Python Language Server using pygls which is an implementation of the Language Server Protocol.

<br>

## Technologies
- **Python (3.10 or higher)**: this was the language that we used the most, as this extension is made for Python code, and the qChecker is a Python library. Ensure to use Python version 3.10 or higher as qChecker cannot work otherwise.
- **qchecker (latest)**: This is the Python library that makes the semantic check on student code - provided and created by our client, James.
- **pygls (latest)**: This is an implementation of the Language Server Protocol that we used to implement Python Purifier.
-  **JSON**: This was used to make modification to the configuration of our Python Purifier extension (for example, defining what qChecker checks to make.)


## Set-up Instructions

### Install Virtual Enviroment

 `python -m venv .env` (for Windows) <br>
 `python3 -m venv .env` (for macOS/Unix)

### Extension Settings Set-up
1. Go to File -> Preferences -> Settings (Ctrl+) 
1. For User settings go the Extension dropdown and modify the Python Default Interpreter Path to the path python.exe is located on your local machine.
1. For Workspace settings go the Extension dropdown and modify the Python Default Interpreter Path to the path python.exe is located on your local machine.

### Activate Virtual Enviroment

 `.env/Scripts/activate` (for Windows) <br>
 `source .env/bin/activate` (for macOS/Unix)

### Install Server Dependencies

1. `pip install pygls`
1. `pip install qchecker`

### Install Client Dependencies

Open terminal and execute following commands:

1. `npm install`
1. `cd client`
1. `npm install`

### Run Example

1. Open this directory in VS Code
1. Open debug view (`ctrl + shift + D`)
1. Select `Server + Client` and press `F5`

<br>

## Future Plans
- Publish Python Purifier to VS Code Extension Marketplace.
- Improve implementation of overlapping code style defects on one line.
- Keep up with changes made to qChecker.
- Python Purifier is designed to make all code style defect checks available in qChecker. All we will need to do is to  update qChecker to latest version and add new code style defect checks to the package.json file so that they appear in the extension configuration page.  

<br>

## Acknowledgements

### Projects:

The json-extension repository was a Python language server template we have based the Python-Purifier extension on, which has provided useful understanding of Language Server Protocols and pygls implementation that we used as a point of reference.

https://github.com/openlawlibrary/pygls/tree/master/examples/json-extension 

### People: 

James Finnie-Ansley (Project Client)

Over the course of this project we have been in regular communication with James to ask for guidance whenever we had issues regarding our understanding of Python Language Servers (pygls).

