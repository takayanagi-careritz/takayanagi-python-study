# 接続確認: docker exec -it my-python-app_devcontainer-db-1 mysql demo

# エンジン: データベースに対してクエリを送信し、結果を受け取るための処理を行う
from sqlalchemy import create_engine
# セッション: 接続を管理する一時的な場
# declarative_base: テーブルのベースとなるクラスを提供
from sqlalchemy.orm import sessionmaker, declarative_base


# "mysql+ドライバ名://ユーザ名@ホスト名:ポート/DB名?文字コード等オプション"
DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8mb4"

# echo=Trueにてコンソールにクエリが出る
db_engine = create_engine(DB_URL, echo=True)

# autocommit=Falseで明示的にコミットできる
# フラッシュ: コミットする前にコミットできるかの確認
# bind=db_engineで接続エンジン指定
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

# セッションを取得（こいつでDBアクセスする）
# with文: 処理終わったら接続を閉じてくれる
# yield: 一時的なリターン
def get_db():
  with db_session() as session:
    yield session

# with文ってこんな風にも使う
# with open("file.txt") as file:
#     content = file.read()
