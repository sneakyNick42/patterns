"""Prototype pattern module."""
import copy


class Prototype:
    """Prototype class."""
    def __init__(self) -> None:
        self._objects = {}

    def register(self, name, obj):
        """Register object."""
        self._objects[name] = obj

    def unregister(self, name):
        """Unregister object."""
        del self._objects[name]

    def clone(self, name, **kwargs):
        """Clone object."""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class SpiderMan:
    """Spider-Man class."""
    def __init__(self) -> None:
        self.name = 'Spider-man'
        self.power = 'Unlimited'

    def __str__(self):
        return '{0}\'s power is {1}'.format(self.name, self.power)


if __name__ == '__main__':
    HERO = SpiderMan()
    PROTOTYPE = Prototype()
    PROTOTYPE.register('Spider-Man', HERO)

    ANOTHER_CLONE = PROTOTYPE.clone('Spider-Man')
    print(ANOTHER_CLONE)
