from falcon import HTTPBadRequest
import json

from infrastructure.service.pyrandom_shuffler import PyrandomShuffler, PyrandomShufflerError


class ShufflerViewV1:
    def on_post(self, req, resp):
        min_value = req.get_param_as_int(name='min_value', required=True)
        max_value = req.get_param_as_int(name='max_value', required=True)

        try:
            seq = PyrandomShuffler.shuffle(
                min_value=min_value,
                max_value=max_value,
            )
        except PyrandomShufflerError as e:
            raise HTTPBadRequest(title=str(e)) from e

        resp.body = json.dumps(seq)


__all__ = ('ShufflerViewV1',)
