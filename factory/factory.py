"""Factory pattern module."""


def speaker(func):
    """Speaker decorator."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{0} says \'{1}\''.format(args[0].__name__, result))

    return wrapper


class Dog:
    """Dog class."""
    def __init__(self, name) -> None:
        self._name = name

    @classmethod
    @speaker
    def speak(cls):
        """Speak."""
        return 'Woof!'


class Cat:
    """Cat class."""
    def __init__(self, name) -> None:
        self._name = name

    @classmethod
    @speaker
    def speak(cls):
        """Speak."""
        return 'Nya!'


class Bender:
    """Bender class."""
    def __init__(self, name) -> None:
        self._name = name

    @classmethod
    @speaker
    def speak(cls):
        """Speak."""
        return 'Kill all humans!'


def get_pet(pet='dog'):
    """Factory method."""
    pets = dict(
        dog=Dog(name='Lucky'),
        cat=Cat(name='Tom'),
        human=Bender(name='Alex'),
    )
    return pets[pet]


if __name__ == '__main__':
    CAT = get_pet('cat')
    DOG = get_pet('dog')
    BENDER = get_pet('human')

    CAT.speak()
    DOG.speak()
    BENDER.speak()
