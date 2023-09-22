#db.py

#import sqlite3

#class Database:
#	def __init__(self, db_file):
#		self.connection = sqlite3.connect(db_file)
#		self.cursor = self.connection.cursor()
#
#	def user_exists(self, user_id):
#		with self.connection:
#			result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
#			return bool(len(result))
#
#	def add_user(self, user_id):
#		with self.connection:
#			return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
#
#	def set_active(self, user_id, active):
#		with self.connection:
#			return self.cursor.execute("UPDATE 'users' SET 'active' = ? WHERE 'user_id' = ?", (active, user_id,))
#	
#	def get_users(self):
#		with self.connection:
#			return self.cursor.execute("SELECT user_id, active FROM 'users'").fetchall()







#Moon.py


#from aiogram import Bot, types
#from aiogram.dispatcher import Dispatcher
#from aiogram.utils import executor
#import logging
#from db import Database
#
#logging.basicConfig(level=logging.INFO)
#
#TOKEN= '5380718904:AAGqkG7V100TXMzU0LHhvNuoHivdvJbjX28'
#bot = Bot(token=TOKEN)
#dp = Dispatcher(bot)
#db = Database('database.db')
#
#@dp.message_handler(commands=['start'])
#async def start(message: types.Message):
#    if message.chat.type == 'private':
#        if not db.user_exists(message.from_user.id):
#            db.add_user(message.from_user.id)
#        await bot.send_message(message.from_user.id, 'Добро пожаловать!')
#
#@dp.message_handler(commands=['sendall'])
#async def sendall(message: types.Message):
#    if message.chat.type == 'private':
#        if message.from_user.id == 1400426958:
#            text = message.text[9:]
#            users = db.get_users()
#            for row in users:
#                try:
#                    await bot.send_message(row[0], text)
#                    if int(row[1]) != 1:
#                        db.set_active(row[0], 1)
#                except:
#                    db.set_active(row[0], 0)
#
#            await bot.send_message(message.from_user.id, 'Успешная рассылка!')
#
#
#
#if __name__ == '__main__':
#    executor.start_polling(dp, skip_updates=True)

#/sendall тут текст рассылки
"""
ТАКЖЕ БОТ ПОДКЛЮЧЁН К БД И ТАМ СОХРАНЯЮТСЯ ПОЛЬЗОВАТЕЛИ
"""