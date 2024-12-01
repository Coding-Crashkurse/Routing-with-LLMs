from fastapi import FastAPI, HTTPException
from typing import List, Dict
from langchain_core.documents import Document
from pydantic import BaseModel


class DocumentResponse(BaseModel):
    page_content: str


app = FastAPI()

users_data: Dict[str, Dict] = {
    "john_doe": {
        "full_name": "John Doe",
        "documents": [
            Document(page_content="John's first document."),
            Document(page_content="John's second document."),
        ],
    },
    "jane_smith": {
        "full_name": "Jane Smith",
        "documents": [
            Document(page_content="Jane's first document."),
            Document(page_content="Jane's second document."),
        ],
    },
}


@app.get("/users")
async def list_users():
    return [
        {"username": key, "full_name": user["full_name"]}
        for key, user in users_data.items()
    ]


@app.get("/users/{full_name}/documents", response_model=List[DocumentResponse])
async def get_user_documents(full_name: str):
    user_key = next(
        (
            key
            for key, user in users_data.items()
            if user["full_name"].lower() == full_name.lower()
        ),
        None,
    )
    if not user_key:
        raise HTTPException(
            status_code=404,
            detail=f"User with full name '{full_name}' not found or no documents available.",
        )
    return users_data[user_key]["documents"]


@app.get("/users/{username}/last_name")
async def get_last_name(username: str) -> str:
    user = users_data.get(username.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    last_name = user["full_name"].split()[-1]
    return {"last_name": last_name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
