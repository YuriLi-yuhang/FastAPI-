# fast api 是什么?
# FastAPI 是一个现代、高性能的 Python Web 框架，用于构建 API。
# 核心特点:
# | 快速开发  类型提示驱动，IDE 补全友好  
# | 高性能    基于 Starlette（异步）+ Uvicorn，性能接近 Node.js / Go 
# | 自动文档  自动生成交互式文档（Swagger UI / ReDoc）
# | 数据校验  基于 Pydantic，请求/响应自动验证与序列化
# | 标准化    遵循 OpenAPI（原 Swagger）规范
# | 类型安全  充分利用 Python 类型提示，减少运行时错误



# 1. 安装虚拟环境
# 2. pip install fastapi




# fast api 基本路由

from fastapi import FastAPI

app = FastAPI()

@app.get("/items")        # GET 查询
def list_items():
    return [{"name": "苹果"}, {"name": "香蕉"}]

@app.post("/items")       # POST 创建
def create_item():
    return {"msg": "created"}

@app.put("/items/{item_id}")   # PUT 更新
def update_item(item_id: int):
    return {"item_id": item_id, "msg": "updated"}

@app.delete("/items/{item_id}")  # DELETE 删除
def delete_item(item_id: int):
    return {"msg": f"删除了 {item_id}"}