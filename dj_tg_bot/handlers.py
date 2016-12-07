from telegrambot.handlers import command, unknown_command
from geogame.bot_views import StartView, StartNewView, \
    ScenariosListCommandView, UnknownView

urlpatterns = [
    command('start-new', StartNewView.as_command_view()),
    command('start', StartView.as_command_view()),
    command('list', ScenariosListCommandView.as_command_view()),
    unknown_command(UnknownView.as_command_view()),
]
