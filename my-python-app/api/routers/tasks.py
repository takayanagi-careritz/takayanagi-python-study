from fastapi import APIRouter

router = APIRouter()  # インスタンス生成

@router.get("/tasks") # routerインスタンスのデコレータでルート登録
async def list_tasks(): # FastAPIの関数にはとりあえず脳死でasyncつける、つけないとエラーになる（awaitで待とうとするため）
  # ↑ 「list」って動詞的な扱いできるらしい、、、？
    pass
  
@router.post("/tasks")
async def create_task():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass
  
@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
  
# 勝手にエクスポートしてくれるらしい
