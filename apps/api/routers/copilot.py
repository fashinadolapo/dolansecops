from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import generate_ai_fix

router = APIRouter()

class FixRequest(BaseModel):
    repo_name: str
    file_path: str
    vulnerability: str

@router.post("/suggest_fix")
async def suggest_fix(request: FixRequest):
    ai_fix = generate_ai_fix(request.repo_name, request.file_path, request.vulnerability)
    return {"ai_fix": ai_fix, "repo": request.repo_name}
