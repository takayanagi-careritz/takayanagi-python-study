## Fast API 試用してみる

<details>
<summary>main.py</summary>

```py
from fastapi import (
    FastAPI,
)  # インポート、実態は .venv/lib にある？、dockerenvはそれを参照してる？

app = FastAPI()


# FastAPIのデコレータ、「HTTPメソッド」と「パス」を定義
# これのおかげでSwaggerUI（http://localhost:8000/docs#/）で記述してくれる
@app.get("/hello")
async def hello():
    return {"message": "Hello World"} # デフォはjson返す

```
</details>

<br>

## REST API とは
ここでは以降の学習に困らない程度に簡単に  

エンドポイント（APIのURL）とHTTPメソッド（GET、PUT、POST、、、）を組み合わせてAPIを構成する方法

シンプルなので理解しやすく実装もしやすい

## FastAPIとは
これから学ぶ Fast API は REST API を実現するためのPythonのフレームワーク

早くて型安全でSwaggerUIも書いてくれる
  
FastAPIでは「パスオペレーション」という単語がでてくるが、パスはエンドポイント、オペレーションはHTTPメソッドを示すらしい  
なのでルーターでパスオペレーションを定義する感じ


次からは学習のために「ToDoアプリ」を作っていく
