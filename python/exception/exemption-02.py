def example_function(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError as e:
        print("Caught a FileNotFoundError:", e) 
    except Exception as e:
        print("Caught a general exception:", e) 
    else:
        f.close()

example_function("file.txt")