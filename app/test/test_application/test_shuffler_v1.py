from falcon import testing

from application.startup import api


class BaseTestCase(testing.TestCase):
    def setUp(self):
        super().setUp()
        self.app = api


class TestShuffler(BaseTestCase):
    url = '/v1/shuffler'

    def test_standard(self):
        a = 5
        b = 10
        result = self.simulate_post(
            self.url,
            params={
                'min_value': a,
                'max_value': b,
            },
        )
        self.assertEqual(result.status_code, 200)

        seq = list(range(a, b + 1))
        self.assertEqual(len(result.json), len(seq))
        for i in seq:
            self.assertIn(i, seq)

    def test_equal_values(self):
        a = 5
        result = self.simulate_post(
            self.url,
            params={
                'min_value': a,
                'max_value': a,
            },
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, [a])

    def test_wrong_values(self):
        a = 5
        b = 10
        result = self.simulate_post(
            self.url,
            params={
                'min_value': b,
                'max_value': a,
            },
        )
        self.assertEqual(result.status_code, 400)
