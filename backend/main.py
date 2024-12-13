from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse, Response
import requests
import asyncio, json
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


origins = [
    "http://localhost:3000",  # React frontend
    "http://localhost:8000",  # FastAPI backend
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/inference/")
async def inference(prompt: str):
    print("prompt", prompt)
    url = "http://host.docker.internal:11434/api/generate"    # Replace URL for different llama deployment
    data = {
         "model": "llama3.1:8b", 
        "prompt": prompt
    }
    response = requests.post(url, json=data, stream=True)

    async def generate():
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk
    
    return StreamingResponse(generate(), media_type="text/plain")
            

@app.websocket("/ws/inference")
async def inference_websocket(websocket:WebSocket):
    
    await websocket.accept()
    try:
        prompt = await websocket.receive_text()
        print(f"Received prompt: {prompt}")

        url = "http://host.docker.internal:11434/api/generate"    # Replace URL for different llama deployment
        data = {
            "model": "llama3.1:8b", 
            "prompt": prompt
        }

        response = requests.post(url, json=data, stream=True)

        
        for chunk in response.iter_content(chunk_size=1024):
            res = json.loads(chunk)
            await websocket.send_text(res['response'])
            # await asyncio.sleep(1)
    except Exception as e:
        print(e)
    
    await websocket.close()



@app.get("/test")
async def test_connection():
    return Response(content="Connection working!")