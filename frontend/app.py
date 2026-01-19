import streamlit as st
import requests
from datetime import date

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(layout="wide", page_title="영화 리뷰 감성 분석", page_icon="🎬")
st.title("영화 리뷰 감성 분석")

tab1, tab2 = st.tabs(["영화 조회", "영화 등록"])





def fetch_movies():
    r = requests.get(f"{API_BASE}/movies", params={"offset": 0, "limit": 100}, timeout=10)
    r.raise_for_status()
    return r.json()

def delete_movie_api(movie_id: int):
    r = requests.delete(f"{API_BASE}/movies/{movie_id}", timeout=10)
    r.raise_for_status()
    return r.json()

def create_movie_api(payload: dict):
    r = requests.post(f"{API_BASE}/movies", json=payload, timeout=10)
    r.raise_for_status()
    return r.json()


with tab1:
    st.subheader("영화 조회")

    query = st.text_input("제목으로 검색", placeholder="예: 인셉션")

    col_btn, col_spacer = st.columns([1, 4])
    with col_btn:
        load_clicked = st.button("전체 불러오기", use_container_width=True)

    if load_clicked:
        try:
            st.session_state["movies"] = fetch_movies()
        except requests.RequestException as e:
            st.error(f"API 호출 실패: {e}")
            st.session_state["movies"] = []

    movies = st.session_state.get("movies", [])

    if query:
        q = query.strip().lower()
        movies = [m for m in movies if q in m["movie_title"].lower()]

    st.write(f"조회 결과: {len(movies)}개")

    if not movies:
        st.info("영화를 보려면 '전체 불러오기' 버튼을 누르세요.")
    else:
        for m in movies:
            col_img, col_info, col_btn = st.columns([1, 3, 1])

            with col_img:
                st.image(m["poster_url"], use_container_width=True)

            with col_info:
                st.markdown(f"### {m['movie_title']}")
                st.write(f"감독: {m['director']}")
                st.write(f"장르: {m['genre']}")
                st.write(f"개봉일: {m['release_date']}")

            with col_btn:
                st.write("")
                st.write("")
                if st.button("삭제", key=f"del_{m['movie_id']}", use_container_width=True):
                    try:
                        delete_movie_api(m["movie_id"])
                        st.success("삭제 완료")
                        st.session_state["movies"] = fetch_movies()
                        st.rerun()
                    except requests.RequestException as e:
                        st.error(f"삭제 실패: {e}")

            st.divider()


with tab2:
    st.subheader("영화 등록")

    with st.form("movie_create_form"):
        title = st.text_input("제목", placeholder="예: 인셉션")
        release = st.date_input("개봉일", value=date.today())
        director = st.text_input("감독", placeholder="예: Christopher Nolan")
        genre = st.text_input("장르", placeholder="예: 액션 / 드라마")
        poster_url = st.text_input("포스터 URL", placeholder="https://....jpg")

        submitted = st.form_submit_button("등록")

    if submitted:
        if not title.strip() or not director.strip() or not genre.strip() or not poster_url.strip():
            st.warning("제목/감독/장르/포스터 URL은 필수입니다.")
        else:
            payload = {
                "movie_title": title.strip(),
                "release_date": release.isoformat(),
                "director": director.strip(),
                "genre": genre.strip(),
                "poster_url": poster_url.strip(),
            }
            try:
                created = create_movie_api(payload)
                st.success(f"등록 완료: {created['movie_title']}")

                # 등록 후 목록도 갱신해두기(조회 탭에서 바로 보이게)
                try:
                    st.session_state["movies"] = fetch_movies()
                except Exception:
                    pass

            except requests.RequestException as e:
                st.error(f"등록 실패: {e}")
