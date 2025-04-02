# Secure Banking System - Python Version using FastAPI

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib
import hmac
import uuid
import base64
import os
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory user DB
users = {}
shared_key = b'shared_secret'

class User(BaseModel):
    username: str
    password: str

class ActionRequest(BaseModel):
    username: str
    action: str
    amount: int = 0

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/audit-log")
def get_audit_log():
    if not os.path.exists("audit_log.txt"):
        return {"error": "No audit log found."}
    with open("audit_log.txt", "r") as f:
        log = f.readlines()
    return {"log": [entry.strip() for entry in log]}


@app.post("/register")
def register(user: User):
    if user.username in users:
        return {"error": "User exists"}
    users[user.username] = {"password": user.password, "balance": 1000}
    return {"message": "Registered"}


@app.post("/login")
def login(user: User):
    u = users.get(user.username)
    if not u or u["password"] != user.password:
        return {"error": "Invalid credentials"}
    nonce1 = uuid.uuid4().hex
    nonce2 = uuid.uuid4().hex
    master_secret = hmac_sha256(shared_key, (nonce1 + nonce2).encode())
    enc_key = hmac_sha256(master_secret, b"ENCRYPT")
    mac_key = hmac_sha256(master_secret, b"MAC")

    return {
        "message": "Authenticated",
        "nonce1": nonce1,
        "nonce2": nonce2,
        "encKey": base64.b64encode(enc_key).decode(),
        "macKey": base64.b64encode(mac_key).decode()
    }

@app.post("/action")
def action(req: ActionRequest):
    u = users.get(req.username)
    if not u:
        return {"error": "User not found"}

    if req.action == "deposit":
        u["balance"] += req.amount
    elif req.action == "withdraw":
        if u["balance"] >= req.amount:
            u["balance"] -= req.amount
        else:
            return {"error": "Insufficient funds"}
    elif req.action == "inquiry":
        pass
    else:
        return {"error": "Invalid action"}

    log_action(req.username, req.action)
    return {"balance": u["balance"]}

def hmac_sha256(key, message):
    return hmac.new(key, message, hashlib.sha256).digest()

def log_action(username, action):
    timestamp = datetime.now().isoformat()
    entry = f"{username} | {action} | {timestamp}\n"
    with open("audit_log.txt", "a") as f:
        f.write(entry)

# Run with: uvicorn secure_banking_app:app --reload
