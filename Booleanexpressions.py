def true_func():
    print("true_func()")
    return True

def false_func():
    print("false_func()")
    return False
   
    true_func() or false_func()
    true_func()

    false_func() or true_func()
    false_func()
    true_func()
    true_func() and false_func()
    true_func()
    false_func()

    false_func() and false_func()
    false_func()

