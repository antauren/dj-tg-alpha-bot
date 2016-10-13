from telegrambot.handlers import command
from geogame.bot_views import StartView

urlpatterns = [
    command('start', StartView.as_command_view()),
]
