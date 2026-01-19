from sqlmodel import create_engine, Session
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent          # backend 폴더
DB_PATH = BASE_DIR / "database.db"                 # backend/database.db
sqlite_url = f"sqlite:///{DB_PATH}"
engine = create_engine(sqlite_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

