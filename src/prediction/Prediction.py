from abc import ABC, abstractmethod


class Prediction(ABC):
  neighbors = dict()
  matrix = []
  u = None
  
  @abstractmethod
  def predict():
    pass
