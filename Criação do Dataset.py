#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ------------------- Função para criar o Dataset num Txt --------------------

import random

def generate_cities_dataset(num_cities=100, file_path="cities_data.txt"):
    cities = []

    for i in range(1, num_cities + 1):
        latitude = round(random.uniform(36.0, 70.0), 6) # Latitude da Europa
        longitude = round(random.uniform(-20.0, 40.0), 6) # Longitude da Europa
        cities.append([i, latitude, longitude])

    try:
        with open(file_path, 'w') as file:
            for city in cities:
                file.write(f"{city[0]} {city[1]} {city[2]}\n")
        print(f"Dados das cidades foram salvos em {file_path}")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

# ------------------------------ Criação do dataset --------------------------

generate_cities_dataset(num_cities=100, file_path="cities_data.txt")

