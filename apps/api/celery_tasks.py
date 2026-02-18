from celery import Celery
from services.ai_service import generate_ai_fix
from services.github_service import create_pr
from core.db import get_db_session
from ai_engine.copilot_agent import CopilotAgent

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def process_scan_results(org_id, raw_scan_results):
    """
    Normalize scan results, generate AI PR fixes, and optionally push to GitHub
    """
    agent = CopilotAgent(org_id)
    patches = agent.process_scan_results(raw_scan_results)
    
    # Example: store patches in DB
    db = get_db_session()
    for patch in patches:
        db.add_patch(org_id, patch)  # pseudo code
        # Optionally create PR
        # create_pr(org_id, patch)
    db.commit()
    return {"status": "completed", "patches_generated": len(patches)}
