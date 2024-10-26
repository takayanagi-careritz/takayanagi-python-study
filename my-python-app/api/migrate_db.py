# 実行方法：docker exec -it my-python-app_devcontainer-my-python-app-1 poetry run python -m api.migrate_db

from sqlalchemy import create_engine
from api.models.task import Base

# DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf=8" # これだとエンコーディングでエラー
DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8mb4" # utf8mb4 は、MySQLで完全なUTF-8互換の文字エンコーディング
# utf8は3バイト文字、utf8mb4は4バイト文字なので全部のUnicode文字を扱える

engine = create_engine(DB_URL, echo=True)


def reset_database():
    # bind=""でどのDBエンジンに操作するかを指定する
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


# 「if __name__ == "__main__"」は直接実行したときのみ処理が実行される（他の個所から呼び出したら__name__がモジュール名になるはずなので）
if __name__ == "__main__":
    reset_database()
