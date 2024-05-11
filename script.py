def my_decorator(arg):
    def _my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"デコレータの引数：{arg}")
            print("処理前")
            result = func(*args, **kwargs)
            print("処理後")
            return result
        return wrapper

    return _my_decorator


@my_decorator("abcd")
def add(x, y):
    print(x + y)


add(1, 6)

print(add.__name__)
