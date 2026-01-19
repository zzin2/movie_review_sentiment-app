# movie_review_sentiment-app

Streamlit(프론트엔드) + FastAPI(백엔드) 기반의 **영화 관리 웹 애플리케이션**입니다.  
현재는 영화 **등록/조회/삭제** 기능을 구현했으며, 추후 **리뷰 등록 및 감성 분석 기능**을 확장할 예정입니다.

## 주요 기능(현재 구현)
- 영화 등록(제목, 개봉일, 감독, 장르, 포스터 URL)
- 영화 전체 조회(목록)
- 제목 기반 검색(프론트에서 필터링)
- 영화 삭제

## 추후 확장 예정(미구현)
- 리뷰 등록/조회/삭제
- 리뷰 감성 분석(모델 적용) 및 평균 점수 집계

## 기술 스택
- Frontend: Streamlit
- Backend: FastAPI
- DB: SQLite
- ORM: SQLModel

## 폴더 구조
```text
movie-review-sentiment-app/
  backend/
    main.py
    models.py
    sqldb.py
    seed.py
    database.db (로컬 생성)
  frontend/
    app.py
