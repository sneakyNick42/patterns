"""Builder pattern module."""


class Director:
    """Director class."""
    def __init__(self, builder) -> None:
        self._builder = builder

    def construct_transformer(self):
        """Construct transformer."""
        self._builder.create_transformer()
        self._builder.add_model()
        self._builder.add_head()
        self._builder.add_torso()
        self._builder.add_arms()
        self._builder.add_legs()

    def get(self):
        """Get transformer."""
        return self._builder.product


class Builder:
    """Abstract builder class."""
    def __init__(self) -> None:
        self.product = None

    def create_transformer(self):
        """Create transformer."""
        self.product = Transformer()


class OptimusPrimeBuilder(Builder):
    """Optimus Prime builder class."""
    def add_model(self):
        """Add model."""
        self.product.model = 'Optimus Prime'

    def add_head(self):
        """Add head."""
        self.product.head = 'Blue head'

    def add_torso(self):
        """Add torso."""
        self.product.torso = 'Red torso'

    def add_arms(self):
        """Add arms."""
        self.product.arms = 'Red arms'

    def add_legs(self):
        """Add legs."""
        self.product.legs = 'Blue legs'


class BumblebeeBuilder(OptimusPrimeBuilder):
    """Bumblebee builder class."""
    def add_model(self):
        self.product.model = 'Bumblebee'

    def add_head(self):
        self.product.head = 'Yellow head'

    def add_torso(self):
        self.product.torso = 'Yellow torso'

    def add_arms(self):
        self.product.arms = 'Yellow arms'

    def add_legs(self):
        self.product.legs = 'Yellow legs'


class Transformer:
    """Transformer class."""
    def __init__(self) -> None:
        self.model = None
        self.head = None
        self.torso = None
        self.arms = None
        self.legs = None

    def __str__(self):
        return '{0}: {1}, {2}, {3}, {4}'.format(
            self.model, self.head, self.torso, self.arms, self.legs
        )


if __name__ == '__main__':
    OPTIMUS_BUILDER = OptimusPrimeBuilder()
    BUMBLEBEE_BUILDER = BumblebeeBuilder()

    OPTIMUS_DIRECTOR = Director(OPTIMUS_BUILDER)
    BUMBLEBEE_DIRECTOR = Director(BUMBLEBEE_BUILDER)

    OPTIMUS_DIRECTOR.construct_transformer()
    BUMBLEBEE_DIRECTOR.construct_transformer()
    OPTIMUS_PRIME = OPTIMUS_DIRECTOR.get()
    BUMBLEBEE = BUMBLEBEE_DIRECTOR.get()

    print(OPTIMUS_PRIME)
    print(BUMBLEBEE)
