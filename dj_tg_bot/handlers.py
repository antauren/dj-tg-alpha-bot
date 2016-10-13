from telegrambot.handlers import command, unknown_command
from geogame.bot_views import StartView

urlpatterns = [
    command('start', StartView.as_command_view()),
    unknown_command(UnknownView.as_command_view()),
]
