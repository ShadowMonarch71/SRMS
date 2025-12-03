import json
import os
from datetime import datetime
import bcrypt
from getpass import getpass
from typing import List,Dict
import shutil
import tempfile

# json helper function

USER_FILE="users.json" 

def read_json_file(path:str):
    if not os.path.exists(path):
        return []
    with open(path,"r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# user helper functions

def find_user(username:str,users:List[Dict]):
    for user in users:
        if user.get("username")==username:
            return user
        return None
    
def hash_pass(password:str)->str:
    return bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

def verify_pass(password:str,hashed:str)->bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"),hashed.encode("utf-8"))
    except ValueError:
        return False