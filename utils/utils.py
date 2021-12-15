import uuid
from uuid import uuid4
# import secrets
import base64
from flask import request, jsonify

rand_token = uuid4()
import secrets
token = secrets.token_hex(16)

print(rand_token)
print(token)


# from datetime import datetime, timedelta
import os

# token = db.Column(db.String(32), index=True, unique=True)
tokenone = base64.b64encode(os.urandom(24)).decode('utf-8')
print(tokenone)

from datetime import datetime, timedelta

now = datetime.utcnow()
# timedelta
print(now + timedelta(seconds=60))
print(now)

# token64 = base64./
