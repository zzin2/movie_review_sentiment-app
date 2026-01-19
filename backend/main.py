'''
백엔드 (FastAPI)
    기능
        영화 관리
            - 등록: 제목, 개봉일, 감독, 장르, 포스터 URL (나무위키 참고)
            - 전체/특정 영화 조회
            - 특정 영화 삭제
    (심화)
    리뷰 관리
        - 등록, 전체/특정 영화 리뷰 조회, 삭제
    평점 조회
        - 리뷰 감성 분석 점수의 평균
    리뷰 감성 분석
        - 모델: 적절한 모델 리서치하여 적용
        - 모델 경량화 방식에 대해 고민해보기
'''

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import SQLModel, Session, select
from backend.sqldb import engine, get_session
from backend.models import Movie,MovieCreate
from typing import Dict

app = FastAPI()
@app.post("/movies", response_model=Movie)
def create_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    db_movie = Movie.model_validate(movie)
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@app.get("/movies", response_model=list[Movie])
def read_movie(session: Session = Depends(get_session)):
        movies = session.exec(select(Movie)).all()
        return movies

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int, session: Session = Depends(get_session)):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="영화를 찾지 못했습니다.")
    return movie

@app.delete("/movies/{movie_id}", response_model=Dict[str, bool])
def delete_movie(movie_id: int, session: Session = Depends(get_session)):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="영화를 찾지 못했습니다.")
    session.delete(movie)
    session.commit()
    return {"ok": True}


