import threading
import time
import sys

class CursorAnimation(threading.Thread):
    def __init__(self):
        self.flag = True
        self.animation_char = "|/-\\"
        self.idx = 0
        threading.Thread.__init__(self)

    def run(self):
        while self.flag:
            print("Processing... ", self.animation_char[self.idx % len(self.animation_char)]+"\r")
            sys.stdout.flush()
            self.idx += 1
            time.sleep(0.1)

    def stop(self):
        self.flag = False

if __name__ == '__main__':
    spin = CursorAnimation()

    # Start Animation
    spin.start()

    # Do something here
    # Example: sleep
    time.sleep(5)

    # Stop Animation
    spin.stop()