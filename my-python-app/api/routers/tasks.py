from fastapi import APIRouter
import api.schemas.tasks as task_schemas

router = APIRouter()  # インスタンス生成


# routerインスタンスのデコレータでルート登録
# FastAPIの関数にはとりあえず脳死でasyncつける、つけないとエラーになる（awaitで待とうとするため）
@router.get("/tasks", response_model=list[task_schemas.Task])
async def list_tasks():
    return [task_schemas.Task(id=1, title=123)]


# ↑「list」って英単語は動詞的な扱いできるらしい、、、？
# キーワード引数を使うことによって引数の順番を気にしなくていい


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
