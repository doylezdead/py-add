import shutil


class OperationsStack():
    head_node = None
    step_node = head_node

    def push(self, op=' ', val=0, result=0):
        self.head_node = StackNode(prev_node=self.head_node, op=op, val=val, result=result)
        self.step_node = self.head_node

    def get_current_val(self):
        return self.step_node.result

    def step_back(self):
        self.step_node = self.step_node.prev_node

    def revert_to(self):
        self.head_node = self.step_node

    def reset(self):
        self.step_node = self.head_node

    # I call it "formatting hell"
    def print_tape(self, buffer=0, width=-1, length=-1, step=False, border=False):
        current_node = self.head_node
        printout = ''
        prefix = ' '*buffer
        suffix = ''
        if border and (width==-1):
            border = False
        if border:

            prefix += '| '
            suffix = '|'


        while current_node is not None:
            indicator = ' '
            if current_node is self.step_node:
                indicator = '>'
            temp = '{0} {1}'.format(indicator, current_node)
            if border and ((len(temp) + 5) > width):
                print(width-3-2-2)
                temp = temp[0:(width-3-2-2)] + '..'

            printout = '{0}{1}{2}{3}\n'.format(prefix, temp, ' '*(width-3-len(temp)), suffix) + printout

            current_node = current_node.prev_node

        result = '{}'.format(self.step_node.result)
        if len(result)+6 > width:
            result = result[0:(width-6-2)] + '..'

        if border:
            printout = ' '*buffer + '-'*width + '\n' + printout + ' '*buffer + '-'*width + '\n' + ' '*buffer + '|    ' + result + '{}|\n'.format(' '*(width-len(result)-6)) + ' '*buffer + '-'*width

        return printout


class StackNode():
    prev_node = None
    op = ' '
    val = 0
    result = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        if self.result is None:
            self.result = self.val

    def __str__(self):
        retstr = '{0}{1}'.format(self.op,self.val)
        # if self.result is not None:
        #    retstr += ' = {}'.format(self.result)
        return retstr

    def __repr__(self):
        return self.__str__()


def get_size():
    sizes = shutil.get_terminal_size()
    return sizes.columns, sizes.lines
