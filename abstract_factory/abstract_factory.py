"""Abstract factory pattern module."""
from factory.factory import speaker


class Dog:
    """Dog class."""
    @classmethod
    @speaker
    def speak(cls):
        """Speak."""
        return 'Woof!'

    def __str__(self):
        return 'Dog'


class DogFactory:
    """Dog factory class."""

    @staticmethod
    def get_pet() -> Dog:
        """Get pet."""
        return Dog()

    @staticmethod
    def get_food():
        """Get dog food."""
        return 'Dog food.'


class PetStore:
    """Pet store class."""

    def __init__(self, pet_factory) -> None:
        self._pet_factory = pet_factory

    def show_pet(self):
        """Show pet."""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print('Our pet is {0}.'.format(pet))
        pet.speak()
        print('It\'s food is {0}'.format(pet_food))


if __name__ == '__main__':
    FACTORY = DogFactory()
    PET_STORE = PetStore(FACTORY)
    PET_STORE.show_pet()
