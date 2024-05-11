## 構文復習
### クラス
インスタンスで定義した変数はクラス変数を変更しているわけではない  
インスタンス変数を設けるときには、コンストラクタを使おう

### デコレータ
@で始まるやつ（@staticmethod）  
関数やクラスの前後に処理を追加する  
こいつ本質は関数やクラス → 関数を受け取り関数を返す関数   
シンタックスシュガーにすぎない   
自作してみる
ログ出す時とか

```py
def my_decorator(f):
    def wrapper(*args, **kw):
        print("処理前")
        # 引数をアンパック、kwは引数名指定して入れた時のもの（キーワード引数、argsは位置引数）
        f(*args, **kw)
        print("処理後")
        return

    return wrapper


@my_decorator
def add(x, y):
    print(x + y)


add(1, 2)
# >>> add(1, 2)
# 処理前
# 3
# 処理後
```

戻り値あってもいいように
```py
def my_decorator(f):
    def wrapper(*args, **kw):
        print("処理前")
        result = f(*args, **kw)
        print("処理後")
        return result

    return wrapper


@my_decorator
def add(x, y):
    return x + y


print(add(1, 2))
# >>> print(add(1, 2))
# 処理前
# 処理後
# 3
```

デコレータも引数受け取れる  
デコレータをさらにラップする
```py
def my_decorator(deco_arg):
    def _my_decorator(f):
        def wrapper(*args, **kw):
            print(f'デコレータの引数：{deco_arg}')
            
            print("処理前")
            result = f(*args, **kw)
            print("処理後")
            return result

        rを使うrn wrapper
    return _my_decorator


@my_decorator("こんにちは")
def add(x, y):
    return x + y


print(add(1, 2))
# >>> print(add(1, 2))
# デコレータの引数：こんにちは
# 処理前
# 処理後
# 3
```
ただこうするとaddのメタデータがおかしくなる
```py
print(add.__name__)
>>> print(add.__name__)
wrapper
```
ので別のデコレータを使う
```py
@functools.wraps(f)
        def wrapper(*args, **kw):
```

## Dockerを使う
### 利点
windows - mac の環境の差をなるたけ除ける  
のちにMySQLとか入れること考えてマシンを汚さずに済む  
バージョン管理が容易  

### Docker Desktop
便利さは知っているので割愛  
企業利用ではお金がかかるが、代替の無料GUIとして、「Rancher Desktop」がある ⇒ 動かしてるVMが違うらしい  
Dockerのバージョン1系と2系ではコマンドが変わる
1系はPython、2系はGoで作られていることに起因するらしい  
Windowsで使うときは改行コードを CRLF ⇒ LF に変えておくのを忘れない（VSCode、git）

docker-composeとDockerfileを作っていく
```
my-python-app
├ .dockerenv
├ docker-compose.yaml
└ Dockerfile
```