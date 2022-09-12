import abc


class FileReader(abc.ABC):

    def extract(self):
        print("Extracting content file...")
        self._open()
        self._read()
        self._close()

    @abc.abstractmethod
    def _open(self):
        pass

    @abc.abstractmethod
    def _read(self):
        pass

    @abc.abstractmethod
    def _close(self):
        pass
