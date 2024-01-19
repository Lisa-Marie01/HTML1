from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class UserProfiles(BaseModel):
    username: str
    email: str
    age: int
    bio: str

profiles:list[UserProfiles] = []

app = FastAPI()

@app.get("/profiles")
def get_profiles():
    return profiles

@app.put("/profiles")
def add_profile(profile):
    profiles.append(profile)
    return profile

@app.patch("/profiles")
def patch_profiles():
    return profiles

def get_single_profile(username: str):
    profile = get_profile_by_username(username)
    if profile:
        return profile

def get_profile_by_username(username: str):
    for profile in profiles:
        if profile.username == username:
            return profile
    return None

def main():
    import uvicorn
    uvicorn.run(app=app,host="localhost",port=8000)
    print ("Hello Friends, main()")

if __name__ == "__main__":
    main()
