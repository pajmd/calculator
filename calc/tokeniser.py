from .operators import operators
from .operator import Operator
from .token_items import TokenNum
from .token_items import TokenOp
from .token_items import TokenArg
from .tokens import Tokens


def get_operator(op):
    if op in operators:
        return operators[op]
    return None


def push_previous_token_if_argument_to_function_stack(tokens, function_stack):
    len_tokens = len(tokens)
    if len_tokens - 1 > 0:  # (
        if tokens[len_tokens - 2].is_argument():
            # make it a function
            function_operator = Operator(name=tokens[len_tokens - 2].val,
                                         precedence=2, arity=0,
                                         associativity='L',
                                         calculate=None, function='Y')
            tokens[len_tokens - 2].argument_to_function(function_operator)
            function_stack.append(tokens[len_tokens - 2])
            return True
    return False


def parse_back(tokens):
    len_tokens = len(tokens)
    counter = 0
    if len_tokens > 0:
        while len_tokens > 0:
            len_tokens -= 1
            if tokens[len_tokens].is_left_parenthesis() is True:
                counter -= 1
                if counter == 0:
                    if len_tokens - 1 >= 0 and tokens[len_tokens - 1].is_function():
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
    tokens = Tokens()
    function_stack = []
    is_building_argument = False
    building_function_arity = 0
    building_argument = ''

    for c in infix_expression:
        if str.isdigit(c):
            if len(tokens) != 0 and (tokens.is_last_token_number() is True or
                                             tokens.is_last_token_argument() is True):
                tokens.last_token_concatenate_value(c)
            else:
                tokens.append(TokenNum(c))
        elif c == '.':
            if len(tokens) != 0 and tokens.is_last_token_number() is True:
                tokens.last_token_concatenate_value(c)
            else:
                tokens.append(TokenNum('0.'))
        elif c in [' ', '\t']:
            continue
        else:
            operator = get_operator(c)
            if operator is not None:
                is_building_argument = False
                building_argument = ''
                tokens.append(TokenOp(operators[c]))
                if operators[c].name == '(':
                    # if token before ( is a function push it on function stack to determine arity later
                    push_previous_token_if_argument_to_function_stack(tokens, function_stack)
                    #    is_building_argument = False
                    #    building_argument = ''
                    building_function_arity = 0  # check no longer needed
                elif operators[c].name == ',':  # check no longer needed
                    building_function_arity += 1  # check no longer needed
                elif operators[c].name == ')':
                    # look for the previous (, if just before this ( there is a function, set the attributes of the function
                    tok = parse_back(tokens)
                    if tok.is_function() is True:
                        set_token_attriutes(tok, tokens)
                elif is_building_argument is True:
                    # while building a function we can only get a number, a ( or a )
                    raise SyntaxError('Error builing argument/function: ' + building_argument + '>' + c + '<')
            else:
                # if len(tokens) != 0 and tokens[len(tokens) - 1].is_function() is True:
                #     tokens[len(tokens) - 1].val.name += c
                #     building_function_name = tokens[len(tokens) - 1].val.name
                # else:
                #     building_function = True
                #     building_function_name = c
                #     function_operator = Operator(name=c, precedence=2, arity=0, associativity='L', calculate=None, function='Y')
                #     tokens.append(TokenOp(function_operator))
                if len(tokens) != 0 and tokens.is_last_token_argument() is True:
                    tokens.last_token_concatenate_value(c)
                    building_argument = tokens.last_token_value()
                else:
                    is_building_argument = True
                    building_argument = c
                    tokens.append(TokenArg(building_argument))

    return tokens
