from fastapi import FastAPI
from .db.session import engine
from .api.models import user as apiUserModels
from .api.routes.user import userRoute
from .api.routes.auth import auth
app = FastAPI()
# create tables
apiUserModels.Base.metadata.create_all(bind=engine)

app.include_router(userRoute)
app.include_router(auth)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

