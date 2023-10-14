from math import sqrt
from utils import intersection_qualified_items
from abc import ABC, abstractmethod


class Metric(ABC):
  
  @abstractmethod
  def similutues():
    pass
  
  
  
  
  @staticmethod
  def euclidean_distance(matrix, u):
    resultados = dict()
    for v in range(len(matrix)):
      if v == u:
        continue
      else:
        intersection = intersection_qualified_items(matrix, u, v)
        result = 0
        for i in intersection:
          result += (matrix[u][i]  - matrix[v][i])**2
        resultados[f"Sim({u}, {v})"] = sqrt(result)
    return resultados


if __name__ == "__main__":
  pass