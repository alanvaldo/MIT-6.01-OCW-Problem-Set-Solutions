class SM():
    def start(self):
        self.state = self.startState
        
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

##################################
# First Word SM
##################################

# Test 1
test1 = '''hi
ho'''
# This can also be writtent as:
# test1 = 'hi\nho'

#Test 2
test2 = '''  hi
ho'''
# This can also be writtent as:
# test2 = '  hi\nho'

#Test 3
test3  = '''

 hi
 ho ho ho

 ha ha ha'''
# This can also be writtent as:
# test3 ='\n\n hi \nho ho ho\n\n ha ha ha'

class FirstWordSM(SM):
    startState = 'FW' # Finding word

    def getNextValues(self, state, inp):
        isNLorSpace = (inp == '\n' or inp == ' ')
        if state == 'FW' and isNLorSpace:
            return ('FW', None) # FW = Finding word
        elif state == 'FW' and not isNLorSpace:
            return ('R', inp) # R = Read
        elif state == 'R' and not isNLorSpace:
            return ('R', inp) 
        elif state == 'R' and inp == ' ':
            return ('W', None) # W = Wait
        elif state == 'W' and inp != '\n':
            return ('W', None)
        else:
            return ('FW', None)

def runTestsFW():
    m = FirstWordSM()
    print 'Test1:', m.transduce(test1)
    print 'Test2:', m.transduce(test2)
    print 'Test3:', m.transduce(test3)
    m = FirstWordSM()
    m.start()
    [m.getNextValues(m.state, i) for i in '\nFoo ']
    print 'Test 4', [m.step(i) for i in test1]

# execute runTestsFW() to carry out the testing, you should get:

#Test1: ['h', 'i', None, 'h', 'o']
#Test2: [None, None, 'h', 'i', None, 'h', 'o']
#Test3: [None, None, None, 'h', 'i', None, None, 'h', 'o', None, None, None, None, None, None, None, None, None, 'h', 'a', None, None, None, None, None, None]
#Test4: ['h', 'i', None, 'h', 'o']

runTestsFW()
