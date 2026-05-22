from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import asyncio

token = "8809806959:AAFf0o_USa5j2O-7XlTvY0odp4tEVhUTOeA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="هاي يروحقلبي دا مش اكونتي الاصلي خش البايو هتلاقي القناة بتاعي تعالا كل الدلع هناك")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="كل الدلع هنا يروحي @mariom131")


if __name__ == "__main__":

    app = ApplicationBuilder().token(token).build()

    scommand = CommandHandler("start", start)
    hcommand = CommandHandler("help", help)

    app.add_handler(scommand)
    app.add_handler(hcommand)

    app.run_polling()

    # (Update
    #  (message=Message(channel_chat_created=False, 
    # chat=Chat(first_name='مريومة', id=8238137251, last_name='الدلوعة🔥🫦', type=<ChatType.PRIVATE>, username='Mariom446'),
    # date=datetime.datetime(2026, 5, 22, 19, 11, 25, tzinfo=datetime.timezone.utc),delete_chat_photo=False,
    # from_user=User(first_name='مريومة', id=8238137251, is_bot=False, language_code='en', last_name='الدلوعة🔥🫦', username='Mariom446')
    # , group_chat_c reated=False, message_id=3, supergroup_chat_created=False, text='hph')