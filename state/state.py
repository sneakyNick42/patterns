"""State pattern module."""
from typing import List


class HeroForm:
    """Hero state class."""
    name: str = 'Form'
    allowed: List = []

    def next_form(self, form):
        """Set next form."""
        if form.name in self.allowed:
            not_final = 'This isn\'t even my final form!' if form.allowed else ''
            print('{0}! {1}'.format(form.name, not_final))
            self.__class__ = form
        else:
            print('Impossibru! It\'s over 9000!')

    def __str__(self) -> str:
        return self.name


class ZeroForm(HeroForm):
    """Zero hero form."""
    name = 'Zero Form'
    allowed = ['First Form']


class FirstForm(HeroForm):
    """First hero form."""
    name = 'First Form'
    allowed = ['Second Form']


class SecondForm(HeroForm):
    """Second hero form."""
    name = 'Second Form'
    allowed = ['Final Form']


class FinalForm(HeroForm):
    """Final form."""
    name = 'Final Form'
    allowed = []


class Hero:
    """Hero class."""
    def __init__(self) -> None:
        self.current = ZeroForm()

    def set_form(self, form):
        """Set form."""
        self.current.next_form(form)


if __name__ == '__main__':
    HERO = Hero()

    HERO.set_form(FirstForm)
    HERO.set_form(SecondForm)
    HERO.set_form(FinalForm)
    HERO.set_form(FirstForm)
