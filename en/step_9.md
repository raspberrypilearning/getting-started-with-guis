## Combo 

The combo widget allows you to select an option from a drop-down menu.


--- task ---

Start a new file. Add `Combo` to the list of widgets at the start of your program.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from guizero import App, Combo
--- /code ---

--- /task ---


--- task ---
Create the `App` and add a `Combo` widget.

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
---
app = App(title="Movie chooser")
film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"])
app.display()
--- /code ---

--- /task ---

--- task ---

Save and run your code. You should see a drop down box with three options. 

![A GUI window with a drop down box containing the options Star Wars, Frozen and Lion King](images/combo.png)

--- /task ---




