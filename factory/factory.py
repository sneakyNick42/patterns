"""Factory pattern."""


class Dog:
    """Dog class."""
    def __init__(self, name) -> None:
        self._name = name

    @staticmethod
    def speak():
        """Speak."""
        return 'Woof!'


class Cat:
    """Cat class."""
    def __init__(self, name) -> None:
        self._name = name

    @staticmethod
    def speak():
        """Speak."""
        return 'Nya!'


class Human:
    """Human class."""
    def __init__(self, name) -> None:
        self._name = name

    @staticmethod
    def speak():
        """Speak."""
        return 'Hello world!'


def get_pet(pet='dog'):
    """Factory method."""
    pets = dict(
        dog=Dog(name='Lucky'),
        cat=Cat(name='Tom'),
        human=Human(name='Alex'),
    )
    return pets[pet]


if __name__ == '__main__':
    CAT = get_pet('cat')
    DOG = get_pet('dog')
    HUMAN = get_pet('human')

    print(CAT.speak())
    print(DOG.speak())
    print(HUMAN.speak())
