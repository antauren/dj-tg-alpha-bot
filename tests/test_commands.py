import telegram
from telegrambot.test import testcases
try:
    from unittest import mock
except ImportError:
    import mock  # noqa


class TestSimpleCommands(testcases.BaseTestBot):
    fixtures = [
        'tests/fixtures/scenarios',
    ]
    start = {'in': '/start',
             'out': {'parse_mode': 'Markdown',
                     'reply_markup': '',
                     'text': "Welcome"}}

    lists = {'in': '/list',
             'out': {'parse_mode': 'Markdown',
                     'reply_markup': '/scenario 1',
                     'text': "Select from list:"}}

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

    def test_start(self,):
        """
        Test bot accept normally command /start and replies as it should.
        """
        self._test_message_ok(self.start)

    def test_list(self):
        """
        Test bot can reply command /list and lists available scenarios.
        """
        self._test_message_ok(self.lists)
