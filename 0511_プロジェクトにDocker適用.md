## Dockerを使う
### 利点
- windows - mac の環境の差をなるたけ除ける  
- のちにMySQLとか入れること考えてマシンを汚さずに済む  
- バージョン管理が容易  

### Docker Desktop
便利さは知っているので割愛  
企業利用ではお金がかかるが、代替の無料GUIとして、「Rancher Desktop」がある ⇒ 動かしてるVMが違うらしい  

Dockerのバージョン1系と2系ではコマンドが変わる  
1系はPython、2系はGoで作られていることに起因するらしい  
Windowsで使うときは改行コードを CRLF ⇒ LF に変えておくのを忘れない（VSCode、git）

### 実践
docker-composeとDockerfileを作っていく  

<details>
<summary>docker-compose.yaml</summary>

```yaml
### docker-compose.yaml ###
# 一言でいうなら、コンテナ管理を設定

version: "3"
services:
  my-python-app:
    build: . # このディレクトリ内でDockerイメージをビルド
    # ↑ Dockerfileを呼び出してる！パスを明示でも行けるはず
    volumes: # ホストとコンテナのディレクトリのマウントを記述する箇所
      - .dockervenv:/src/.venv # ホストの.dockerenvをコンテナの/src/.venvにマウント
      # ↑ dockervenv⇒コンテナの環境設定系を記述、venv⇒Pythonプロジェクトの仮想環構成を記述
      - .:/src # カレントディレクトリを/srcにマウント
    ports:
      - "8000:8000" # ホストの8000をdockerの8000に接続
    environment: # 環境変数の設定場所
      - WATCHFILES_FORCE_POLLING=true # ホットリロード設定ON
```
</details>

<details>
<summary>Dockerfile</summary>

```dockerfile
### Dockerfile ###
# 一言でいうなら、コンテナの設計書
# こいつはこのファイル名でなくてはいけない！

# FROMで指定したDockerイメージを使う
# busterって安定板の意味らしい
FROM python:3.11-buster
# 実行結果がデフォだと貯めて出されるが、これでリアルタイムで出るらしい
ENV PYTHONBUFFERED=1

WORKDIR /src

# RUNはビルド時コマンドを実行する
# pipはPythonのパッケージ管理ツール、poetryもそう、これらとvenvとの違いがよくわからない、、、
# ↓ npm で yarn 入れる的なことをしてる？
RUN pip install poetry

# package.json と package-lock.jsonみたいな、これをカレントにコピー
COPY pyproject.toml* poetry.lock* ./

# 仮想環境をpoetryが作らないよう設定、Docker上だから要らない？
# venvはローカルで仮想環境が必要だから使う？
RUN poetry config virtualenvs.in-project true
# pyprojectがあるならインストール、fiは条件分岐を終わり
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# ENTRYPOINTは起動時コマンドを実行する、RUNはビルド時！こっちはコンテナ起動時！つまり毎回！
# poetry run uvicorn api.main:app --host 0.0.0.0 --reload
# uvicorn はAPIサーバーを立ち上げるためのもの、ASGI（Asynchronous Server Gateway Interface）：非同期サーバーゲートウェイインターフェース
# 深井さんが言っていたPythonでの非同期というやつ？
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
```
</details>

<br>

venvをマウントする.dockerenvを作成する  
```
my-python-app
├ .dockerenv
├ docker-compose.yaml
└ Dockerfile
```

イメージをビルドする  
パッケージを追加したら再ビルドを忘れない
```
docker compose build
```

上記を作成後は `pyproject.toml` が無いので initで作ってもらう  
Dockerイメージの中で poetry コマンドを実行
```shell
docker compose run --entrypoint "poetry init --name my-python-app --dependency fastapi --dependency uvicorn[standard]" my-python-app
```

パッケージインストール、.lockファイルも作られることを確認
```shell
docker compose run --entrypoint "poetry install --no-root" my-python-app
```

<br>

