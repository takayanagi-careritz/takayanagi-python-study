from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str | None = Field(None, example="○○をする")

class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int
    class Config:
        orm_mode = True

class TaskGetResponse(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
    class Config:
        orm_mode = True



# 古いPythonだとパイプが使えないので、Optional[str]と書くらしい