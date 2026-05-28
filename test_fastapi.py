from fastapi import FastAPI

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Membuat endpoint dasar (Root)
@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Wagwan!"
    }

# Endpoint tambahan untuk tes parameter
@app.get("/ping")
def ping_server():
    return {"ping": "pong!"}
