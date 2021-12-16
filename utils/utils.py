import uuid
from uuid import uuid4
import secrets
import base64
# from flask import request, jsonify
#
# rand_token = uuid4()
# import secrets
# token = secrets.token_hex(16)
#
# print(rand_token)
# print(type(str(token)))
# a = '123'
# print(type(a))

# from datetime import datetime, timedelta
# import os
#
# # token = db.Column(db.String(32), index=True, unique=True)
# tokenone = os.urandom(24)
# print(tokenone)

# from datetime import datetime, timedelta
#
# now = datetime.utcnow()
# # timedelta
# print(now + timedelta(seconds=60))
# print(now)

# token64 = base64./
from datetime import datetime, timedelta
#
# print(datetime.strptime('2021-12-15 13:13:13.00001', '%Y-%m-%d %H:%M:%S.%f'))


def create_token():
    now_time = datetime.utcnow()
    token = str(secrets.token_hex(16))
    token_expiration = now_time + timedelta(seconds=1800)
    return token, token_expiration


tokens = create_token()
print(tokens)
