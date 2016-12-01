from telegrambot.handlers import command, unknown_command
from geogame.bot_views import StartView, StartView1, \
    ScenariosListCommandView, UnknownView

urlpatterns = [
    command('start', StartView.as_command_view()),
    command('start1', StartView1.as_command_view()),
    command('list', ScenariosListCommandView.as_command_view()),
    unknown_command(UnknownView.as_command_view()),
]
