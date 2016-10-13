"""
Views of Bot sepateated from standard web views.
"""
from telegrambot.bot_views.generic import TemplateCommandView


class StartView(TemplateCommandView):
    template_text = 'geogame/messages/command_start_text.txt'


class UnknownView(generic.TemplateCommandView):
    template_text = "geogame/messages/command_unknown_text.txt"
