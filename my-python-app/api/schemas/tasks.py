from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="○○をする")
    done: bool = Field(False, description="完了フラグ")


# 古いPythonだとパイプが使えないので、Optional[str]と書くらしい
