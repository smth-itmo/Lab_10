from handlers import dollar, euro, dream, dream_true, dream_right, stop, randoms
from voice import voice


COMMANDS = [
    {'id': 0, 'text': 'доллар', 'handler': dollar},
    {'id': 1, 'text': 'евро', 'handler': euro},
    {'id': 3, 'text': 'мечта', 'handler': dream},
    {'id': 4, 'text': 'исполни мечту', 'handler': dream_true},
    {'id': 5, 'text': 'настоящая мечта', 'handler': dream_right},
    {'id': 6, 'text': 'стоп', 'handler': stop},
    {'id': 7, 'text': 'случайный курс', 'handler': randoms},


]

ACTIVATION = 'алиса'
class Command:

    def __init__(self, text):
        self.text = text 
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Повторите, пожалуйста')

    def run(self, cmd):
        handler = cmd['handler']
        handler(self.text)