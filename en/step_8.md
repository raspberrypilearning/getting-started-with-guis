## PushButton widget

You can use a `PushButton` widget to create a button. When the button is pushed, a function is called.

- **Above** the code which creates the GUI app, write a function which will be called when the button is pressed. It is a good idea to put all of your function code at the start of your program, immediately after the `import` line.

    ```python
    def say_my_name():
        welcome_message.value = my_name.value
    ```

    This function refers to the `Text` widget (`welcome_message`) and sets its `value` to what was typed into the `TextBox` widget (`my_name`).

    You can use the `value` property with many widgets to retrieve their current value or to set it to something new.

- Add the `PushButton` widget to your `import` statement.

- Add a `PushButton` to the GUI:

    ```python
    update_text = PushButton(app, command=say_my_name, text="Display my name")
    ```

    The first argument tells the `PushButton` that the `app` is its master. Then we use two keyword arguments: `command` tells the button which function to call when it is pressed, and `text` is the text which will be displayed on the button.

- Press <kbd>F5</kbd> to run your code. Type your name into the text box and then press the button. You should see your name displayed in large text at the top.

    ![Display my name](images/display-my-name.png)

--- collapse ---

---
title: My name didn't appear!
---
Make sure that you have defined the function `say_my_name` near the top of your program after the `import` statement, and that you've set the `PushButton` `command` argument to call that function.

```python
from guizero import App, Text, TextBox, PushButton

def say_my_name():
    welcome_message.value = my_name.value

app = App(title="Hello world")

welcome_message = Text(app, text="Welcome to my app", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=say_my_name, text="Display my name")

app.display()
```

--- /collapse ---

The `PushButton` widget is a good example of how the event loop works: the GUI waits for an event (in this case, you clicking on the button), and it calls a function in response to the event. This function may contain code to change something on the GUI, and if it does, the display is updated accordingly.
