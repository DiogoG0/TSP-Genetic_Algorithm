# TSP-Genetic_Algorithm
An implementation of the Traveling Salesman Problem solver using a Genetic Algorithm in Python.

Desafio - TSP - Genetic Algorithm

## 1 

TSP - Genetic Algorithm - Notebook.ipynb

##
## 2 

Num Algoritmo Genético, a forma como representamos o cromossoma é crucial para o desempenho do algoritmo. No Traveling Salesman Problem (TSP), o cromossoma indica a ordem das cidades visitadas e é representado como uma lista no código. Esta representação possui as seguintes vantagens:

- Simplicidade: A lista é fácil de entender, sendo que cada posição corresponde a uma cidade na rota.
- Facilidade de Implementação: Em Python, acessar ou manipular listas é eficiente, logo simplifica o processo de modificar as posições das cidades.
  
Quanto às operações de reprodução:

#### Mutação:
A mutação introduz pequenas mudanças aleatórias nos cromossomas para explorar novas soluções. No código, isso é feito escolhendo aleatoriamente um par de posições e trocando as cidades nelas. 

- Código:
if random.random() < mutation_rate:
  point1, point2 = random.sample(range(lenCities), 2)
  child_chromosome1[point1], child_chromosome1[point2] = child_chromosome1[point2], child_chromosome1[point1]
  point1, point2 = random.sample(range(lenCities), 2)
  child_chromosome2[point1], child_chromosome2[point2] = child_chromosome2[point2], child_chromosome2[point1]

#### Crossover (Cruzamento):
O crossover combina informações de dois cromossomas "pais" para criar "filhos". No código, os "pais" são escolhidos aleatoriamente com recurso a torneios e uma parte de um "pai" é trocada com o outro para gerar dois descendentes.

- Código:
if random.random() < crossover_rate:
  point = random.randint(0, lenCities - 1)
  child_chromosome1 = parent_chromosome1[1][:point] + [city for city in parent_chromosome2[1] if city not in parent_chromosome1[1][:point]]
  child_chromosome2 = parent_chromosome2[1][:point] + [city for city in parent_chromosome1[1] if city not in parent_chromosome2[1][:point]]
##
## 3 

#### Preferência pela solução com a maior distância

Quando modificamos o algoritmo para sempre preferir a solução com a maior distância durante as operações de mutação e crossover, observámos impactos significativos no comportamento e desempenho do Algoritmo Genético para o Traveling Salesman Problem.

##
Soluções Subótimas:

Ao escolher a solução com a maior distância, notamos uma tendência à preservação de soluções subótimas ao longo das gerações. O algoritmo favorece soluções com distâncias elevadas, dificultando a superação de mínimos locais e a descoberta de soluções mais eficientes.

##
Exploração Limitada do Espaço:

A escolha da solução com maior distância restringe a exploração do espaço de procura. 
O algoritmo tem menos probabilidade de encontrar soluções inovadoras, concentrando-se em regiões associadas a distâncias mais longas.

##
Convergência Prematura:
A falta de aleatoriedade na escolha de soluções para atualização contribui para uma convergência prematura do algoritmo. Isso demonstra que o algoritmo pode ficar preso em soluções subótimas, ou seja, torna-se ineficaz na procura de soluções mais otimizadas.
