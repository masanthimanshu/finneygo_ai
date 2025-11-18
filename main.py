from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Finneygo", version="1.0.0")

import routes
for route_name in routes.__all__:
    module = getattr(routes, route_name)
    app.include_router(module)

@app.get("/health")
async def health():
    return  {"message": "It's Working", "api_key": getenv("GOOGLE_API_KEY")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)
