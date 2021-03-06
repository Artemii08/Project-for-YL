import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters, Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/morse', '/binary', '/caesar']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard = [['/start']]
markup_s = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Приветствую! Это бот для кодирования ваших сообщений различными способами. Выберите шифр.",
        reply_markup=markup
    )


def morse(update, context):
    update.message.reply_text(
        "Введите текст для кодирования.",
        reply_markup=ReplyKeyboardRemove()
    )

    return 1


def binary(update, context):
    update.message.reply_text(
        "Введите текст для кодирования.",
        reply_markup=ReplyKeyboardRemove()
    )

    return 1


reply_keyboard = [['/english', '/russian', '/stop']]
markup_c = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def caesar(update, context):
    update.message.reply_text(
        "Выберите язык шифра.",
        reply_markup=markup_c
    )

    return ConversationHandler.END


def english(update, context):
    update.message.reply_text(
        "Введите число (шаг) и текст через точку с запятой (;)",
        reply_markup=ReplyKeyboardRemove()
    )

    return 1


def russian(update, context):
    update.message.reply_text(
        "Введите число (шаг) и текст через точку с запятой (;)",
        reply_markup=ReplyKeyboardRemove()
    )

    return 1


def english_next(update, context):
    alf_eng = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alf_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if ";" in update.message.text and update.message.text.count(";") < 2:
        step = update.message.text.split(";")[0]
        text = list(update.message.text.split(";")[1].lower())
        answer = []
        for i in text:
            if i in alf_eng:
                answer.append(alf_eng[alf_eng.find(i) + int(step)])
            elif i in alf_rus:
                answer = list("Некорректный язык ввода. Попробуйте снова.")
                continue
            else:
                answer.append(i)
    else:
        answer = list("Некорректный ввод. Попробуйте снова.")
    update.message.reply_text(
        "".join(answer),
        reply_markup=markup
    )

    return ConversationHandler.END


def russian_next(update, context):
    alf_eng = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alf_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if ";" in update.message.text and update.message.text.count(";") < 2:
        step = update.message.text.split(";")[0]
        text = list(update.message.text.split(";")[1].lower())
        print(step, text)
        answer = []
        for i in text:
            if i in alf_rus:
                answer.append(alf_rus[alf_rus.find(i) + int(step)])
            elif i in alf_eng:
                answer = list("Некорректный язык ввода. Попробуйте снова.")
                continue
            else:
                answer.append(i)
    else:
        answer = list("Некорректный ввод. Попробуйте снова.")
    update.message.reply_text(
        "".join(answer),
        reply_markup=markup
    )

    return ConversationHandler.END


def morse_next(update, context):
    text = list(update.message.text.lower())
    morse_symbols = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                     'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                     'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                     's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                     'y': '-.--', 'z': '--..', ' ': '\t', 'а': '.-', 'б': '-...', 'в': '.--',
                     'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..',
                     'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
                     'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.',
                     'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-',
                     'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--',
                     'я': '.-.-', '?': '..--..', '.': '·–·–·–', ',': '––··––', '-': '-....-',
                     ':': '---...', '"': '.-..-.', '!': '-.-.--', ';': '-.-.-.', '_': '..--.-',
                     '=': '-...-', '+': '.-.-.', '(': '-.--.', ')': '-.--.-', '$': '...-..-',
                     '&': '.-...', '@': '.--.-.'
                     }
    morse_text = []
    for i in text:
        morse_text.append(morse_symbols[i])
    update.message.reply_text(
        " ".join(morse_text) + "\n"
                               "Для удобства расшифровки сообщения буквы разделены пробелами"
                               ", а слова - табуляцией. Не забудьте упомянуть отправителю"
                               " язык сообщения, так как обозначения некоторых букв совпадают!",
        reply_markup=markup
    )

    return ConversationHandler.END


def binary_next(update, context):
    text = list(update.message.text.lower())
    binary_text = []
    for i in text:
        n = ord(str(i))
        b = ""
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        if len(b) < 12:
            b = "0" * (12 - len(b)) + b
        binary_text.append(b)
    update.message.reply_text(
        str("".join(binary_text)) + "\n"
                                    "Для удобства расшифровки сообщения каждая "
                                    "буква имеет числовое значение одинаковой "
                                    "длинны - 12 цифр. Если числовое значение буквы "
                                    "оказалось меньше необходимого, то в начале к нему "
                                    "приписываются 0 до необходимого. Не забудьте "
                                    "упомянуть этот факт перед вашим собесединком.",
        reply_markup=markup
    )

    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    conv_handler_m = ConversationHandler(
        entry_points=[CommandHandler('morse', morse)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, morse_next)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    conv_handler_b = ConversationHandler(
        entry_points=[CommandHandler('binary', binary)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, binary_next)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    conv_handler_ce = ConversationHandler(
        entry_points=[CommandHandler('english', english)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, english_next)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    conv_handler_cr = ConversationHandler(
        entry_points=[CommandHandler('russian', russian)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, russian_next)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('caesar', caesar))
    dp.add_handler(conv_handler_m)
    dp.add_handler(conv_handler_b)
    dp.add_handler(conv_handler_ce)
    dp.add_handler(conv_handler_cr)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
