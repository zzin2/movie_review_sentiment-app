from sqlmodel import Field, SQLModel
from datetime import date, datetime

class Movie(SQLModel, table=True):
    movie_id: int | None = Field(default=None, primary_key=True)      # 영화번호
    movie_title: str = Field(nullable=False)                          # 제목
    release_date: date = Field(nullable=False)                        # 개봉일
    director: str = Field(nullable=False)                             # 감독
    genre: str = Field(nullable=False)                                # 장르
    poster_url: str = Field(nullable=False)                           # 포스터 주소
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)    # 등록일

class MovieCreate(SQLModel):
    movie_title: str                          # 제목
    release_date: date                        # 개봉일
    director: str                             # 감독
    genre: str                               # 장르
    poster_url: str                          # 포스터 주소


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)                      # 리뷰 번호
    movie_id: int = Field(foreign_key="movie.movie_id", nullable=False)         # 영화 번호
    author_name: str = Field(nullable=False)                                    # 작성자 이름
    content: str = Field(nullable=False)                                        # 내용
    sentiment_label: str | None = Field(nullable=None)                          # 감성분석
    sentiment_score: float | None = Field(nullable=None)                        # 점수
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False) # 등록날짜