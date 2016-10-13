"""
Views of Bot sepateated from standard web views.
"""
from telegrambot.bot_views import generic #import TemplateCommandView


class TemplateCommandView(generic.TemplateCommandView):
    # template_text = None
    # template_keyboard = None
    #
    # def get_context(self, bot, update, **kwargs):
    #     return None

    def handle(self, bot, update, **kwargs):
        try:
            ctx = self.get_context(bot, update, **kwargs)
            text = TextResponse(self.template_text, ctx).render()
            keyboard = KeyboardResponse(self.template_keyboard, ctx).render()
            logger.debug("Text:" + str(text.encode('utf-8')))
            logger.debug("Keyboard:" + str(keyboard))
            if text:
                if not PY3:
                    text = text.encode('utf-8')
                bot.send_message(chat_id=update.message.chat_id, text=text,
                                 reply_markup=keyboard,
                                 parse_mode=ParseMode.MARKDOWN)
            else:
                logger.info("No text response for update %s" % str(update))
        except:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            logger.error(*exc_info)
            raise

    # @classmethod
    # def as_command_view(cls, **initkwargs):
    #     def view(bot, update, **kwargs):
    #         self = cls(**initkwargs)
    #         return self.handle(bot, update, **kwargs)
    #     return view


class StartView(TemplateCommandView):
    template_text = 'geogame/messages/command_start_text.txt'


class UnknownView(TemplateCommandView):
    template_text = "geogame/messages/command_unknown_text.txt"
