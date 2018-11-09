# python_proj.py

import pyowm
import json
import time
#import requests
import smtplib
from email.mime.text import MIMEText

# passing my API key to PyOWM
owm = pyowm.OWM("922a8d576caddedeb0eb87ca2b38602f")
location = "Portland, OR, USA"
report = owm.weather_at_place(location)
w = report.get_weather()

# # Weather details

w2 = w.to_JSON()
weather_info = json.loads(w2)

# This is an example JSON file from the get_weather command
# weather_info =  {"reference_time": 1541530560, "sunset_time": 1541551775, "sunrise_time": 1541516310, "clouds": 1, "rain": {}, "snow": {}, "wind": {"speed": 1.5}, "humidity": 79, "pressure": {"press": 1026, "sea_level": ""}, "temperature": {"temp": 283.2, "temp_kf": "", "temp_max": 284.85, "temp_min": 282.05}, "status": "Mist", "detailed_status": "mist", "weather_code": 701, "weather_icon_name": "50d", "visibility_distance": 16093, "dewpoint": "", "humidex": "", "heat_index": ""}

# setting key variables from dictionary
time_report = weather_info["reference_time"]
time_rise = weather_info["sunrise_time"]
time_set = weather_info["sunset_time"]

# converting unix epoch time to human readable format
time_report = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time_report))
time_rise = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time_rise))
time_set = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time_set))

# instead of getting the defaul kelving readings and convering to fahrenheit, specific temp info is gathered here
# Example: {'temp': 55.58, 'temp_max': 57.92, 'temp_min': 53.96, 'temp_kf': None}
temp_info = w.get_temperature("fahrenheit")
temperature = temp_info["temp"]
temp_high = temp_info["temp_max"]
temp_low = temp_info["temp_min"]

current_weather = weather_info["detailed_status"]
current_weather.capitalize()
humidity = weather_info["humidity"]

winds = w.get_wind()
wind_speed = winds["speed"]
wind_direction = int(winds["deg"])
if wind_direction in range(0,30) or wind_direction in range(330, 360):
    wind_direction = "out of the south"
elif wind_direction in range(30, 60):
    wind_direction = "out of the southwest"
elif wind_direction in range(60, 120):
    wind_direction = "out of the west"
elif wind_direction in range(120, 150):
    wind_direction = "out of the northwest"
elif wind_direction in range(150, 210):
    wind_direction = "out of the north"
elif wind_direction in range(210, 240):
    wind_direction = "out of the northeast"
elif wind_direction in range(240, 300):
    wind_direction = "out of the east"
elif wind_direction in range(300, 330):
    wind_direction = "out of the southeast"

## I stole this from Google's API walkthrough
## def create_message(sender, to, subject, message_text):
##     message = MIMEText(message_text)
##     message['to'] = to
##     message['from'] = sender
##     message['subject'] = subject
##     return {'raw': base64.urlsafe_b64encode(message.as_string())}

## setting up parameters for create_message
## sender = "me"
## to = "9187346020@vtext.com"
## subject = "Weather"

message_string1 = f"Weather for {location}\n{time_report}\n{current_weather}\nCurrent Temp: {temperature}F\nLow: {temp_low} High: {temp_high}"
message_string2 = f"Humidity: {humidity}%\nWinds: {wind_speed}mph {wind_direction}\nSunrise: {time_rise}\nSunset: {time_set}"

# message_to_send = create_message(sender, to, subject, message_string)

##I stole this from Google's API developer guide
## def send_message(service, user_id, message):
 
##   try:
##     message = (service.users().messages().send(userId=user_id, body=message).execute())
##     print('Message Id: %s') % message['id']
##     return message
##   except errors.HttpError as error:
##     print('An error occurred: %s') % error

## send_message(service, user_id, message_to_send)


## this mailgun api message
## def send_simple_message():
##     return requests.post(
##         "https://api.mailgun.net/v3/sandbox26572ae867e141539882237b8515e913.mailgun.org/messages",
##         auth=("api", "pubkey-4a82d58c7ca81c19ffc966139c6f6036"),
##         data={"from": "Mailgun Sandbox <postmaster@sandbox26572ae867e141539882237b8515e913.mailgun.org>",
##               "to": "Scott Harvey <9187346020@vtext.com>",
##               "subject": "Hello Scott Harvey",
##               "text": message_string})

## send = send_simple_message()


# formatting simple messages for smtplib 
msg1 = MIMEText(message_string1)
msg1['Subject'] = "Weather"
msg1['From'] = "scottharvey@gmail.com"
msg1['To'] = "scottharvey@gmail.com"

msg2 = MIMEText(message_string2)
msg2['Subject'] = "Weather"
msg2['From'] = "scottharvey@gmail.com"
msg2['To'] = "scottharvey@gmail.com"

session = smtplib.SMTP('smtp.mailgun.org', 587)
session.login('postmaster@sandbox26572ae867e141539882237b8515e913.mailgun.org','b5c86266cdc1aa820b43e61c48129835-4412457b-3ca88440')
session.sendmail(msg1['From'], msg1['To'], msg1.as_string())
session.quit()

session = smtplib.SMTP('smtp.mailgun.org', 587)
session.login('postmaster@sandbox26572ae867e141539882237b8515e913.mailgun.org', 'b5c86266cdc1aa820b43e61c48129835-4412457b-3ca88440')
session.sendmail(msg2['From'], msg2['To'], msg2.as_string())
session.quit()
