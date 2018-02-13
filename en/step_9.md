## Slider widget

A slider lets users pick a value from a range of values easily, since it works rather like moving a volume control slider.

- Above the code which creates the GUI app, write a function `change_text_size`.

    ```python
    def change_text_size(slider_value):
        welcome_message.size = slider_value
    ```

    This function will be called whenever the slider is moved, which is why it takes a parameter called `slider_value`. We must add a parameter inside the brackets so that when the slider is moved, its current value will **automatically** be sent to the function.
    
    The code inside the function uses the current slider value to set the `size` of the `welcome_message`.

- Add `Slider` to your `import` statement.

- Add a `Slider` widget to the GUI:

    ```python
    text_size = Slider(app, command=change_text_size, start=10, end=80)
    ```

    The `command` argument specifies the function that will be called when the slider is moved — the `change_text_size` function we just created.
    
    The values of the `start` and `end` arguments determine the largest and smallest values of the slider. Since we are using it to change text size, we have specified these so that the font does not get too large or small — the smallest it can be is 10pt and the largest is 80pt.

- Save your code and press <kbd>F5</kbd> to run it. Move the slider from side to side and watch the size of the `welcome_message` change.

    ![Using a slider](images/slider-display.png)


