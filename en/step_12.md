## A new app

- Create a new file and save it as `gui_test2.py`.

- Add a line of code at the start of your file to import the App class from the guizero library:

    ```python
    from guizero import App
    ```

- Now add two more lines of code to create an `App` and then display it on the screen:

    ```python
    app = App(title="My second GUI app", width=300, height=200, layout="grid")
    app.display()
    ```

    This time we have specified some new keyword arguments: `width` and `height` change the size of the app window and `layout` allows us to set out our widgets on an invisible grid.

