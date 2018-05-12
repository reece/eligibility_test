from abc import ABC, abstractmethod


class EligibilityBase(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def config(self):
        pass

    @abstractmethod
    def validate(self, inp_json):
        pass

    @abstractmethod
    def check_eligibility(self, inp):
        pass
