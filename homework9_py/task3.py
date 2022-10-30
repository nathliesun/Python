import csv
import os
from os import system
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def add_new_contact_in_phonebook(new_contact): # Добавление нового контакта не из csv
    last_id = read_last_id() + 1
    with open('telephone.csv', 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writerow({'id': last_id, 'First_Name': new_contact[0], 
                'Last_Name': new_contact[1], 'Number': new_contact[2], 
                'Description': new_contact[3]})

def read_last_id(): # Считывание последнего ID
    with open('telephone.csv', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line[0].split(',')
        last_id = int(last_line[0])
        return last_id



async def show_all_contacts (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('telephone.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            await update.message.reply_text(f"{row['id']} {row['First_Name']} {row['Last_Name']} {row['Number']} {row['Description']}")
        await update.message.reply_text('Для добавления контакта введите: /add Имя Фамилия Телефон Примечание')

async def add_new_contact (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = update.message.text.split(' ')
    if len(items) == 5:
        add_new_contact_in_phonebook([items[1], items[2], items[3], items[4]])
    else:
        await update.message.reply_text('Для добавления контакта введите: /add Имя Фамилия Телефон Примечание')




app = ApplicationBuilder().token("5386855733:AAFJNpLKEHIQQj3jQ-2HqOdXVQmbfDEfNOs").build()
app.add_handler(CommandHandler("tel", show_all_contacts))
app.add_handler(CommandHandler("add", add_new_contact))
app.run_polling()