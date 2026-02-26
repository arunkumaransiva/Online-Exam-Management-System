import os
from online_exam.app import app, init_db, DATABASE

# ensure db is fresh
if os.path.exists(DATABASE):
    os.remove(DATABASE)

init_db()

with app.test_client() as client:
    r1 = client.post("/", data={"name":"Alice","email":"alice@example.com","password":"pass"}, follow_redirects=True)
    print("register status", r1.status_code)
    r2 = client.post("/login", data={"email":"alice@example.com","password":"pass"}, follow_redirects=True)
    print("login status", r2.status_code)
    r3 = client.get("/exam")
    print("exam status", r3.status_code)
    text = r3.data.decode('utf-8', 'ignore')
    print("exam content snippet", repr(text[:200]))
