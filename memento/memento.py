"""Mediator pattern module."""
import pickle


class OnePlaceFridge:
    """Fridge class."""
    def __init__(self) -> None:
        self._state = 'Empty'

    def set_state(self, new_state):
        """Change fridge state."""
        self._state = new_state

    def freeze_food(self) -> pickle:
        """Freeze food."""
        return pickle.dumps(vars(self))

    def defrost_food(self, food) -> None:
        """Defrost food."""
        previous_state = pickle.loads(food)
        vars(self).clear()
        vars(self).update(previous_state)


if __name__ == '__main__':
    FRIDGE = OnePlaceFridge()

    print(vars(FRIDGE))

    MEAT = FRIDGE.freeze_food()

    FRIDGE.set_state('Full')

    print(vars(FRIDGE))

    FRIDGE.defrost_food(MEAT)

    print(vars(FRIDGE))
