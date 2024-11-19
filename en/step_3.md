## Adding widgets

You can add text, text boxes, buttons and other features to a GUI. These are called **widgets**. 

Each time you add add a widget, follow these two rules:

--- task ---

Add the widget to the list at the start of your program. This program imports two widgets: `App` and `Text`.

--- code ---
---
language: python
line_numbers: true
---
from guizero import App, Text
--- /code ---

Each type of widget only needs to be added to the list once, and then you can use it as many times as you want on your GUI.

--- /task ---

--- task ---
All code to add widgets should go between the line of code which creates the `App`, and the line of code which displays it. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
from guizero import App
app = App(title="Hello world")

# All widget code should go here

app.display()
--- /code ---

--- /task ---

