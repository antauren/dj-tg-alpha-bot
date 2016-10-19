"""
Test Configuration of logger.
"""


import os, importlib
from unittest.mock import patch
# from django.test import TestCase
# from unittest import skip
# we have to use tools outside of django, because when it's initialized
# it's too late to change environment variables
from unittest import TestCase, skip

class LoggingLevelTest(TestCase):

    levels = ('DEBUG', 'INFO', 'CRITICAL', 'WARNING',)

    # @skip
    def test_loglevel_debug(self):
        """
        Checks config accepts environment variable
        DJANGO_LOG_LEVEL and sets log level according to it
        """
        env_var = 'DJANGO_LOG_LEVEL'
        for level in self.levels:
            with patch.dict('os.environ', {env_var: level}):
                from dj_tg_bot import settings
                importlib.reload(settings)
                # print(os.environ[env_var])  # should print out 'newvalue'
                assert env_var in os.environ  # should be True
                # print(settings.LOGGING['loggers'])
                # django application should get logging setting DJANGO_LOG_LEVEL
                self.assertEqual(
                    settings.LOGGING['loggers']['django']['level'], level
                )
                # geogame too
                self.assertEqual(
                    settings.LOGGING['loggers']['geogame']['level'], level
                )
            assert env_var not in os.environ  # should be True
