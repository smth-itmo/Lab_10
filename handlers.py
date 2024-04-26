import random
from voice import voice
import webbrowser
import requests
import pyautogui


def dollar(text):
    options = [
        'Вот настоящий курс доллара на данный момент',
        'Я бы на твоем месте не смотрела',
        'Упадёт ещё',
    ]
    webbrowser.open('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+&gs_lcrp=EgZjaHJvbWUqEAgBEAAYgwEYsQMYyQMYgAQyBggAEEUYOTIQCAEQABiDARixAxjJAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDIGCAQQRRg9MgYIBRBFGD0yBggGEEUYPTIGCAcQRRhB0gEIMjk1M2owajmoAgCwAgE&sourceid=chrome&ie=UTF-8')
    sel = random.choice(options)
    voice.text_to_speech(sel)

def euro(text):
    options = [
        'Вот настоящий курс евро на данный момент',
        'Я бы на твоем месте не смотрела',
        'Упадёт ещё',
    ]
    webbrowser.open('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sca_esv=324d2da6d69578fe&sxsrf=ACQVn08Qw-4Yaje_BEOF7Tkl6SI6mOcrPQ%3A1714147694489&ei=btErZs23HZ62wPAP78KK8AU&ved=0ahUKEwjNprDjoeCFAxUeGxAIHW-hAl4Q4dUDCBA&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiEdC60YPRgNGBINC10LLRgNC-MhMQABiABBixAxiDARjJAxhGGIICMggQABiABBixAzILEAAYgAQYsQMYgwEyDhAAGIAEGLEDGJIDGIMBMgsQABiABBiSAxiKBTIFEAAYgAQyERAuGIAEGLEDGIMBGMcBGK8BMgUQABiABDIFEAAYgAQyCxAAGIAEGLEDGIMBMh8QABiABBixAxiDARjJAxhGGIICGJcFGIwFGN0E2AEBSJoRUKEGWJEOcAN4AZABAJgBO6AB7wOqAQE5uAEDyAEA-AEBmAIMoALRBMICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIKECMYgAQYJxiKBcICChAAGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgIQEAAYgAQYsQMYgwEYFBiHAsICDRAAGIAEGLEDGEMYigXCAg8QIxiABBgnGIoFGEYYggLCAggQABiABBiSA8ICGRAAGIAEGIoFGEYYggIYlwUYjAUY3QTYAQHCAgQQABgDwgIOEAAYgAQYsQMYgwEYyQOYAwCIBgGQBgq6BgYIARABGBOSBwIxMqAHk2A&sclient=gws-wiz-serp')
    sel = random.choice(options)
    voice.text_to_speech(sel)

def dream(text):
    webbrowser.open('https://forbes.kz/img/articles/d70c7d3313293ec11405d8ca561a3151-small.jpg')
    voice.text_to_speech('Вот ваша мечта')

def dream_right(text):
    webbrowser.open('https://photos.app.goo.gl/fXXpRt5MgfwrvzmT7')
    voice.text_to_speech('Вот ваша настоящая мечта')

def dream_true(text):
    url = 'https://forbes.kz/img/articles/d70c7d3313293ec11405d8ca561a3151-small.jpg'
    response = requests.get(url)
    voice.text_to_speech('Я исполнила вашу мечту, и теперь она всегда будет рядом с вами в папке этой лабороторной')
    with open('мечта тут.jpg', 'wb') as f:
        f.write(response.content)

def stop(text):
    options = [
        'Понимаю, на это тяжело смотреть',
        'Да, лучше на это не смотреть',
    ]
    pyautogui.hotkey('ctrl', 'w')
    sel = random.choice(options)
    voice.text_to_speech(sel)


def randoms(text):
    options = [
        'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F&oq=rehc+&gs_lcrp=EgZjaHJvbWUqDwgFEAAYChiDARixAxiABDIGCAAQRRg5MhIIARAAGAoYgwEYsQMYyQMYgAQyDwgCEAAYChiDARixAxiABDIPCAMQABgKGIMBGLEDGIAEMg8IBBAAGAoYgwEYsQMYgAQyDwgFEAAYChiDARixAxiABDIMCAYQABgKGJIDGIAEMg0IBxAAGJIDGIAEGIoFMg8ICBAAGAoYgwEYsQMYgAQyDwgJEAAYChiDARixAxiABNIBCDQ2NTNqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8',
        'https://www.google.com/search?q=rehc+rhjya&oq=rehc+rhjya&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMgkIAhAAGA0YgAQyCQgDEAAYDRiABDIJCAQQABgNGIAEMgkIBRAAGA0YgAQyCQgGEAAYDRiABDIJCAcQABgNGIAEMgkICBAAGA0YgAQyCQgJEAAYDRiABNIBCDE5NDZqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8',
        'https://www.google.com/search?q=rehc+kbhs&oq=rehc+kbhs&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABgKGIMBGLEDGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyCQgGEAAYChiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDY3NzVqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8',
        'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=324d2da6d69578fe&sxsrf=ACQVn09RnwYUf542WkFDR6ga1vrueNmtqA%3A1714150997600&ei=Vd4rZqqWJNe73AOjm6aIAQ&udm=&oq=rehc+ntyut&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnJlaGMgbnR5dXQqAggAMgkQABiABBgKGCoyDRAAGIAEGLEDGIMBGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApIqh1QlQVYkxJwA3gAkAEAmAFLoAHkBaoBAjExuAEByAEA-AEBmAINoAKYBsICChAAGLADGNYEGEfCAhEQLhiABBixAxjRAxiDARjHAcICCxAuGIAEGLEDGIMBwgILEAAYgAQYsQMYgwHCAg4QLhiABBixAxjRAxjHAcICCBAAGIAEGLEDwgIgEC4YgAQYsQMY0QMYgwEYxwEYlwUY3AQY3gQY4ATYAQHCAhAQLhiABBjRAxhDGMcBGIoFwgIFEC4YgATCAh8QLhiABBjRAxhDGMcBGIoFGJcFGNwEGN4EGOAE2AEBwgIOEAAYgAQYARjJAxgKGCrCAgkQABiABBgBGArCAgsQABiABBiSAxiKBcICBxAjGLECGCfCAgoQABiABBhDGIoFwgIQEAAYgAQYsQMYQxiDARiKBcICChAAGIAEGLEDGArCAgwQIxixAhgnGEYYggLCAhYQABixAhhGGIICGJcFGIwFGN0E2AECwgIIEAAYogQYiQXCAggQABiABBiiBMICDhAAGIAEGAoYKhhGGIICwgIaEAAYgAQYChgqGEYYggIYlwUYjAUY3QTYAQKYAwCIBgGQBgi6BgYIARABGBS6BgYIAhABGBOSBwIxM6AH_WU&sclient=gws-wiz-serp'
    ]
    sel = random.choice(options)
    webbrowser.open(sel)
    voice.text_to_speech('Вот курс случайной валюты к рублю')
