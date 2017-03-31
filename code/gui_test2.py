from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_booking():
    print( film_choice.get() )
    print( vip_seat.get_value() )
    print( row_choice.get() )
    info("Booking", "Thank you for booking")



app = App(title="My second GUI app", width=300, height=200, layout="grid")

film_description = Text(app, text="Which film?", grid=[0,0], align="left")
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")

seat_type = Text(app, text="Seat type", grid=[1,0], align="left")
vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")

seat_location = Text(app, text="Seat location", grid=[2,0], align="left")
row_choice = ButtonGroup(app, options=[ ["Front", "F"],
                                        ["Middle", "M"],
                                        ["Back", "B"]
                                      ], selected="M", horizontal=True, grid=[2,1], align="left")

book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[3,1], align="left")


app.display()
