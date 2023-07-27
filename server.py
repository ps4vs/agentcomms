import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agentfs:start_server", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
