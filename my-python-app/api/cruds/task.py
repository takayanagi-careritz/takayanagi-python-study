from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

import api.schemas.tasks as task_schema
import api.models.task as task_model


# SQLAlchemyでは、Integer型のカラムが主キーとして設定されている場合、オートインクリメントの挙動がデフォルトで適用されるらしい
# ので、今回は id が無い task_model.Task 型の変数が一時的にできるし、db.refresh(task)で自動採番され取得される
def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())  # dict型にして展開
    db.add(task)
    db.commit()
    db.refresh(task)  # DBからマッパー上のオブジェクトを最新化
    return task


def get_task_with_done(db: Session) -> list[tuple[int, str, bool]]:
    # resultのこの時点では値が入っていない、all()することで得られる
    result: Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            # task_model.Task.done,　# ← relationship は Python オブジェクト間の関連を表すだけでテーブルに存在するわけではない
            task_model.Done.id.isnot(None).label("done"),  # Doneの存在をbool値として取得
        ).outerjoin(task_model.Done)
    )
    return result.all()
