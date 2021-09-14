from abc import ABC
from client.IHM.session import Session

class AbstractMenu(ABC):
    session = Session()