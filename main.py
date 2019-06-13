from turing import turing_machine

print(
    'Welcome to Turing Machine. Go to machine.txt file and enter your machine rules. There will be an example of how the rules should be entered.')
q = int(input('If you need more information to how the rules should be entered, input 1, 0 otherwise.\n'))

if q == 1:
    print('The first line of the file should be the string you want to operate.')
    print('All following lines are rules. Each line is separate rule.')
    print('Each rule contains two parts that are divided with ->')
    print(
        "First part contains current state and current letter for the rule to take place. They are separated by ',' and no spaces.")
    print(
        "Second part contains letter to write on the current position, where to move the machine (L-left, R-right, H-stay) and the state to switch to.")
    print('Blank characters are represented as spaces so make sure to use spaces only when needed.')
    exit()

f = open('machine.txt', 'r')
string = f.readline().strip()
states = dict()
for line in f:
    left = line.split('->')[0]
    right = line.split('->')[1]
    states[tuple(left.split(','))] = list(right.replace('\n', '').split(','))
f.close()

print(string, '--->', turing_machine(states, string))
