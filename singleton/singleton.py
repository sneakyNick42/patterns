"""Singleton pattern module."""


class Borg:
    """Borg class making class attributes global."""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    """Singleton class that shares all it attributes among it's instances."""

    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


if __name__ == '__main__':
    FIRST = Singleton(HTTP='Hyper Text Transfer Protocol')
    print(FIRST)

    SECOND = Singleton(SNMP='Simple Network Management Protocol')
    print(FIRST)
