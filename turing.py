def turing_machine(states, string):
    """
    Does main loop, changing given string following given rules
    :param states: dictionary
    :param string: string
    :return: string
    """
    curr_state = 'q1'
    curr_position = 0

    while curr_state != 'q0':
        if curr_position == -1:
            curr_position = 0
            string = ' ' + string
        try:
            curr_char = string[curr_position]
        except IndexError:
            string += ' '
            curr_char = string[curr_position]

        change_rules = states[curr_state, curr_char]
        string = replace_str(string, curr_position, change_rules[0])
        curr_position = move_position(curr_position, change_rules[1])
        curr_state = change_rules[2]

    return string


def replace_str(string, pos, char):
    """
    Replaces character in the given position in a string
    :param string: string
    :param pos: integer
    :param char: string
    :return: string
    """
    lst = list(string)
    lst[pos] = char
    return "".join(lst)


def move_position(current, rule):
    """
    Moves current position of a machine following the given rule
    :param current: integer
    :param rule: string
    :return: integer
    """
    if rule != 'H':
        current = current + 1 if rule == 'R' else current - 1
    return current
