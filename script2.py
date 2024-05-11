def my_decorator(deco_arg):
    def _my_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print(f"デコレータの引数：{deco_arg}")

            print("処理前")
            result = f(*args, **kw)
            print("処理後")
            return result

        return wrapper

    return _my_decorator


@my_decorator("こんにちは")
def add(x, y):
    return x + y


print(add.__name__)
