from test_framework import generic_test


def evaluate(expression: str) -> int:
    # stack: List[int] = []
    stack = [int]
    operators = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y,
        '*': lambda y, x: x * y, '/': lambda y, x: x // y
    }

    delimiter = ','
    for val in expression.split(delimiter):
        if val in operators:
            stack.append(operators[val](
                stack.pop(), stack.pop()))
        else:
            stack.append(int(val))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
