import abc


class figure(abc.ABC):
    @abc.abstractmethod
    def square(self):
        pass

    @abc.abstractmethod
    def repr(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass
