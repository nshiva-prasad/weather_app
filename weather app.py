import tkinter as tk
import requests

def show():

	# Enter your API key here
	api_key = "insert_api_key_here"

	# base_url variable to store url
	base_url = "http://api.openweathermap.org/data/2.5/weather?"


	# Give city name
	city_name = clicked.get()

	if city_name == "select city":
		Output.config( text = "Please Select city ")
	else:
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response =  requests.get(complete_url)
		x = response.json()

		# Now x contains list of nested dictionaries
		# Check the value of "cod" key is equal to
		# "404", means city is found otherwise,
		# city is not found
		if x["cod"] != "404":

			# store the value of "main"
			# key in variable y
			y = x["main"]

			# store the value corresponding
			# to the "temp" key of y
			current_temperature = y["temp"]-273.15

			# store the value corresponding
			# to the "pressure" key of y
			current_pressure = y["pressure"]

			# store the value corresponding
			# to the "humidity" key of y
			current_humidity = y["humidity"]

			# store the value of "weather"
			# key in variable z
			z = x["weather"]
			weather_description = z[0]["description"]

			# print following values
			t = (" Temperature (in Celsius unit) = " +
							str(current_temperature) +
				"\n atmospheric pressure (in hPa unit) = " +
							str(current_pressure) +
				"\n humidity (in percentage) = " +
							str(current_humidity) +
				"\n description = " +
							str(weather_description))
			Output.config( text = t)

		else:
			print(" City Not Found ")
			Output.config( text = " City Not Found ")


app =tk.Tk() # Defining the main app
app.title("Weather")
app.geometry("800x400+50+50")

# Dropdown menu options
options = [
	"Hyderabad",
	"Leh",
	"Delhi",
	"Mumbai",
	"Chennai",
	"Kolkata",
	"Varanasi",
	"Bhopal",
	"Jaipur"
    ]

# datatype of menu text
clicked = tk.StringVar()


# initial menu text
clicked.set( "select city" )

# Create Dropdown menu
drop = tk.OptionMenu( app , clicked , *options ).pack()

# Create button, it will change label text
button = tk.Button( app , text = "Get Info" , bg="yellow", fg="blue",font=("arial",10,"bold"), command = show )
button.place(x=550,y=120,height=40,width=100)


OutputLabel=tk.Label(text="Output:",font=("arial",15,"bold")).place(x=290,y=220,height=20,width=200) #Creating output label
Output = tk.Label(app,text = "") #displaying the output
Output.config(bg="white",fg="black",font=("arial",10,"bold"))
Output.place(x=350,y=250,height=100,width=400)


app.mainloop()