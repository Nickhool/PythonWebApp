__Author__ = "noduez"

import asyncio
import www.orm
from www.models import User, Blog, Comment

# async def test(loop):
#     await www.orm.create_pool(loop, user='root', password='123456', database='awesome')
#
#     u = User(name='adminz_sj712', admin=True, email='1282622481@qq.com', passwd='awesome12593', image='about:blank')
#
#     await u.save()

#要运行协程，需要使用事件循环
# if __name__ == '__main__':
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(test(loop))
#         print('Test finished.')
#         loop.close()


async def test(loop):
    await www.orm.create_pool(loop=loop, user='root', password='123456', database='awesome')
    u = Blog(user_id='001543028386871e12de7ab862d4f4c9267ea829f2847bb000', user_name='test', user_image='about:blank',name='Test', summary='BlogTest', content='1234567890')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

