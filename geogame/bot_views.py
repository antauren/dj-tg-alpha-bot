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
    # def __init__(self, arg):
    #     super(ListView, self).__init__()
    #     self.arg = arg


class UnknownView(TemplateCommandView):
    template_text = "geogame/messages/command_unknown_text.txt"
