#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

MINI_APP_URL = "https://zhesttp.github.io/drake_learnMINIAPP/"
TEMPLATES_CHANNEL_URL = os.getenv("TEMPLATES_CHANNEL_URL", "https://t.me/your_templates_channel")  # Замените на реальную ссылку канала или добавьте в .env файл

WELCOME_MESSAGE = """🚀 <b>Готов зарабатывать!</b>

Привет! Добро пожаловать в систему заработка на коротких видео от <b>DRAZZE</b>!

📱 <b>Что тебя ждёт:</b>
• Понятная модель заработка на TikTok, YouTube Shorts и Instagram Reels так же Threades
• Пошаговые инструкции для каждой платформы
• Рабочие стратегии и примеры контента
• Системный подход к масштабированию дохода

💎 <b>Как это работает:</b>
Создавай короткие видео, направляй трафик на игровую платформу Drazze.game через свою реферальную ссылку и получай процент с активности привлечённых пользователей.

✨ <b>Начни прямо сейчас!</b>
Открой обучающий курс и пройди пару этапов, чтобы начать зарабатывать уже сегодня."""


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton(text="🎯 Открыть обучающий курс", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="📋 Канал с шаблонами", url=TEMPLATES_CHANNEL_URL)]
    ]
    await update.message.reply_html(WELCOME_MESSAGE, reply_markup=InlineKeyboardMarkup(keyboard))
    logger.info(f"User {user.id} ({user.username}) started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """📚 <b>Доступные команды:</b>

/start - Начать работу с ботом
/help - Показать это сообщение
/app - Открыть обучающий курс

💡 <b>Совет:</b> Используй кнопку "Открыть обучающий курс" для доступа к полному руководству по заработку на коротких видео."""
    keyboard = [
        [InlineKeyboardButton(text="🎯 Открыть обучающий курс", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="📋 Канал с шаблонами", url=TEMPLATES_CHANNEL_URL)]
    ]
    await update.message.reply_html(help_text, reply_markup=InlineKeyboardMarkup(keyboard))


async def app_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(text="🚀 Открыть обучающий курс", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="📋 Канал с шаблонами", url=TEMPLATES_CHANNEL_URL)]
    ]
    await update.message.reply_html("🎯 <b>Открой обучающий курс</b>\n\nНажми на кнопку ниже, чтобы начать обучение и узнать, как зарабатывать на коротких видео!", reply_markup=InlineKeyboardMarkup(keyboard))


async def post_init(application: Application) -> None:
    await application.bot.set_my_commands([
        ("start", "Начать работу с ботом"),
        ("help", "Справка по командам"),
        ("app", "Открыть обучающий курс"),
    ])


def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("❌ Ошибка: BOT_TOKEN не найден в переменных окружения")
        return
    
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("app", app_command))
    
    logger.info("Bot is starting...")
    application.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()
