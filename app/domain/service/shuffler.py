from abc import ABC, abstractmethod
from typing import Sequence

from domain.exception import CoreError


class ShufflerError(CoreError):
    pass


class Shuffler(ABC):
    @classmethod
    @abstractmethod
    def shuffle(cls, min_value: int, max_value: int) -> Sequence[int]:
        pass

    @classmethod
    def check_params(cls, min_value: int, max_value: int) -> None:
        if min_value > max_value:
            raise ShufflerError('Min value ({}) must be less or equal to max value ({})'.format(min_value, max_value))


__all__ = ('Shuffler', 'ShufflerError')
