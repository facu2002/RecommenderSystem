from utils import intersection_qualified_items


## similitudes se calcula en base a los vecinos que elige el usaurio (los x vecinos que mayor simulitud tenga (más cerca al 1))
def simple_prediction(matrix, u, similarities):
  numerador = 0
  denominador = sum([abs(similarities[f"Sim({u}, {v})"]) for v in range(1,3)])
  print("La suma de las similitudes es -> ", denominador)
  for v in range(3):
    if v == u:
      continue
    else:
      intersection = intersection_qualified_items(matrix, u, v)
      for i in intersection:
        numerador += similarities[f"Sim({u}, {v})"] * matrix[v][i]
        
  print("HOLA EZ%R ES ", numerador / denominador)
