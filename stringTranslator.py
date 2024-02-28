from googletrans import Translator

def englishTranlator(text: str, key: str):
    translator = Translator()

    languages = ['fa', 'tr', 'ar', 'az']

    for lang in languages:
        translation = translator.translate(text, dest=lang)
        print('<string name="{}">{}</string>'.format(key, translation.text))


def persianTranlator(text: str, key: str):
    translator = Translator()

    languages = ['en', 'tr', 'ar', 'az']

    for lang in languages:
        translation = translator.translate(text, dest=lang)
        print('<string name="{}">{}</string>'.format(key, translation.text))
while True:
    option = input('1: englishTranlator\n2: persianTranlator\n3: exit\n')
    if option == '3':
        break

    key = input('enter string key: ')
    text = input('enter string value to translate: ')

    if option == '1':
        englishTranlator(text, key)
    elif option == '2':
        persianTranlator(text, key)