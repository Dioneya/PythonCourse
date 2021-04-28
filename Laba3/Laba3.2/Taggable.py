from abc import ABCMeta, abstractmethod

class Taggable(object):
    @abstractmethod
    def tag(self):
        pass