from utils import intersection_qualified_items


def simple_prediction(matrix, u, similarities):
  numerador = 0
  for v in range(matrix[0][0]):
    if v == u:
      continue
    else:
      intersection = intersection_qualified_items(matrix, u, v)
      for i in intersection:
        numerador += similarities[f"Sim({u},{v})"] * matrix[1][(v,i)]
