"""Abstract factory pattern."""
from factory.factory import speaker


class Dog:
    """Dog class."""
    @speaker
    def speak(self):
        """Speak."""
        return 'Woof!'

    def __str__(self):
        return 'Dog'


class DogFactory:
    """Dog factory class."""

    def get_pet(self) -> Dog:
        """Get pet."""
        return Dog()

    def get_food(self):
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
