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