# api/dependencies/auth.py

from fastapi import Header, HTTPException


def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    return {
        "message": "authenticated"
    }