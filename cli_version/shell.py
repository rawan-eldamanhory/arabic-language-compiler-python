import dcode

while True:
    text = input('اساسي > ')
    result, error = dcode.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
    