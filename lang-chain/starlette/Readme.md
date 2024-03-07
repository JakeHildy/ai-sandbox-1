=== STARLETTE SERVER ===
pip install starlette uvicorn

```
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

async def homepage(request):
return PlainTextResponse('Hello, world!')

app = Starlette(debug=True, routes=[
Route('/', homepage),
])
```

uvicorn app:app --reload