せっかくVSCode使っているので、Dev Conatainersで構築できるよう変更  
- Dev Containers：コンテナ立ち上げをVSCodeで行うツール  

vscodeの設定や拡張機能も、devcontainerで共通管理可能

<details>
<summary>devcontainer.json</summary>

```json
// devcontainer.json
{
  "name": "my-python-app",
  "dockerComposeFile": [
    "docker-compose.yaml"
  ],
  "service": "my-python-app",
  "workspaceFolder": "/src",
  "customizations": {
    "vscode": {
      "settings": {
        "[python]": {
          "editor.defaultFormatter": "ms-python.black-formatter"
        }
      },
      "extensions": [
        "MS-CEINTL.vscode-language-pack-ja",
        "ms-python.black-formatter",
        "KevinRose.vsc-python-indent",
        "formulahendry.code-runner",
        "mhutchie.git-graph",
        "eamodio.gitlens",
        "ms-python.vscode-pylance",
        "ms-python.python",
        "ms-python.debugpy",
        "Codeium.codeium"
      ]
    }
  }
}
```
</details>

<details>
<summary>docker-compose.yaml</summary>

```yaml
### docker-compose.yaml ###
# 一言でいうなら、コンテナ管理を設定

version: "3"
services:
  my-python-app:
    # build: . # このディレクトリ内でDockerイメージをビルド
    # # ↑ Dockerfileを呼び出してる！パスを明示でも行けるはず
    build:
      context: ../
      dockerfile: .devcontainer/Dockerfile

    volumes: # ホストとコンテナのディレクトリのマウントを記述する箇所
      - ../.dockervenv:/src/.venv # ホストの.dockerenvをコンテナの/src/.venvにマウント
      # ↑ dockervenv⇒コンテナの環境設定系を記述、venv⇒Pythonプロジェクトの仮想環構成を記述
      - ../:/src # カレントディレクトリを/srcにマウント
    ports:
      - "8000:8000" # ホストの8000をdockerの8000に接続
    environment: # 環境変数の設定場所
      - WATCHFILES_FORCE_POLLING=true # ホットリロード設定ON
```
</details>

<details>
<summary>Dockerfile</summary>

```dockerfile
### Dockerfile ###
# 一言でいうなら、コンテナの設計書
# こいつはこのファイル名でなくてはいけない！

# FROMで指定したDockerイメージを使う
# busterって安定板の意味らしい
FROM python:3.11-buster
# 実行結果がデフォだと貯めて出されるが、これでリアルタイムで出るらしい
ENV PYTHONBUFFERED=1

WORKDIR /src

# RUNはビルド時コマンドを実行する
# pipはPythonのパッケージ管理ツール、poetryもそう、これらとvenvとの違いがよくわからない、、、
# ⇒ pipはパッケージ管理をするもの、poetryはenv環境管理をするもの、venvは仮想環境を作成するもの
RUN pip install poetry

# package.json と package-lock.jsonみたいな、これをカレントにコピー
COPY pyproject.toml* poetry.lock* ./

# 仮想環境をpoetryが作らないよう設定、Docker上だから要らない？
# venvはローカルで仮想環境が必要だから使う？
RUN poetry config virtualenvs.in-project true
# pyprojectがあるならインストール、fiは条件分岐を終わり
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# ENTRYPOINTは起動時コマンドを実行する、RUNはビルド時！こっちはコンテナ起動時！つまり毎回！
# poetry run uvicorn api.main:app --host 0.0.0.0 --reload
# uvicorn はAPIサーバーを立ち上げるためのもの、ASGI（Asynchronous Server Gateway Interface）：非同期サーバーゲートウェイインターフェース
# 深井さんが言っていたPythonでの非同期というやつ？
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
```
</details>



<br>

このような感じになった
```
my-python-app
├ .dockerenv
└ .devcontainer
  ├ devcontainer.json
  ├ docker-compose.yaml
  └ Dockerfile
```
 
