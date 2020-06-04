from typing import Sequence
import random

from domain.service.shuffler import Shuffler, ShufflerError


class PyrandomShufflerError(ShufflerError):
    pass


class PyrandomShuffler(Shuffler):
    @classmethod
    def shuffle(cls, min_value: int, max_value: int) -> Sequence[int]:
        try:
            cls.check_params(min_value=min_value, max_value=max_value)
        except Exception as e:
            raise PyrandomShufflerError(str(e)) from e

        seq = list(range(min_value, max_value + 1))
        random.shuffle(seq)
        return seq


__all__ = ('PyrandomShuffler', 'PyrandomShufflerError')
