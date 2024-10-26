from sqlalchemy.orm import Session

import api.schemas.tasks as task_schema
import api.models.task as task_model

# SQLAlchemyでは、Integer型のカラムが主キーとして設定されている場合、オートインクリメントの挙動がデフォルトで適用されるらしい
# ので、今回は id が無い task_model.Task 型の変数が一時的にできるし、db.refresh(task)で自動採番され取得される
def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
  task = task_model.Task(**task_create.model_dump()) # dict型にして展開
  db.add(task)
  db.commit()
  db.refresh(task) # DBからマッパー上のオブジェクトを最新化
  return task
  
  