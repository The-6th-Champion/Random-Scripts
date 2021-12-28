from ast import Call
from typing import Any, Tuple, Optional, Callable

class Sequence:
    """
    A class that allows sequences of numbers to be cycled through, and then restarted at the beginning
    """
    def __init__(self, start_bound: int, end_bound: int, filter: Callable) -> None:
        self._start: int = start_bound
        self._end: int = end_bound
        self._current: int = start_bound
        self._index: int = 0
        self._sequence: Tuple = tuple(range(start_bound, end_bound))
        self._return_sequence: Optional[Tuple[Any]] = tuple(filter(i) for i in self._sequence)

    def __getitem__(self, index: int) -> int:
        return self.sequence[index]

    def __len__(self) -> int:
        return len(self.sequence)

    def __repr__(self) -> str:
        return f"Sequence({self.start}, {self.end})"

    def __str__(self) -> str:
        return f"Sequence from {self.start} to {self.end}, inclusive"

    @property
    def start(self) -> int:
        """
        Get the start of the sequence
        """
        return self._start

    @property
    def end(self) -> int:
        """
        The end of the sequence
        """
        return self._end

    @property
    def current(self) -> int:
        """
        Return the current position
        """
        return self._return_sequence[self._index]
    @current.setter
    def current(self, value: int) -> None:
        """
        Set the current position to a value
        """
        if value < self.start or value > self.end:
            raise ValueError(f"{value} is not in the range {self.start} to {self.end}")
        self._current = value

    @property
    def sequence(self) -> Tuple:
        """
        Return the sequence of numbers
        """
        return self._return_sequence

    def reset(self, end: bool=False) -> None:
        """
        Reset the current position to the start
        """
        if end:
            self._current = self._end
            self._index = len(self._sequence) - 1
        else:
            self._current = self._start
            self._index = 0

    def _advance(self) -> None:
        """
        Move the current position forward by one
        """
        self._index += 1
        self._current = self.sequence[self._index]

    def _recede(self) -> None:
        """
        Move the current position backwards by one
        """
        self._index -= 1
        self._current = self.sequence[self._index]

    def move_forward(self, amount: int, reverse: bool=False) -> None:
        """
        Move the current position forward by one, or backwards by one
        """
        for i in range(amount):
            if reverse:
                if self._current == self._start:
                    print(f"{self._current} is already at the start of the sequence")
                    self.reset(True)
                else:
                    print(f"Moving backwards by one")
                    self._recede()
            else:
                if self._current == self._end:
                    print(f"{self._current} is already at the end of the sequence")
                    self.reset()
                else:
                    print(f"Moving forward by one")
                    self._advance()