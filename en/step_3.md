## Adding widgets

Let's start adding content to the GUI. We refer to items you can add to a GUI (such as text, text boxes, buttons, etc.) as **widgets**. There are a couple of rules to follow when adding a widget.

- If you want to use a new type of widget, you must import it. The first line of code in your program looks like this:

    ```python
    from guizero import App
    ```

    As an example, if you wanted to use the `Text` widget, you would add it to the `import` statement, like this:

    ```python
    from guizero import App, Text
    ```

    We will ask you to import various types of widgets while you work through this project. Each type of widget only needs to be added to the `import` statement once, and then you can use it as many times as you want on your GUI.

- All code that creates a widget must be added above the **event loop**, meaning above the `app.display()` line of code, and below the line of code where you create the app:

    ![Event loop](images/event-loop.png)

    Throughout this guide, whenever we ask you to add widgets to the GUI, you should add them anywhere between these two lines of code.
    
    This is because the line of code `app.display()` starts the event loop. Once it is executed, the GUI will be waiting for the user to do things such as click a button – these user actions are called **events**. The GUI app will constantly check whether the user has done anything new, and it will automatically update the display if necessary. The event loop **blocks**, so code written after the event loop will never execute. So this loop acts rather like a `while True:` loop, which is an infinite loop you may have used before when writing a Python script.
