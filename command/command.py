"""Command pattern module."""
import random

FOOD = [
    'nutella', 'eggs', 'milk',
    'meat', 'cake', 'salad'
]


class Command:
    """Command class."""
    def execute(self):
        """Execute command."""


class Open(Command):
    """Open command class."""
    def execute(self):
        """
        Execute 'open a fridge' command.

        :return: None
        :rtype: None
        """
        print('Opening a fridge')


class Take(Command):
    """Take command class."""
    def execute(self) -> None:
        """
        Execute 'take food' command.

        :return: None
        :rtype: None
        """
        try:
            chosen_food = random.choice(FOOD)
            FOOD.remove(chosen_food)
            print('Taking {0}'.format(chosen_food))
        except IndexError:
            print('No food left')


class Close(Command):
    """Close command class."""
    def execute(self):
        """
        Execute 'close fridge' command.

        :return: None
        :rtype: None
        """
        print('Closing a fridge')


class Macro:
    """Macro class for adding and executing commands."""
    def __init__(self):
        """Initialize commands."""
        self.commands = []

    def add(self, command: Command) -> None:
        """
        Adding a command.

        :param command: Command
        :return: None
        :rtype: None
        """
        self.commands.append(command)

    def run(self) -> None:
        """
        Execute all commands.

        :return: None
        :rtype: None
        """
        for command in self.commands:
            command.execute()


if __name__ == '__main__':
    EAT = Macro()
    EAT.add(Open())
    EAT.add(Take())
    EAT.add(Close())
    EAT.run()
