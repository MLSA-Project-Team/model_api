# Import necessary modules
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define your endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run the application using the uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)