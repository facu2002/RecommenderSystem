from abc import ABC, abstractmethod


class Metric(ABC):

  
  @abstractmethod
  def similarity():
    """
    Function that calculates the similarity between two users, but it is implemented in the different subclasses since it is an abstract class.
    Returns:
    Result of similarity.
    """
    pass

