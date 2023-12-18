import streamlit as st
import pandas as pd
import geocoder

def main():
    st.title("위치 업데이트 및 지도 표시 앱")
    
    # 위치 정보 초기화
    lat, lon = 0, 0
    
    # 위치 권한을 허용하는 버튼
    allow_location = st.button("내 위치 허용하기")

    # 위치 권한을 허용한 경우
    if allow_location:
        st.write("내 위치 허용됨.")
        st.write("버튼을 클릭하여 위치를 업데이트하세요.")
        location = geocoder.ip("me")  # 사용자의 현재 위치를 얻어옵니다.
        if location.ok:
            lat, lon = location.latlng
            st.write(f"현재 위치: 위도 {lat}, 경도 {lon}")

    # 데이터 프레임 생성
    df = pd.DataFrame({'LAT': [lat], 'LON': [lon]})

    # 지도 시각화
    st.map(df)
    
    # 음식점 위치를 받기 위한 버튼
    allow_location = st.button("음식점 위치 허용하기")
    

if __name__ == "__main__":
    main()
