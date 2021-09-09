import logging
import os
import sys

import responder

from database.dao import DAO
from database.models import Site
from mock import site as mock_site

FORMAT = '%(asctime)s - %(filename)s - line %(lineno)d - %(levelname)s: %(message)s'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p'))
logger.addHandler(handler)

os.environ["PORT"] = os.getenv('NOMAD_PORT_http', '5033')
api = responder.API()


@api.route("/health")
class Health:

    def on_get(self, req, resp):
        logger.debug('Got /health request')
        resp.status_code = 200
        resp.media = {"success": True}

    def on_post(self, req, resp):
        resp.status_code = 501
        resp.media = {"success": False, "error": "Not Implemented"}


@api.route("/site/{id}")
class SiteGet:

    def on_get(self, req, resp, *, id):
        logger.info(f"Fetching site id: {id}")
        try:
            data = dao.fetch_site(int(id))
            if data is None:
                resp.status_code = 200
                resp.media = {}
            else:
                resp.status_code = 200
                resp.media = data
        except Exception as e:
            resp.status_code = 500
            resp.media = str(e)


@api.route("/site")
class SitePost:

    def on_get(self, req, resp):
        try:
            data = dao.fetch_all()
            if data is None:
                resp.status_code = 200
                resp.media = {}
            else:
                resp.status_code = 200
                resp.media = data
        except Exception as e:
            resp.status_code = 500
            resp.media = str(e)

    async def on_post(self, req, resp):
        content_type = req.mimetype
        if content_type != 'application/json':
            resp.status_code = 415
            resp.media = f"Unsupported content type: {content_type}"
            return

        message = await req.media()
        if message is None:
            resp.status_code = 422
            resp.media = "No payload provided"
            return

        try:
            dao.insert(Site(message))

            resp.status_code = 200
            resp.media = {"success": True}
        except Exception as e:
            resp.status_code = 500
            resp.media = str(e)


@api.route("/seed")
class SiteSeed:

    async def on_post(self, req, resp):
        try:
            dao.insert(Site(mock_site))

            resp.status_code = 200
            resp.media = {"success": True}
        except Exception as e:
            resp.status_code = 500
            resp.media = str(e)


@api.route("/ids")
class SiteSeed:

    def on_get(self, req, resp):
        try:
            data = dao.fetch_ids()
            if data is None:
                resp.status_code = 200
                resp.media = {}
            else:
                resp.status_code = 200
                resp.media = data
        except Exception as e:
            resp.status_code = 500
            resp.media = str(e)


if __name__ == '__main__':
    dao = DAO()

    api.run()
