def min_remove_to_make_valid(s):
    # s is a string of lowercase letters, '(' and ')'
    # Return a valid string after removing the fewest parentheses
    # strategy: use stack to keep track of open '(', 
    # when a closing ')' found, match with top '('
    # else, remove the closing ')'
    # join the remaining chars for the final string 
    chars = list(s)
    opens = []
    for i, char in enumerate(chars):
        if char == '(':
            opens.append(i)
        elif char == ')':
            if opens:
                opens.pop()
            else:
                chars[i] = ''

    for i in opens:
        chars[i] = ''
    
    return ''.join(chars)

