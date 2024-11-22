## TextBox 

A TextBox widget allows the user to type in data.

--- task ---

Start a new file. Add `TextBox` to the list of widgets at the start of your program.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from guizero import App, TextBox
--- /code ---

--- /task ---

--- task ---

Create a `TextBox` widget

--- code ---
---
language: python
line_numbers: false
---
app = App(title="Text box")
my_name = TextBox(app)
app.display()
--- /code ---

--- /task ---

--- task ---

Run your code. You should see a small text box appear. 

![TextBox widget](images/text-box.png)

--- /task ---








