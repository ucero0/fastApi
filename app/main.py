from fastapi import FastAPI
from .db.session import engine
from .api.models import user as apiUserModels
from .api.routes.user import userRoute
app = FastAPI()
# create tables
apiUserModels.Base.metadata.create_all(bind=engine)

app.include_router(userRoute)
@app.get("/")
async def read_root():
    return {"Hello": "World"}

