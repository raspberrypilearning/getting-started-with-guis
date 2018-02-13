## Review 

You have now learnt how to use simple GUI widgets. This is the full code for this first part:

```python
from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello world")

welcome_message = Text(app, text="Welcome to my app", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="cat.gif")

app.display()
```

You can also download a complete working example [here](resources/gui_test.py).

Next we'll make a simple GUI for booking cinema tickets to look at some a little more complicated GUI widgets: combo menus, check boxes, and radio buttons.
