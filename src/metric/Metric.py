from abc import ABC, abstractmethod


class Metric(ABC):
  matrix = []
  u = None
  
  @abstractmethod
  def similarity(matrix, u):
    pass

  @staticmethod
  def mean_rows(matrix, u, intersecting_columns):
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[u][i]
      return sum / len(intersecting_columns)
    return 0
  