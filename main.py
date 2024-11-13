from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat_router, files_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chatitup.co"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router( chat_router.router, prefix='/chat', tags=['Chat'] )
app.include_router( files_router.router, prefix='/files', tags=['Files Upload'] )
# ==> Route for other azure resources ...