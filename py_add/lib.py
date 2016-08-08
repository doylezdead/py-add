import shutil


class OperationsStack():
    head_node = None
    step_node = head_node

    def push(self, op='', val=0, result=0):
        head_node = StackNode(next_node=self.head_node, op=op, val=val)
        step_node = head_node

    def get_current_val(self):
        return self.step_node.result

    def step_back(self):
        self.step_node = self.step_node.prev_node

    def revert_to(self):
        self.head_node = self.step_node

    def reset(self):
        self.step_node = self.head_node

    def print_tape(self, width=-1, length=-1, step=False, border=False):
        current_node = self.head_node
        printout = ''
        prefix = ''
        if border and (width==-1):
            border = False
        if border:
            printout = '='*width + '\n'
            prefix = '| '
            suffix = '  |'
        while current_node is not None:
            indicator = ' '
            if current_node is self.step_node:
                indicator = '>'
            temp = ''
            temp = '{0}{1}'.format(indicator, current_node)
            if (temp + 6) > width:
                temp = temp[0:-3] + '...'

            printout = '{0}{1}{2}\n'.format(prefix,temp,suffix)

            current_node = current_node.prev_node

        if border: printout += '='*width
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
        retstr = '{0}{1}'.format(( self.op + ' '*(2-len(self.op)) ),self.val)
        # if self.result is not None:
        #    retstr += ' = {}'.format(self.result)
        return retstr

    def __repr__(self):
        return self.__str__()


def get_size():
    sizes = shutil.get_terminal_size()
    return sizes.columns, sizes.lines
