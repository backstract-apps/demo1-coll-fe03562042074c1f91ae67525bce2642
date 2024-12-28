from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - demo1-coll-fe03562042074c1f91ae67525bce2642',debug=False,docs_url='/great-cannon-2be822bcc50111efa0a50242ac12000568/docs',openapi_url='/great-cannon-2be822bcc50111efa0a50242ac12000568/openapi.json')

app.include_router(router, prefix='/great-cannon-2be822bcc50111efa0a50242ac12000568/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()