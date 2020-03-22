"""Interpreter pattern module."""


class RomanNumberInterpreter:
    """Roman number interpreter class."""
    def __init__(self) -> None:
        """Initialization."""
        self.dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self, text: str) -> int:
        """
        Converts Roman number to Arabic number.

        :param text: Roman number
        :return: Arabic number
        :rtype: int
        """
        numbers = map(self.dictionary.get, text)

        if None in numbers:
            raise ValueError('Error value: {0}'.format(text))

        result = 0
        tmp = None

        for number in map(self.dictionary.get, text):
            if tmp is None or tmp >= number:
                result += number
            else:
                result += (number - tmp * 2)
            tmp = number
        return result


if __name__ == '__main__':
    INTERPRETER = RomanNumberInterpreter()
    print(INTERPRETER.interpret('MMMCMXCX'))
    print(INTERPRETER.interpret('MCMLXXXVIII'))
    print(INTERPRETER.interpret('MMXX'))
