## Getting started

--- task ---
Make sure you have [Python 3](https://www.python.org/downloads/){:target=blank} installed. Install the `guizero` library by typing a command into the terminal:

#### Windows / Mac OS
--- code ---
---
language: bash
line_numbers: false
---
pip3 install guizero
--- /code ---

#### Raspberry Pi
--- code ---
---
language: bash
line_numbers: false
---
sudo apt-get install python3-guizero
--- /code ---

--- /task ---

--- task ---
Open a new file in your favourite Python IDE, and save it as `gui_test.py`.
--- /task ---

--- task ---
Add a line of code at the top of your file to import the `App` class from the `guizero` module:

--- code ---
---
language: bash
line_numbers: false
---
from guizero import App
app = App(title="Hello world")
app.display()
--- /code ---

--- /task ---

--- task ---

Save and then run your file. You should see a GUI window that looks like this:

![A GUI with a title bar containing the text 'Hello world'. The rest of the window is blank.](images/first-app.png)

--- /task ---
