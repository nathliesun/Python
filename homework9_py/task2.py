from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'/menu \n /sum \n /minus \n /mult \n /del')
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/sum \n /minus \n /mult \n /del')
    await update.message.reply_text(f'Вводите  комплексные числа в формате a+bj \n')
 



async def sum (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print (msg)
    items = msg.split()
    len(items) #/sum 123
    x= complex(items[1])
    y= complex(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def minus (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print (msg)
    items = msg.split() #/sum 123
    x= complex(items[1])
    y= complex(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def mult (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print (msg)
    items = msg.split() #/sum 123
    x= complex(items[1])
    y= complex(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def delit (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print (msg)
    items = msg.split() #/sum 123
    x= complex(items[1])
    y= complex(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')


app = ApplicationBuilder().token("5386855733:AAFJNpLKEHIQQj3jQ-2HqOdXVQmbfDEfNOs").build()


app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("minus", minus))
app.add_handler(CommandHandler("mult", mult))
app.add_handler(CommandHandler("delit", delit))
app.run_polling()