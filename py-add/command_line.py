import colors
import py-add.lib as addlib
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
        self.control_actions = {
            'q': self.end,
            'w': self.write,
            'r': self.revert,
            '[': self.step_back,
            ']': self.cancel_lookback
        }

        self.op_actions = {
            '+': self.op_add,
            '-': self.op_sub,
            '*': self.op_mult,
            '/': self.op_div,
        }

        #start setting up terminal
        sys.stdout.write('\n'*self.height)
        sys.stdout.flush()


    def run(self):
        count = 0;
        self.stack.push(val=0)
        #self.stack.push(op='+', val=100, result=200)
        #self.stack.push(op='+', val=100, result=300)
        #self.stack.push(op='+', val=100, result=400)
        #self.stack.push(op='+', val=1000, result=1400)
        #self.stack.push(op='-', val=100, result=1300)
        #self.stack.push(op='+', val=100, result=1400)



        while self.running:
            new_out = self.stack.print_tape(buffer=2, width=self.width - 4, border=True)
            num_lines = len(new_out.split('\n'))
            sys.stdout.write(UP*(num_lines+2) + new_out + '\n')
            sys.stdout.write('  ' + '=' * (self.width - 4) + '\n\n  ' + '=' * (self.width - 4) + '{}\r'.format(UP))
            sys.stdout.write(' ' * self.width + '\r  >{}> '.format(count))
            sys.stdout.flush()
            input_str = input()
            count+=1

            self.parse_in(input_str)

        sys.stdout.flush()
        print('\n\nThank you for your patronage')
        return 0

    def parse_in(self, in_str):
        try:
            if in_str[0] in self.control_actions:
                self.control_actions[in_str[0]]()

            elif in_str[0] in self.op_actions:
               self.op_actions[in_str[0]](float(in_str[1:]))
            else:
                self.op_add(float(in_str))
        except Exception:
            pass

    def op_add(self, input_val):
        self.stack.push(op='+', val=input_val, result=self.stack.get_current_val()+input_val)

    def op_sub(self, input_val):
        self.stack.push(op='-', val=input_val, result=self.stack.get_current_val()-input_val)

    def op_mult(self, input_val):
        self.stack.push(op='x', val=input_val, result=self.stack.get_current_val()*input_val)

    def op_div(self, input_val):
        self.stack.push(op='/', val=input_val, result=self.stack.get_current_val()/input_val)


    def write(self):
        pass

    def step_back(self):
        self.stack.step_back()

    def revert(self):
        self.stack.revert_to()
        sys.stdout.write(UP*(self.height-4) + (' '*self.width + '\n') * (self.height-2))
        sys.stdout.flush()

    def cancel_lookback(self):
        self.stack.reset()

    def end(self):
        self.running = False
