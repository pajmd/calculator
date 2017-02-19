

def evaluate_rpn(output_queue):
    """evaluates the output queue

    :rtype: Token
    """
    stack = []
    for token in output_queue:
        if token.is_number() is True or token.is_argument():
            stack.append(token)
        elif token.is_separator():
            continue
        else:
            arity = token.val.arity
            args = []
            while arity > 0:
                args.append(stack.pop())
                arity -= 1
            args.reverse()
            targs = tuple(args)
            # check the assiciativity
            stack.append(token.val.calculate(*targs))

    return stack[0]
