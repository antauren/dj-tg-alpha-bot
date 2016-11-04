"""
Views of Bot sepateated from standard web views.
"""

from telegrambot.bot_views.generic import TemplateCommandView, ListCommandView
from geogame.models import Scenario
import logging

logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'geogame/messages/command_start_text.txt'


class ScenariosListCommandView(ListCommandView):
    # """docstring for ListView."""
    template_text = 'geogame/messages/command_list_text.txt'
    template_keyboard = 'geogame/messages/command_list_keyboard.txt'
    context_object_name = 'scenarios'
    model = Scenario

    def get_context(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context(*args, **kwargs)
        if not context[self.context_object_name]:
            # empty list - disable a keybord
            self.template_keyboard = None
        return context


class UnknownView(TemplateCommandView):
    template_text = "geogame/messages/command_unknown_text.txt"
