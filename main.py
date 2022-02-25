from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import uvicorn

app = FastAPI(
    title="FASTAPI Doc API"
)

#custom open API properties
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FASTAPI doc API",
        version="1.0.0",
        description="This is API documentation for FASTAPI doc API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

#set custom openapi
app.openapi = custom_openapi

#get API basic Hello World
@app.get("/")
async def index():
    response = get_base_response(200, "SUCCESS", "Success geting response", [{"Hello": "World"}])
    return response

def get_base_response(response_code, response_result, response_message, data):
    response = {
        "response_code": response_code,
        "response_result": response_result,
        "response_message": response_message,
        "data": data,
    }
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
