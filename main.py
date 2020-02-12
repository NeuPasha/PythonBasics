import pyowm

owm=pyowm.OWM('54cf9848d3a8217371631ac69c8da3e5')

observation = owm.weather_at_place('Moscow,RU')
w = observation.get_weather()

print('Температура в Москве: '+str(w.get_temperature('celsius')['temp'])+'°C')
