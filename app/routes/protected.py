from fastapi import APIRouter, Depends, HTTPException
from jose import JWTError, jwt
from app.routes.auth import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/protected", tags=["Protected"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/dashboard")
def get_dashboard_data(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": f"Welcome to your dashboard, {username}!"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
