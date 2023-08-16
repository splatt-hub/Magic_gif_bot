from aiogram import executor, types
import loader
import requests
import json
from keyboard import kb_button

bot = loader.bot
dp = loader.dp

async def on_startup(_):
    print("Magic_Bot запушен")

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    await message.answer(f'Привет, <b>{message.from_user.first_name}!</b> задавай свой вопрос...', parse_mode="HTML", reply_markup = kb_button)
    await message.delete()

@dp.message_handler(text = '/help')
async def help_command(message: types.Message):
    await message.answer("""
/start-Начало работы бота 
/help-команды бота
/description-описание бота
/pogoda-погода в Воронеже
Задай свой вопрос и я отвечу да/нет
""")
    await message.delete()

@dp.message_handler(commands = ['description'])
async def description(message: types.Message):
    await message.answer(f'Раньше, чтобы определиться со сложным выбором, человеку приходилось прибегать к помощи "монетки". '
                         f'21 Век-высоких технологий и редко у кого может заваляться в кармане монетка.'
                         f'Но больше она тебе и не пригодится если у тебя есть MagicBot')
    await message.delete()

@dp.message_handler(text = '/pogoda')
async def weather(message: types.Message):
    res = requests.get(f'https://goweather.herokuapp.com/weather/Voronezh')
    data = json.loads(res.text)
    a = list(data.items())
    b = 'Погода сейчас: '
    for i in a[:3]:
        b += (str(i[0]) + ":" + str(i[1]) + '; ')
    await bot.send_message(message.chat.id, b)

    g = data['forecast']
    c = list(g[0].items())
    b = 'Погода на завтра: '
    for i in c[1:]:
        b +=(i[0] + ':' + i[1] + '; ')
    await bot.send_message(message.chat.id, b)
    await message.delete()

@dp.message_handler(content_types=['text'])
async def yesno(message: types.Message):
    res = requests.get('https://yesno.wtf/api')
    data = json.loads(res.text)
    await bot.send_animation(message.chat.id, data['image'])
    await bot.send_message(message.chat.id, data['answer'])


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates = True)