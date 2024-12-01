from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    user_input: str


@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.user_input
    if not user_input:
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    response_message = f"You said: {user_input}"
    return {"message": response_message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
