from fastapi import APIRouter

router = APIRouter()

@router.put("/tasks/{task_id}/done")
async def mark_done(task_id: int):
  return

@router.delete("/tasks/{task_id}/done")
async def unmark_done(task_id: int):
  pass