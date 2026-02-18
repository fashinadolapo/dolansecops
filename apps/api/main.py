from fastapi import FastAPI
from routers import auth, copilot, pr_fix, tenants
from websocket import manager
import uvicorn

app = FastAPI(title="DolanSecOps API")

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(copilot.router, prefix="/copilot")
app.include_router(pr_fix.router, prefix="/pr")
app.include_router(tenants.router, prefix="/tenants")

@app.on_event("startup")
async def startup_event():
    print("DolanSecOps API starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("DolanSecOps API shutting down...")

# WebSocket for real-time updates
from fastapi import WebSocket

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # just keep alive
    except:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
