## Slider widget

A slider lets users pick a value from a range of values easily. It works rather like moving a volume control slider.

This example will let you change the font size using a slider.


--- task ---

Add `Slider` to the list of widgets at the start of your program.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from guizero import App, Text, Slider
--- /code ---

--- /task ---

--- task ---

Write a function called `change_text_size`. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 4
---
def change_text_size(slider_value):
    sample_text.size = slider_value
--- /code ---

--- /task ---

--- task ---
Underneath the function, create the `App` and add a `Text`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
---
app = App(title="Text size")
sample_text = Text(app, text="Some example text")
app.display()
--- /code ---

--- /task ---

--- task ---

Create a `Slider` widget. When the slider is moved, the `change_text_size` function will be called, and given the current value of the slider.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 10-14
---
text_size = Slider(
    app, 
    command=change_text_size, 
    start=10, 
    end=80
)
app.display()
--- /code ---

--- /task ---

--- task ---

Save and run your code. You should see a joke, and when you press the button, the punch line is displayed. 

![GUI with text 'Some example text' and a slider from 10 to 80](images/slider-display.png)

--- /task ---



