from typing import Optional, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base, Site

engine = create_engine('sqlite:///database.db')


class DAO:

    def __init__(self):
        Base.metadata.create_all(engine)

    def insert(self, site: Site):
        session = sessionmaker(bind=engine)()
        session.add(site)
        session.commit()

    def fetch_all(self):
        session = sessionmaker(bind=engine)()
        sites = session.query(Site.data).all()
        session.commit()

        return sites

    def fetch_site(self, id: int) -> Optional[str]:
        session = sessionmaker(bind=engine)()
        site = session.query(Site).filter(Site.id == id).first()
        session.commit()

        if site is None:
            return None

        return site.data

    def fetch_ids(self) -> List[str]:
        session = sessionmaker(bind=engine)()
        ids = session.query(Site.id).all()
        session.commit()

        return [item for sublist in ids for item in sublist]
