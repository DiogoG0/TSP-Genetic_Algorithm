#!/usr/bin/env python
# coding: utf-8

# # ------------------- Função para criar o Dataset num Txt --------------------

# In[89]:


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


# # ------------------------------ Criação do dataset --------------------------

# In[90]:


generate_cities_dataset(num_cities=100, file_path="cities_data.txt")


# # --------------------------  Verificação do dataset ------------------------------- 

# In[91]:


def read_cities_dataset(file_path="cities_data.txt"):
    cities = []
    try:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                l_dataset= line.split()
                city_num = l_dataset[0]
                latitude = float( l_dataset[1])
                longitude = float( l_dataset[2])
                cities.append([city_num, latitude, longitude])
    except FileNotFoundError:
        print(f"Não foi possível encontrar o ficheiro {file_path}.")
    
    return cities


# # ------------ Ler e Listar Cidades ----------------

# In[92]:


cities_data = read_cities_dataset()
for city in cities_data:
    print(f"Nome: {city[0]}, Latitude: {city[1]}, Longitude: {city[2]}")


# In[93]:


import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Calculo das distâncias entre cidades
def calc_dist(cities):
    total_sum = 0
    n_total = len(cities) # Número total de cidades

    for i in range(n_total):
        cityA = cities[i]
        cityB = cities[(i + 1) % n_total] 

        # Calcular a distância euclidiana entre cityA e cityB
        d = math.sqrt((cityB[1] - cityA[1]) ** 2 + (cityB[2] - cityA[2]) ** 2)
        
        
        total_sum += d  # Adicionar a distância ao total

    return total_sum

# Seleção da População
def select_population(cities, size):
    population = []
    
    # Gerar população inicial
    for _ in range(size):
        shuffled_cities = random.sample(cities, len(cities))
        distance = calc_dist(shuffled_cities)
        route = [distance, shuffled_cities.copy()]
        population.append(route)
        
    # Encontrar a rota mais curta na população
    fittest = min(population, key=lambda x: x[0])

    return population, fittest

def genetic_algorithm(population, lenCities, tournament_select, mutation_rate, crossover_rate, target):
    gen_number = 0
    
    # Loop até atingir um número máximo de gerações (1000)
    for _ in range(1000):
        new_population = []
        
        # Selecionar os dois melhores indivíduos da população atual (elitismo)
        sorted_population = sorted(population)
        new_population.extend(sorted_population[:2])

        # Realização do crossover e da mutação para criar novos indivíduos
        while len(new_population) < len(population):
            
            # CROSSOVER
            parent_chromosome1 = sorted(random.choices(population, k=tournament_select))[0]
            parent_chromosome2 = sorted(random.choices(population, k=tournament_select))[0]

            if random.random() < crossover_rate:
                point = random.randint(0, lenCities - 1)
                child_chromosome1 = parent_chromosome1[1][:point] + [city for city in parent_chromosome2[1] if city not in parent_chromosome1[1][:point]]
                child_chromosome2 = parent_chromosome2[1][:point] + [city for city in parent_chromosome1[1] if city not in parent_chromosome2[1][:point]]
            else:
                child_chromosome1 = parent_chromosome1[1]
                child_chromosome2 = parent_chromosome2[1]

            # MUTATION
            if random.random() < mutation_rate:
                point1, point2 = random.sample(range(lenCities), 2)
                child_chromosome1[point1], child_chromosome1[point2] = child_chromosome1[point2], child_chromosome1[point1]
                point1, point2 = random.sample(range(lenCities), 2)
                child_chromosome2[point1], child_chromosome2[point2] = child_chromosome2[point2], child_chromosome2[point1]

            new_population.append([calc_dist(child_chromosome1), child_chromosome1])
            new_population.append([calc_dist(child_chromosome2), child_chromosome2])

        # Atualizar a população
        population = new_population

        # Atualizar o número de gerações
        gen_number += 1

        # Print do progresso a cada 10 gerações
        if gen_number % 10 == 0:
            print(f'\rGeração nº {gen_number}, {sorted(population)[0][0]}', end='', flush=True)         

        # Verificar se o critério de break foi atingido
        if sorted(population)[0][0] < target:
            break

    # Encontrar a melhor solução
    solucao_candidata = sorted(population)[0]

    return solucao_candidata, gen_number

# Mapa
def draw_map(cities, solucao_candidata):
    plt.figure(figsize=(10, 6))

    # Plot das cidades
    for city in cities:
        plt.plot(city[2], city[1], 'o', markersize=8, color='blue', alpha=0.7)
        plt.text(city[2], city[1], city[0], fontsize=8, ha='right', va='bottom')

    # Plot da rota ótima
    for i in range(len(solucao_candidata[1])):
        try:
            first = solucao_candidata[1][i]
            second = solucao_candidata[1][i + 1]
            plt.plot([first[2], second[2]], [first[1], second[1]], 'gray', linestyle='-', linewidth=1, alpha=0.7)
        except:
            continue

    first = solucao_candidata[1][0]
    second = solucao_candidata[1][-1]
    plt.plot([first[2], second[2]], [first[1], second[1]], 'gray', linestyle='-', linewidth=1, alpha=0.7)

    plt.title("Mapa das Cidades e Rota Ótima")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()

def print_route_info(solucao_candidata):
    print("\nRota Ótima:")
    for city in solucao_candidata[1]:
        print(city[0], end=" -> ")
    print(solucao_candidata[1][0][0]) 

def print_information(initial_distance, gen_number, first_fittest, solucao_candidata, target, cities):
    print("\n----------------------------------------------------------------")
    print("Distancia Inicial:", round(initial_distance, 2))
    print("Geração:", gen_number)
    print("Fit da distância antes do treino:", first_fittest[0])
    print("Fit da distância depois do treino:", solucao_candidata[0])
    print("Distância a atingir:", target)
    print("Distância Total entre as Cidades:", round(calc_dist(solucao_candidata[1]), 2))
    print("----------------------------------------------------------------\n")

    draw_map(cities, solucao_candidata)
    print_route_info(solucao_candidata)

def main():
    # Configuração
    population_size = 500
    tournament_select = 4
    mutation_rate = 0.05
    crossover_rate = 0.8
    target = 600.0
    
    random.seed(42)

    cities = read_cities_dataset()
    initial_distance = calc_dist(cities)
    first_population, first_fittest = select_population(cities, population_size)
    solucao_candidata, gen_number = genetic_algorithm(first_population, len(cities), tournament_select, mutation_rate, crossover_rate, target)
    
    print_information(initial_distance, gen_number, first_fittest, solucao_candidata, target, cities)
   
    
    


# # ------------- Iniciar Otimização -----------------

# In[94]:


main()


# In[ ]:




