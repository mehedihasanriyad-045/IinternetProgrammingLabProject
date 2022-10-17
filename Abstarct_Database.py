from abc import abstractmethod, ABC

# Abstract database class
class Abstract_Database(ABC): 

    @abstractmethod
    def __init__(self, config, debug=False):
        pass
    
    def log(self, text):
        if self.debug:
            print(text)

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def insert(self):
        pass 
    
    @abstractmethod
    def update(self):
        pass 
    
    @abstractmethod
    def select(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
