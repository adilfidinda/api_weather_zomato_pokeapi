import requests
key = "1df8035c8905ef360fe7bd9ecee6ec2e"
host = "api.openweathermap.org"
unit = "metric"
language = "id"


while True :
    try :
        print("Prakiraan Cuaca")
        kota = input("Masukkan nama kota : ")
        url = f"https://{host}/data/2.5/weather?q={kota.lower()}&appid={key}&units={unit}&lang={language}"
        data = requests.get(url)
        cuaca = data.json()
        temp_kelvin = cuaca['main']['temp']
        keadaan_cuaca = cuaca['weather'][0]['description']
        longitude = cuaca['coord']['lon']
        latitude = cuaca['coord']['lat']
        humidity = cuaca['main']['humidity']
        kec_angin = cuaca['wind']['speed']

        print(f'Suhu : {round(temp_kelvin)} Celcius')
        print(f'Keadaan cuaca : {keadaan_cuaca.title()}')
        print(f'Longitude : {longitude}, Latitude : {latitude}')
        print(f'Humidity level : {humidity}%')
        print(f'Kecepatan angin : {kec_angin} meter/sec')
        break
    except :
        print("Kota yang anda masukkan tidak terdaftar\n")
        continue
