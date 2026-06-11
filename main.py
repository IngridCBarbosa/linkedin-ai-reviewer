from fastapi import FastAPI, Depends

from api.dependencies.auth import get_current_user

app = FastAPI(
    title="LinkedIn AI Reviewer",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "LinkedIn AI Reviewer API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/protected")
def protected_route(
    user=Depends(get_current_user)
):
    return {
        "message": "Access granted",
        "user": user
    }