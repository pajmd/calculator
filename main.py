from calc.tokeniser import tokenize
from calc.infixrpn import infix_to_rpn
from calc.evaluator import evaluate_rpn


if __name__ == '__main__':
    # print('calculating 9+24/(7-3)+max(100,200)')
    print('calculating 9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5)')
    # test case when last ) is missing
#    tokens_res = tokenize('9+24/(7-3)+max(100,sum(200,100))')
    tokens_res = tokenize('9+24/(7-3)+max(100,sum(200,100))+sum(1,2,3,4,5)')
    print('Token list: {}'.format(tokens_res))
    output_queue_res = infix_to_rpn(tokens_res)
    print('Output queue: {}'.format(output_queue_res))
    total = evaluate_rpn(output_queue_res)
    print(total)
