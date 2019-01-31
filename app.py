from aiohttp import web
from routes import routes
import settings
from gino_db import db
from models.auth import User


def init():
    application = web.Application()
    for route in routes:
        application.router.add_route(route[0], route[1], route[2], name=route[3])
    return application


async def db_init(application):
    await db.set_bind("postgresql://{username}:{password}@{host}:{port}/{database}".format(**settings.DSN))
    await db.gino.create_all()  # create gino registered tables !if not exist!
    application['db'] = db

if __name__ == '__main__':
    app = init()
    app.on_startup.append(db_init)
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)
