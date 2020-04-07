"""Mediator pattern module."""
from abc import ABC, abstractmethod
from typing import List


class PlainPilot(ABC):
    """Main plain class."""
    def __init__(self, plain_dispatcher: 'Dispatcher', plain_id: int) -> None:
        self._dispatcher = plain_dispatcher
        self._id = plain_id

    @property
    def id(self) -> int:
        """Pilot id."""
        return self._id

    @abstractmethod
    def send(self, msg):
        """Send message to other pilots."""

    @abstractmethod
    def receive(self, msg):
        """Receive message from other pilots."""


class Pilot(PlainPilot):
    """Plain class."""

    def send(self, msg) -> None:
        print('Pilot {0} send: {1}'.format(self.id, msg))
        self._dispatcher.distribute(self, msg)

    def receive(self, msg) -> None:
        print('Pilot {0} receives: {1}'.format(self.id, msg))


class Dispatcher:
    """Dispatcher class."""

    def __init__(self) -> None:
        self._pilots: List[Pilot] = []

    def add(self, pilot) -> None:
        """Adding pilots to list for further message distribution."""
        self._pilots.append(pilot)

    def distribute(self, sender, msg) -> None:
        """Distributing message among pilots."""
        for pilot in self._pilots:
            if pilot.id != sender.id:
                pilot.receive(msg)


if __name__ == '__main__':
    DISPATCHER = Dispatcher()

    PILOT_ONE = Pilot(DISPATCHER, 1)
    PILOT_TWO = Pilot(DISPATCHER, 2)
    PILOT_THREE = Pilot(DISPATCHER, 3)

    DISPATCHER.add(PILOT_ONE)
    DISPATCHER.add(PILOT_TWO)
    DISPATCHER.add(PILOT_THREE)

    PILOT_ONE.send("Let's race, guys!")
    PILOT_TWO.send('No way!')
    PILOT_THREE.send("I'm in!")
