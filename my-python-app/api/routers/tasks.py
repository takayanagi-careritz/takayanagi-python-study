from fastapi import APIRouter, Depends
import api.schemas.tasks as task_schemas
from sqlalchemy.orm import Session
from api.db import get_db
import api.cruds.task as task_crud

router = APIRouter()  # インスタンス生成


# routerインスタンスのデコレータでルート登録
# FastAPIの関数にはとりあえず脳死でasyncつける、つけないとエラーになる（awaitで待とうとするため）
@router.get("/tasks", response_model=list[task_schemas.TaskGetResponse])
async def list_tasks():
    # todo: DBから取得
    result = [task_schemas.TaskGetResponse(id=1, title="ダミーデータ")]
    return result

# Depends -> 噂のDI（依存性注入）、これをすることでテスト環境のDBセッションとかを入れられる
# 密結合すぎる状態を防いでる（＝依存性注入）
@router.post("/tasks", response_model=task_schemas.TaskCreateResponse)
async def create_task(task_body: task_schemas.TaskCreate, db: Session=Depends(get_db)):
    return task_crud.create_task(db, task_body)
    # 戻りの型は DBの型「task_model.Task」のはずなのに、スキーマの型「task_schemas.TaskCreateResponse」が返る
    # これは、task_schemas.TaskCreateResponseに「orm_mode = True」を付けたからである、不思議


# task_idについて、パスパラメータと引数の変数名を合わせることで関数内で使える
@router.put("/tasks/{task_id}", response_model=task_schemas.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schemas.TaskCreate):
    # DBに保存
    result = task_schemas.TaskCreateResponse(id=task_id, **task_body.model_dump())
    return result


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return
