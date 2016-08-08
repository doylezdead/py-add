import colors
import py_add.lib as addlib
import sys
import time

UP = '\033[1A'

def entry_point():
    sys.exit(CLI().run())

class CLI(object):
    motd = ''
    stack = addlib.OperationsStack()
    running = True
    width, height = addlib.get_size()

    def __init__(self):
        self.motd = 'Welcome :)'
        control_actions = {
            'q': self.end,
            'w': self.write,
            '[': self.step_back,
            ']': self.cancel_lookback()
        }

        #start setting up terminal
        sys.stdout.write('\n'*self.height)
        sys.stdout.flush()


    def run(self):
        count = 0;
        sys.stdout.write('   ' + '=' * (self.width - 6) + '\n\n   ' + '=' * (self.width - 6) + '{}\r'.format(UP))

        while self.running:
            sys.stdout.write(' ' * self.width + '\r   >{}> '.format(count))
            sys.stdout.flush()
            input_str = input()
            count+=1
            sys.stdout.write('   ' + '=' * (self.width - 6) + '{}\r'.format(UP))

        sys.stdout.flush()
        print('\n\nThank you for your patronage')
        return 0

    def write(self):
        pass

    def step_back(self):
        pass

    def cancel_lookback(self):
        self.stack.reset()

    def end(self):
        self.running = False
