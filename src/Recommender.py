import heapq
from file_system import load_data


class Recommender:
  def __init__(self, file_name, num_neighbors, similarity_function):
    """
    Constructor of the Recommender class, responsible for creating instances of the class
    Args:
        self: argument that refers to the created instance of the class.
        file_name: name of the file from which the data is extracted.
        num_neighbors: number of neighbors selected by the user.
        similarity_function: similarity function selected by the user.
    Returns:
        Returns the created instance of the Recommender class.
    """
    # Se inicializan los valores necesarios y se normaliza la matriz
    self.lower, self.upper, self.unnormalized_matrix = load_data(file_name)
    self.matrix = self.normalize(self.unnormalized_matrix)
    self.num_neighbors = num_neighbors
    self.similarity_function = similarity_function
    self.prediction_queue = None



  def run(self, prediction_function):
    """
    Function responsible for filling the matrix with the predicted ratings.
    Args:
        self: argument that refers to the created instance of the class.
        prediction_function: prediction function selected by the user.
    Returns:
        Matrix with all values already calculated.
    """
    print("\n\nMatriz inicial  ###############################################################\n")        
    self.print_matrix(self.matrix)
    self.calculate_prediction_queue()

    iterator = 0
    while self.prediction_queue:
      self.coordinate_prediction = self.prediction_queue.pop(0)
      self.neighbors = self.get_neighbors(self.num_neighbors, self.similarity_function(self))
      if len(self.neighbors) == 0:
        self.prediction_queue.append(self.coordinate_prediction)
        continue
      result = prediction_function(self)
      self.matrix[self.coordinate_prediction[0]][self.coordinate_prediction[1]] = result
      print(f"\n\nMatriz en la iteración {iterator}  #####################################################\n")    
      self.print_matrix(self.matrix)
      print("\nLa posición que se acaba de predecir es", self.coordinate_prediction, " : ", result)
      print("\nLas similitudes son ", self.similarity_function(self))
      print("\nLos vecinos seleccionados son ", self.neighbors)
      iterator += 1
    self.unnormalized_matrix = self.denormalize(self.matrix)
    return self.matrix    



  def print_matrix(self, matrix, out_file="output.txt"):
    """
    Function responsible for filling the matrix with the predicted ratings.
    Args:
        self: argument that refers to the created instance of the class.
        matrix: matrix that you want to print.
        out_file: file in which you want the output, by default output.txt
    Returns:
        void
    """
    with open(out_file, "w") as file:
      aux = f"\nLa matriz de {len(matrix)} X {len(matrix[0])}\n"
      aux += f"El rango de los valores es {self.lower} - {self.upper}\n"
      print(aux, file=file)
      print(aux)
      if len(matrix) == 0:
        return
      for row in matrix:
        for element in row:
          if element == None:
            print(f"{'-':<6}", end=" ", file=file)
            print(f"{'-':<6}", end=" ")
          else:
            print(f"{element:<6.2f}", end=" ", file=file)
            print(f"{element:<6.2f}", end=" ")  
        print()
        print("", file=file)



  def mean_rows(self, matrix, user, intersecting_columns):
    """
    Function that is responsible for taking the arithmetic mean of a row.
    Args:
        self: argument that refers to the created instance of the class.
        matrix: matrix that you want to use.
        user: user of whom you want to know the arithmetic mean.
        intersecting_columns: matching columns for a real arithmetic mean.
    Returns:
        Arithmetic mean of the row.
    """
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[user][i]
      return sum / len(intersecting_columns)
    return 0



  def intersection_qualified_items(self, u, v):
    """
    Function that returns the intersection of qualified items between two users.
    Args:
        self: argument that refers to the created instance of the class.
        u: first user to analyze
        v: second user to analyze
    Returns:
        List of items rated by both users.
    """
    row = self.matrix[u]
    # buscamos los indices de los elementos no nulos
    return [ x for x in range(len(row)) if self.matrix[u][x] is not None and self.matrix[v][x] is not None]



  def get_neighbors(self, num_neighbor, similarity):
    """
    Function that returns the users that are most similar to the main user.
    Args:
        self: argument that refers to the created instance of the class.
        num_neighbor: number of users
        similarity: list of similarities of both users
    Returns:
        List of users that are most similar to the main user
    """
    # Ordena el diccionario por los valores de forma descendente
    ordered_similarity = sorted(similarity, key=lambda x: similarity[x], reverse=True)
    neighbors = dict()
    if num_neighbor == 0:
      return neighbors
    for x in ordered_similarity:
      if self.matrix[x[1]][self.coordinate_prediction[1]] != None:
        neighbors[x] = similarity[x]
        num_neighbor -= 1
      if num_neighbor <= 0:
        break
    return neighbors
  
  
  
  def calculate_priority(self, row):
    """
    Function that calculates the priority of a row that will be inserted in the queue 
    Args:
        self: argument that refers to the created instance of the class.
        row: row that it is analyzed
    Returns:
        Priority of a row based on the number of Nones
    """
    return sum(1 for elemento in row if elemento is None)



  def calculate_prediction_queue(self):
    """
    Function that fill the prediction_queue attribute with all the row priorities. 
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Void
    """
    # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
    priority_rows = [(self.calculate_priority(row), index) for index, row in enumerate(self.matrix)]
    # Convertir la lista en una cola de prioridad (heap)
    indices_none = []
    for row in sorted(priority_rows, key=lambda x: x[0]):
      indices_none += [(row[1],indice) for indice, valor in enumerate(self.matrix[row[1]]) if valor is None and not(all(row_matrix[indice] is None for row_matrix in self.matrix))
]
    self.prediction_queue = indices_none
    
    
    
  def normalize(self, matrix):
    """
    Function that given a matrix, normalizes its values.
    Args:
        self: argument that refers to the created instance of the class.
        matrix: matrix that you want to normalize
    Returns:
        Matrix with all normalized values
    """
    result = []
    for row_aux in matrix:
      row = []
      for i in range(len(row_aux)):
        if row_aux[i] != None:
          row.append((row_aux[i] - self.lower) / (self.upper - self.lower))
        else:
          row.append(None)
      result.append(row)
    return result
  
  
  
  def denormalize(self, matrix):
    """
    Function that given a normalized matrix, returns the original values.
    Args:
        self: argument that refers to the created instance of the class.
        matrix: matrix from which you want to obtain the original values
    Returns:
        Matrix with all orginal values
    """
    result = []
    for row_aux in matrix:
      row = []
      for i in range(len(row_aux)):
        if row_aux[i] != None:
          row.append((row_aux[i] * (self.upper - self.lower)) + self.lower)
        else:
          row.append(None)
      result.append(row)
    return result