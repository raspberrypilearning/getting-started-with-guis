## Slider widget

A **slider** lets users move within a range of values easily, rather like moving a volume control up or down.

- Before the code which creates the GUI app, write a function which will be called when the slider is moved.

    ```python
    def change_text_size(slider_value):
        welcome_message.font_size(slider_value)
    ```

    This function has a parameter called `slider_value`. When the slider is moved, the current value of the slider will **automatically be sent to the function**, so we must give it a name. We have chosen to call this parameter `slider_value`. The code inside the function sets the `font_size` of the `welcome_message` to the current slider value.

- Add the `Slider` widget to your import statement.

- Add a `Slider` to the GUI:

    ```python
    text_size = Slider(app, command=change_text_size, start=10, end=80)
    ```

    The `command` is the function that will be called when the slider is moved (i.e. the function we just created). `start` and `end` values are specified for the largest and smallest values the slider can have. We have specified these so that the font does not get too large or small - the smallest it can be is 10pt and the largest is 80pt.

- Save your code and press F5 to run it. Move the slider from side to side and watch the size of the text change.

    ![Using a slider](images/slider-display.png)


