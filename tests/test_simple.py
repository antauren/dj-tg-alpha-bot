from django.test import TestCase
from geogame.models import Scenario


def test_success():
    assert True


class TestScenario(TestCase):

    def test_scenario_str_method(self):
        name = 'Some scenario name'
        scenario = Scenario(name=name)
        self.assertEqual(str(scenario), name)
        assert str(scenario), name
