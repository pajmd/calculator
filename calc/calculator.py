from .tokeniser import tokenize
from .infixrpn import infix_to_rpn
from .evaluator import evaluate_rpn


# https://en.wikipedia.org/wiki/Operator_(computer_programming)
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# https://en.wikipedia.org/wiki/Reverse_Polish_notation


def calculate(expression):
    token_list = tokenize(expression)
    output_queue_to_evaluate = infix_to_rpn(token_list)
    grand_total = evaluate_rpn(output_queue_to_evaluate)
    return grand_total
