from fastapi import APIRouter
import api.schemas.tasks as task_schemas

router = APIRouter()  # インスタンス生成


# routerインスタンスのデコレータでルート登録
# FastAPIの関数にはとりあえず脳死でasyncつける、つけないとエラーになる（awaitで待とうとするため）
@router.get("/tasks", response_model=list[task_schemas.TaskGetResponse])
async def list_tasks():
    # todo: DBから取得
    result = [task_schemas.TaskGetResponse(id=1, title="ダミーデータ")]
    return result


# ↑「list」って英単語は動詞的な扱いできるらしい、、、？
# キーワード引数を使うことによって引数の順番を気にしなくていい


@router.post("/tasks", response_model=task_schemas.TaskCreateResponse)
async def create_task(task_body: task_schemas.TaskCreate):
    # DBに保存
    result = task_schemas.TaskCreateResponse(
        id=1, **task_body.model_dump()  # 残余引数こう書ける
    )
    return result


# task_idについて、パスパラメータと引数の変数名を合わせることで関数内で使える
@router.put("/tasks/{task_id}", response_model=task_schemas.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schemas.TaskCreate):
    # DBに保存
    result = task_schemas.TaskCreateResponse(id=task_id, **task_body.model_dump())
    return result


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return
