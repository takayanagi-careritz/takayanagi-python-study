from fastapi import (
    FastAPI,
)
from api.routers import (
    tasks,
    done,
)  # src下からパス指定、勝手にエクスポートしてくれてるらしい

app = FastAPI()
app.include_router(tasks.router) # appインスタンスにルートを登録
app.include_router(done.router)
