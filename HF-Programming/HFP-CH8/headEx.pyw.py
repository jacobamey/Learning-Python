from tkinter import *

app = Tk()
app.title('Head-Ex deliveries')

Label(app, text="Depot:").pack()
depot = Entry(app)
depot.pack()

Label(app, text="Description:").pack()
description = Entry(app)

Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save", command=save_data).pack()
app.mainloop()
