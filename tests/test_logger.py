"""
Test Configuration of logger.
"""


<<<<<<< HEAD
import os
=======
import os, importlib
>>>>>>> master
from unittest.mock import patch
# from django.test import TestCase
# from unittest import skip
# we have to use tools outside of django, because when it's initialized
# it's too late to change environment variables
<<<<<<< HEAD
from unittest import TestCase, skip

class LoggingLevelTest(TestCase):

=======
from unittest import TestCase, skip, main

class LoggingLevelTest(TestCase):

    levels = ('DEBUG', 'INFO', 'CRITICAL', 'WARNING',)

>>>>>>> master
    # @skip
    def test_loglevel_debug(self):
        """
        Checks config accepts environment variable
        DJANGO_LOG_LEVEL and sets log level according to it
        """
<<<<<<< HEAD
        env_var = 'DJANGO_LOG_LEVEL'
        with patch.dict('os.environ', {env_var: 'DEBUG'}):
            from dj_tg_bot import settings
            print(os.environ[env_var])  # should print out 'newvalue'
            assert env_var in os.environ  # should be True
            print(settings.LOGGING['loggers'])
            self.assertEqual(settings.LOGGING['loggers']['django']['level'],
                             'DEBUG')
        assert env_var not in os.environ  # should be True
=======

        env_var = 'DJANGO_LOG_LEVEL'
        from dj_tg_bot import settings
        for level in self.levels:
            with patch.dict('os.environ', {env_var: level}):
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

if __name__ == '__main__':
    main()
>>>>>>> master
