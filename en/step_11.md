## Review 

You have now learnt how to use some simple GUI widgets. The full code for this part of the guide can be found [here](resources/gui_test.py) if you want to see a full working example.

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

Now let's look at some more complicated GUI widgets: combo boxes, check boxes, radio buttons and the menu bar. We will make a simple cinema booking GUI to demonstrate these widgets.

