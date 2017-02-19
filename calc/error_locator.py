

def locate_error(tokens, token_count):
    err = tokens[:token_count]
    err.append('>')
    err.append(tokens[token_count])
    err.append('<')
    err.extend(tokens[(token_count+1):])
    return ''.join(err)
