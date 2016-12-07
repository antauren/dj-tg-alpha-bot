import telegram
from telegrambot.test import testcases
try:
    from unittest import mock
except ImportError:
    import mock  # noqa

from geogame.models import Scenario


class TestSimpleCommands(testcases.BaseTestBot):
    fixtures = ['tests/fixtures/scenarios', ]
    start = {
        'in': '/start',
        'out': {
            'parse_mode': 'Markdown',
            'reply_markup': '',
            'text': "Welcome"
        }
    }

    start_new = {
        'in': '/start-new',
        'out': {
            'parse_mode': 'Markdown',
            'reply_markup': '',
            'text': "OK NEW"
        }
    }

    lists_scen01 = {
        'in': '/list',
        'out': {
            'parse_mode': 'Markdown',
            'reply_markup': '/play 1 Найти Кремль',
            'text': "Select from list:"
        }
    }

    lists_scen02 = {
        'in': '/list',
        'out': {
            'parse_mode': 'Markdown',
            'reply_markup': '/play 2 Find BigBen',
            'text': "Select from list:"
        }
    }

    lists_scen_no = {
        'in': '/list',
        'out': {
            'parse_mode': 'Markdown',
            'reply_markup': '',
            'text': "No scenarios at a moment"
        }
    }

    def setUp(self):
        # Bot upon saving tries to install webhook in real telegram
        # But it just breaks tests because of illegal data
        # So it's better to mock a Bot.setWebhook method
        self._original_setWebhook = telegram.bot.Bot.setWebhook
        self.patcher = mock.patch('telegram.bot.Bot.setWebhook')
        self._patched_setWebhook = self.patcher.start()
        super().setUp()

    def tearDown(self):
        # Stop patcher and restore method as it was before
        self.patcher.stop()

    def test_patched_successfully(self):
        assert telegram.bot.Bot.setWebhook is not self._original_setWebhook
        assert telegram.bot.Bot.setWebhook is self._patched_setWebhook

    def test_start(self, ):
        """
        Test bot accept normally command /start and replies as it should.
        """
        self._test_message_ok(self.start)

    def test_start_new(self, ):
        """
        Test bot accept normally command /start and replies as it should.
        """
        self._test_message_ok(self.start_new)

    def test_list(self):
        """
        Test bot can reply command /list and lists available scenarios.
        """
        self._test_message_ok(self.lists_scen01)
        self._test_message_ok(self.lists_scen02)

    def test_list_empty(self):
        """
        Test what to show in case of empty scenarios list.
        """
        Scenario.objects.all().delete()  # now we have empty fixtures
        # print(Scenario.objects.all())  # just to ensure :)
        self._test_message_ok(self.lists_scen_no)

    def test_list_empty2(self):
        """
        Test what to show in case of empty scenarios list with mocked bot view.
        """
        # Substitute with empty queryset
        with mock.patch('geogame.bot_views.ScenariosListCommandView.queryset',
                        Scenario.objects.none()):
            self._test_message_ok(self.lists_scen_no)
