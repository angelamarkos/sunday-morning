def division(a, b):
    if a == 0 or b == 0:
        return 0
    return a/b


def hello():
    return 'Hello'



# assert division(1, 1) == 1, 'Should be 1'
# assert division(0, 1) == 0, 'Should be 0'
# assert division(1, 2) == 0.5, 'Should be 0.5'
#
# exception_message = ''
# try:
#     division(1, 0)
# except Exception as e:
#     exception_message = str(e)
# assert exception_message == 'division by zero'