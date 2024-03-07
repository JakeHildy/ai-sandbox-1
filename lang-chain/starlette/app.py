from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route

async def homepage(request):
    return PlainTextResponse('Hello, world!')

async def user_info(request):
    data = {"name": "John Doe", "age": 30}
    return JSONResponse(data)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/user', user_info),
])
