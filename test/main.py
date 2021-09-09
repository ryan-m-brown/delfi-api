from database.dao import DAO

from database.models import Site
from mock import site as data

if __name__ == '__main__':
    dao = DAO()
    dao.insert(Site(data))
    site = dao.fetch_site(1)

    print(site)
