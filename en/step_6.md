## PushButton widget

You can use a `PushButton` widget to create a button, and write code so that when the button is pushed, a function is called.

To keep your script nice and tidy, it is a good idea to put all the code which defines functions at the top of your program, immediately below the `import` line.

- **Above** the code which creates the GUI app, write a function called `say_my_name`:

    ```python
    def say_my_name():
        welcome_message.value = my_name.value
    ```
    
    So this `say_my_name` function refers to the `Text` widget that you've written earlier `welcome_message`. It will set the `value` of `welcome_message` to what was typed into your `TextBox` widget (`my_name`).
    
    You can use the **`value` property** with many widgets to retrieve their current value or to set it to something new.

- Add `PushButton` to your `import` statement.

- Add a `PushButton` widget to the GUI:

    ```python
    update_text = PushButton(app, command=say_my_name, text="Display my name")
    ```

    The first argument tells the `PushButton` that the `app` is its boss. Then we use two keyword arguments: `command` tells the button which function to call when it is pressed, and `text` is the text which will be displayed on the button.

- Press <kbd>F5</kbd> to run your code. Type your name into the text box and then press the button. You should see your name displayed in large text at the top.

    ![Display my name](images/display-my-name.png)

--- hints ---

--- hint ---

- Define a function `say_my_name` near the top of your program below the `import` statement.

- Tell the `command` argument of the `PushButton` to call this function.

--- /hint ---

--- hint ---

This is what your code should look like:

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

--- /hint ---

--- /hints ---



The `PushButton` widget is a good example of how the event loop works: the GUI waits for an event (in this case, you clicking the button), and it calls a function in response to the event. The function may contain code to change something on the GUI, and if it does, the display is updated accordingly.
