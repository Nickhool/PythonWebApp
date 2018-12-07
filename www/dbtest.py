__Author__ = "noduez"

import asyncio
import www.orm
from www.models import User, Blog, Comment

async def test(loop):
    await www.orm.create_pool(loop, user='root', password='123456', database='awesome')

    u = User(name='adminz_sj712', admin=True, email='1282622481@qq.com', passwd='awesome12593', image='about:blank')

    await u.save()

#要运行协程，需要使用事件循环
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        loop.close()