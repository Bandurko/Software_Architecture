from abc import ABC, abstractmethod
from ast import List

from model_store import PoligonalModel, Flash, Camera, Scene

class IModelChangeObserver(ABC):
   @abstractmethod
   def apply_update_model(self) -> None:
      pass 
   
class IModelChanger(ABC):
   @abstractmethod
   def notify_change(self, sender) -> None:
      pass

class ModelStore(IModelChanger):
   def __init__(self, changeObservers: List[IModelChangeObserver]) -> None:
      self.models: List[PoligonalModel] = [PoligonalModel([])]
      self.scenes: list[Scene] = [Scene(self.models, self.flashes, self.cameras)]
      self.flashes: list[Flash] = [Flash()]
      self.cameras: list[Camera] = [Camera()]
      self.changeObservers = changeObservers

   def get_scene(self, id):
      for scene in self.scenes:
         if scene.id == id:
            return scene
      return None
   
   def notify_change(self, sender) -> None:
      return super().notify_change(sender)
    