## Adding widgets

Let's start adding content to the GUI. We will refer to items you can add to a GUI (such as text, text boxes, buttons etc.) as **widgets**. There are a couple of rules to follow when adding a widget.

- If you want to use a new type of widget, you must import it. The first line of code in your program looks like this:

    ```python
    from guizero import App
    ```

    As an example, if you wanted to use the `Text` widget, you would add it to the import line, like this:

    ```python
    from guizero import App, Text
    ```

    We will ask you to import various types of widget throughout this guide. Each type of widget only needs to be added to the import list once, and then you can use it as many times as you want on your GUI.

- All code that creates a widget must be added before the **event loop**, which means between the line of code where you create the app, and the `app.display()` line of code:

    ![Event loop](images/event-loop.png)

    This is because the line of code `app.display()` starts the **event loop**. The GUI will be waiting for the user to do things such as click on a button - these are called **events**. It will constantly check whether anything new has happened and automatically update the display if necessary. The event loop **blocks** (rather like a `while True:` loop), so code written after the event loop will never execute.

    Throughout this guide, we will ask you to add widgets to the GUI, which means adding them anywhere between these two lines of code.


