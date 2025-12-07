x = "hello"

if isinstance(x, int):
    raise ValueError("x should be an integer")
else:
    print("x is an integer")