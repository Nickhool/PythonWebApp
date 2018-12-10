__Author__ = "noduez"

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from www.coroweb import get, post

from www.models import User, Blog, Comment, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__templates__': 'test.html',
        'users': users
    }