from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
	result = requests.get(url.format(city, api_key))
	if result:
		json = result.json()
		city = json['name']
		country = json['sys']['country']
		temp_kelvin = json['main']['temp']
		temp_cels = temp_kelvin - 273.15
		temp_fah = (temp_cels * (9/5)) + 32
		weather = json['weather'][0]['description']
		icon = json['weather'][0]['icon']
		final = [city, country, temp_cels, temp_fah, icon, weather]
		return final
	else:
		return None


def search():
	city = city_text.get()
	weather = get_weather(city)
	if weather:
		global label
		location_label['text'] = '{}, {}'.format(weather[0], weather[1])
		logo = PhotoImage(file="C://Users//akash//Desktop//weather app//icon//{}@2x.png".format(weather[4]))
		label = Label(image=logo)
		label.image = logo
		label.pack()
		temp_label['text'] = '{:.2f} degree Celsius, {:.2f} degree Fahrenheit'.format(weather[2], weather[3])
		weather_label['text'] = weather[5]
		search_btn['state'] = DISABLED
	else:
		messagebox.showerror('Error', 'Cannot find city')

def delete_info():
	location_label['text'] = ''
	temp_label['text'] = ''
	weather_label['text'] = ''
	label.forget()
	search_btn['state'] = NORMAL

app = Tk()


app.title("Weather App")
app.geometry("700x350")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack() 


search_btn = Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

delete_info_btn = Button(app, text="Delete info", command= delete_info)
delete_info_btn.pack()

location_label = Label(app, text='', font=('bold', 20))
location_label.pack()

temp_label = Label(app, text='')
temp_label.pack()

weather_label = Label(app, text='')
weather_label.pack()


app.mainloop()