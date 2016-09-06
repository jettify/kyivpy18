
def setup_admin(app, pg, admin_config_path):
    admin = aiohttp_admin.setup(app, admin_config_path)

    admin.add_resource(PGResource(pg, db.question, url='question'))
    admin.add_resource(PGResource(pg, db.choice, url='choice'))
    return admin

async def init(loop):
    # ...
    app = web.Application(loop=loop)
    # ...
    admin_config = str(PROJ_ROOT / 'static' / 'js')
    setup_admin(app, pg, admin_config)
