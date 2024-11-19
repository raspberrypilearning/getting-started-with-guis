## Getting started

--- task ---
Make sure you have [Python 3](https://www.python.org/downloads/){:target="_blank"}installed. Install the `guizero` library by typing a command into the terminal:

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
Add this code to your file. This will allow you to check that everything is set up correctly.

--- code ---
---
language: python
line_numbers: false
---
from guizero import App
app = App(title="Hello world")
app.display()
--- /code ---

--- /task ---

--- task ---

Save and then run the file. You should see a GUI window that looks like this:

![A GUI with a title bar containing the text 'Hello world'. The rest of the window is blank.](images/first-app.png)

Your window will look different depending on whether you are using Windows, Mac OS or Linux.

--- /task ---
