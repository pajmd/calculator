from .token_items import Token
from .token_items import TokenNum
from .token_items import TokenOp
from .operators import operators
from .operator import Operator


def get_operator(op):
    if op in operators:
        return operators[op]
    return None


def push_previous_token_if_function_to_function_stack(tokens, function_stack):
    len_tokens = len(tokens)
    if len_tokens - 1 > 0:  # (
        if tokens[len_tokens - 2].is_function():
            function_stack.append(tokens[len_tokens - 2])


def parse_back(tokens):
    len_tokens = len(tokens)
    counter = 0
    if len_tokens > 0:
        while len_tokens > 0:
            len_tokens -= 1
            if tokens[len_tokens].is_left_parenthesis() is True:
                counter -= 1
                if counter == 0:
                    if len_tokens - 1 > 0 and tokens[len_tokens - 1].is_function():
                        return tokens[len_tokens - 1]
                    else:
                        return tokens[len_tokens]
            elif tokens[len_tokens].is_right_parenthesis() is True:
                counter += 1
        if counter != 0:
            raise SyntaxError('Mathincg parenthesis')
    else:
        raise SyntaxError('Mathincg parenthesis')


def set_token_attriutes(tok, tokens):
    tok.val.precedence = operators[tok.val.name].precedence
    tok.val.calculate = operators[tok.val.name].calculate
    arity = 1  # a function has at least one argument
    undetermine_arity = True
    # for arity count , only when the level of parenthesis is 1
    index = len(tokens) - 1
    while index >= 0:
        if tok == tokens[index]:
            count = 0
            i = index
            while i < len(tokens):
                if tokens[i].is_left_parenthesis() is True:
                    count += 1
                elif tokens[i].is_right_parenthesis() is True:
                    count -= 1
                    if count == 0:
                        undetermine_arity = False  # test not valid if function with one param
                elif count == 1 and tokens[i].is_separator() is True:
                    arity += 1
                i += 1
            break
        index -= 1
    if undetermine_arity is True:
        raise SyntaxError('Mathincg parenthesis, or comma impossible to set arity function: ' + tok.val.name)
    tok.val.arity = arity


def tokenize(infix_expression):
    tokens = []
    function_stack = []
    building_function = False
    building_function_arity = 0
    building_function_name = ''

    for c in infix_expression:
        if str.isdigit(c):
            if len(tokens) != 0 and tokens[len(tokens) - 1].is_number() is True:
                tokens[len(tokens) - 1].val += c
            else:
                tokens.append(TokenNum(c))
        elif c == '.':
            if len(tokens) != 0 and tokens[len(tokens) - 1].is_number() is True:
                tokens[len(tokens) - 1].val += c
            else:
                tokens.append(TokenNum('0.'))
        elif c in [' ', '\t']:
            continue
        else:
            operator = get_operator(c)
            if operator is not None:
                tokens.append(TokenOp(operators[c]))
                if operators[c].name == '(':
                    # if token before ( is a function push it on function stack to determine arity later
                    push_previous_token_if_function_to_function_stack(tokens, function_stack)
                    building_function_arity = 0
                elif operators[c].name == ',':
                    building_function_arity += 1
                elif operators[c].name == ')':
                    # look for the previous (, if just before this ( there is a function, set the attributes of the function
                    tok = parse_back(tokens)
                    if tok.is_function() is True:
                        set_token_attriutes(tok, tokens)
                elif building_function is True:
                    # while building a function we can only get a number, a ( or a )
                    raise SyntaxError('Syntax error builing function: ' + building_function_name)
            else:
                if len(tokens) != 0 and tokens[len(tokens) - 1].is_function() is True:
                    tokens[len(tokens) - 1].val.name += c
                    building_function_name = tokens[len(tokens) - 1].val.name
                else:
                    building_function = True
                    building_function_name = c
                    function_operator = Operator(name=c, precedence=2, arity=0, associativity='L', calculate=None, function='Y')
                    tokens.append(TokenOp(function_operator))

    return tokens


def locate_error(tokens, token_count):
    err = tokens[:token_count]
    err.append('>')
    err.append(tokens[token_count])
    err.append('<')
    err.extend(tokens[(token_count+1):])
    return ''.join(err)


def infix_to_rpn(tokens):
    output_stack = []
    output_queue = []
    token_count = 0

    for token in tokens:
        if token.is_number() is True:
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
                for tkn in output_stack:
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


# https://en.wikipedia.org/wiki/Operator_(computer_programming)
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
def evaluate_rpn(output_queue):
    """evaluates the output queue

    :rtype: Token
    """
    stack = []
    for token in output_queue:
        if token.is_number() is True:
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


def calculate(expression):
    token_list = tokenize(expression)
    output_queue_to_evaluate = infix_to_rpn(token_list)
    grand_total = evaluate_rpn(output_queue_to_evaluate)
    return grand_total

if __name__ == '__main__':
    # print('calculating 9+24/(7-3)+max(100,200)')
    print('calculating 9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5)')
    # test case when last ) is missing
    tokens_res = tokenize('9+24/(7-3)+max(100,sum(200,100))')
    print('Token list: {}'.format(tokens_res))
    output_queue_res = infix_to_rpn(tokens_res)
    print('Output queue: {}'.format(output_queue_res))
    total = evaluate_rpn(output_queue_res)
    print(total)
