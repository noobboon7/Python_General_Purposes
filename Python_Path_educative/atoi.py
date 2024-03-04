def myAtoi(s):
    result = '0'
    cln_str = s.lstrip()
    pos_neg_val = -1 if cln_str[0] == '-' else 1
    for char in cln_str:
        if len(result) <= 32:
            if char == '+' or char == '-':
                continue
            elif not char.isdigit():
                break
            else:
                result += char
    return (int(result) * pos_neg_val)


print(myAtoi("97 and 79")) #97