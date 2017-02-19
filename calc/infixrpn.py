from .error_locator import locate_error


def infix_to_rpn(tokens):
    output_stack = []
    output_queue = []
    token_count = 0

    for token in tokens:
        if token.is_number() is True or token.is_argument():
            output_queue.append(token)
        else:
            output_stack_len = len(output_stack)
            if token.is_left_parenthesis():
                output_stack.append(token)
            elif token.is_separator():
                left_parenthesis_found = False
                stack_len = len(output_stack)
                while stack_len > 0:
                    if output_stack[stack_len - 1].is_left_parenthesis():
                        left_parenthesis_found = True
                        break
                    else:
                        output_queue.append(output_stack.pop())
                        stack_len -= 1
                if left_parenthesis_found is False:
                    raise SyntaxError('separator misplaced or parentheses mismatched: ' +
                                      locate_error(tokens, token_count))
            elif token.is_right_parenthesis():
                left_parenthesis_found = False
                while len(output_stack) != 0:
                    pop_tkn = output_stack.pop()
                    if pop_tkn.is_left_parenthesis():
                        left_parenthesis_found = True
                        break
                    output_queue.append(pop_tkn)

                if left_parenthesis_found is False:
                    raise

                stack_left_len = len(output_stack)
                if stack_left_len != 0 and output_stack[stack_left_len - 1].is_function() is True:
                    output_queue.append(output_stack.pop())
            elif output_stack_len != 0:
                while output_stack_len != 0 and \
                                token.get_precedence() <= output_stack[output_stack_len - 1].get_precedence():
                    popped = output_stack.pop()
                    output_stack_len -= 1
                    output_queue.append(popped)

                output_stack.append(token)
            else:
                output_stack.append(token)
        token_count += 1

    while len(output_stack) != 0:
        output_queue.append(output_stack.pop())

    return output_queue
