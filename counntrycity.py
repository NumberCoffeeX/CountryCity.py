from tkinter import *
import random

window = Tk()
window.title("Countrys and Capitals v2")
window.geometry("600x600")
window.configure(bg = "Lightblue")


enter_country = Entry(window)
enter_country.place(relx= 0.5,rely = 0.2, anchor = CENTER)

enter_city = Entry(window)
enter_city.place(relx= 0.5,rely = 0.3, anchor = CENTER)

country_list = Label(window)
random_number_label = Label(window)
random_number_label.configure(bg = "Lightblue")
random_number_label.place(relx= 0.5,rely = 0.9, anchor = CENTER)
random_number_label2 = Label(window)
random_number_label2.configure(bg = "Lightblue")
random_number_label2.place(relx= 0.5,rely = 0.9, anchor = CENTER)
random_country = Label(window)
city_list = Label(window)
city_list.configure(bg = "Lightblue")
random_city = Label(window)

list1 = []
list2 = []
def addfriend():
    country = enter_country.get()
    list1.append(country)
    country_list["text"] = "Country Name : " + str(list1)
    city = enter_city.get()
    list2.append(city)
    city_list["text"] = "City Name : " + str(list2)
def random_number():
    length = len(list1)
    length2 = len(list2)
    random_no = random.randint(0, length-1)
    random_no2 = random.randint(0, length2-1)
    random_number_label["text"] = str(random_no)
    random_number_label2["text"] = str(random_no2)
    generated_random_number = list1[random_no]
    generated_random_number2 = list2[random_no2]
    random_country["text"] = "Random Country : " + str(generated_random_number)
    random_city["text"] = "Random City : " +str(generated_random_number2)

btn = Button(window, text="Display Country and City Name", command = addfriend)
btn.place(relx= 0.5,rely = 0.1, anchor = CENTER )
btn.configure(bg = "Lightblue")

country_list.place(relx= 0.5,rely = 0.4, anchor = CENTER)
city_list.place(relx=0.5,rely = 0.5, anchor = CENTER)
country_list.configure(bg = "Lightblue")

btn1 = Button(window, text="Display Country and City Randomly" , command = random_number)
btn1.place(relx= 0.5,rely = 0.6, anchor = CENTER)
btn1.configure(bg = "Lightblue")

random_number_label.place(relx= 0.5,rely = 0.7, anchor = CENTER)
random_country.place(relx= 0.5,rely = 0.8, anchor = CENTER)
random_country.configure(bg = "Lightblue")

random_number_label2.place(relx= 0.5,rely = 0.9, anchor = CENTER)
random_city.place(relx= 0.5,rely = 0.95, anchor = CENTER)
random_city.configure(bg = "Lightblue")

window.mainloop()
