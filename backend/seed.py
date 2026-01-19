from datetime import date
from sqlmodel import SQLModel, Session, select

from .sqldb import engine
from .models import Movie

def run_seed():
    SQLModel.metadata.create_all(engine)
    movies = [
        Movie(
            movie_title="주토피아2",
            release_date=date(2025,11,26),
            director="Jared Bush,Byron Howard",
            genre="Animation",
            poster_url="https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/Zootopia_2_%282025_film%29.jpg/250px-Zootopia_2_%282025_film%29.jpg"
        ),
         Movie(
            movie_title="아바타:불과 재",
            release_date=date(2025,12,17),
            director="James Francis Cameron",
            genre="밀리터리SF",
            poster_url="https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Avatar_Fire_and_Ash_poster.jpeg/250px-Avatar_Fire_and_Ash_poster.jpeg"
        ),
        Movie(
            movie_title="인셉션",
            release_date=date(2010, 7, 21),
            director="Christopher Edward Nolan",
            genre="액션",
            poster_url="https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg"
        ),
        Movie(
        movie_title="어벤져스:엔드게임",
        release_date=date(2010, 7, 21),
        director="Christopher Edward Nolan",
        genre="슈퍼히어로",
        poster_url="https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg"
        ),
        Movie(
        movie_title = "범죄도시4",
        release_date=date(2024, 4, 24),
        director="허명행",
        genre="범죄",
        poster_url="https://upload.wikimedia.org/wikipedia/en/a/ae/The_Roundup_Punishment_film_poster.jpg"

    )]
    with Session(engine) as session:
        # (선택) 중복 방지: 제목 기준으로 이미 있으면 스킵
        for m in movies:
            exists = session.exec(select(Movie).where(Movie.movie_title == m.movie_title)).first()
            if not exists:
                session.add(m)
        session.commit()

if __name__ == "__main__":
    run_seed()