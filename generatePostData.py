import requests
import random
import time
from datetime import datetime

# Definindo os limites mínimos e máximos
min_values = {
    "direction": 0.00322,
    "temperature": 4.8848,
    "rh": 19.1,
    "pressure": 979.03436,
    "precip": 0,
    "prmsl": 998.9226,
    "tmpsrf": 6.2068,
    "vel_gfs": 0,
    "vel_twr": 0
}
max_values = {
    "direction": 359.87616,
    "temperature": 35.22632,
    "rh": 99.6,
    "pressure": 1024.0297,
    "precip": 17.0625,
    "prmsl": 1034.6104,
    "tmpsrf": 38.54001,
    "vel_gfs": 10.109407,
    "vel_twr": 5.776
}

def generate_weather_data(previous_data=None):
    generated_data = {}

    # Gerando valores dentro dos limites especificados com pequena variação
    for key in min_values.keys():
        min_value = min_values[key]
        max_value = max_values[key]

        if previous_data and key in previous_data:
            previous_value = previous_data[key]
            min_value = max(min_value, previous_value - 1)
            max_value = min(max_value, previous_value + 1)

        generated_data[key] = random.uniform(min_value, max_value)

    # Adicionando datetime fixo
    generated_data["datetime"] = datetime.now().isoformat()
    # Adicionando code fixo
    generated_data["code"] = "CR5103"

    return generated_data

def post_weather_data(data):
    url = "http://2rpnetenergia.pythonanywhere.com/api/weather/"
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("Weather data successfully posted.")
        else:
            print(f"Failed to post weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while posting weather data: {e}")

# Inicialização com um registro aleatório
previous_data = generate_weather_data()

# Loop para fazer o POST a cada segundo
while True:
    # Gerar dados meteorológicos com base nos dados anteriores
    weather_data = generate_weather_data(previous_data)
    print("Generated weather data:", weather_data)
    
    # Enviar dados meteorológicos via POST
    post_weather_data(weather_data)

    # Atualizar os dados anteriores com os dados atuais
    previous_data = weather_data

    # Aguardar 1 segundo antes de fazer a próxima solicitação
    time.sleep(1)
