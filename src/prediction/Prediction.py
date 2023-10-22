from abc import ABC, abstractmethod


class Prediction(ABC):


  @abstractmethod
  def predict():
    """
    Function that calculates the rate of a item by a user, but it is implemented in the different subclasses since it is an abstract class.
    Returns:
    Result of prediction.
    """
    pass
