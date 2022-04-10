from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Planet Encuclopedia")
root.geometry("500x500")
root.configure(background="light blue")

label_planet = Label(root, text="Planet : ", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"), bg="lightblue")
label_planet_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2,releif=SOLID)
label_planet_gravity_radius = Label(root,font=("casteller"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wraplength=500)

def PlanetInfo():
    print("hi")

btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

planets = ["Mercury","Venus", "Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvarable=selectedval)

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Mercury":
    label_planet_name['text'] = "Mercury"
    label_planet_image['image'] = "Mercury"
    label_planet_gravity_radius['text'] = "3.7 m/s² \n Radius : 2,439.7 km"
    label_planet_info['text'] = "Mercury is the smallest planet in our solar system. It's just a little bigger than earths moon"
    elif planet == "Mercury":
        label_planet_name['text'] = "Venus"
    label_planet_image['image'] = "Venus"
    label_planet_gravity_radius['text'] = "8.87 m/s² \n Radius : 6,051.8 km"
    label_planet_info['text'] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning and evning sky"
    elif planet == "Mercury":
        label_planet_name['text'] = "Earth"
    label_planet_image['image'] = "Earth"
    label_planet_gravity_radius['text'] = "9.807 m/s² \n Radius : 6,371.8 km"
    label_planet_info['text'] = "Earth is the only place in the knownm universe confirmed to host life and it's the only one for sure to have liquid water on it's surface"
    dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)

    btn = Button(root text="Show Planet Info" , command=PlanetInfo)
    btn.place(relx=0.5, rely=0.18, anchor=CENTER)

    label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
    label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
    label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
    label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
    label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()