import heapq

# Tu matriz
matriz = [
    [1, 2, 3, None],
    [2, None, 9, 8],
    [None, None, None, 5],
    [None, None, None, 53],
    [None, 2, None, 5],
    [2, 3, 4, 5]
]

# Función para calcular la prioridad de una fila (cantidad de elementos no nulos)
def calcular_prioridad(fila):
  return sum(1 for elemento in fila if elemento is None)

# Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
filas_con_prioridad = [(calcular_prioridad(fila), index) for index, fila in enumerate(matriz)]

# Convertir la lista en una cola de prioridad (heap)
heapq.heapify(filas_con_prioridad)

# Obtener las filas ordenadas por prioridad
while filas_con_prioridad:
  prioridad, fila = heapq.heappop(filas_con_prioridad)
  print(f"Fila con prioridad {prioridad}: {fila}")





############

a = [[1,2,43, None, 4, None],
     []
     [1,2, None, None, 4, 3],
     ]

print(a.index(None))