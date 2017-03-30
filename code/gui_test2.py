from guizero import App, Combo, Text, CheckBox, ButtonGroup

app = App(title="My second GUI app", layout="grid")

film_description = Text(app, text="Film:", grid=[0,0])
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1])

vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1])

row_choice = ButtonGroup(app, options=[ ["Front", 1],
                                        ["Middle", 2],
                                        ["Back", 3]
                                      ], selected=2, grid=[2,1])


app.display()
