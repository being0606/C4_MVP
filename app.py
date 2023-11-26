import streamlit as st
import folium
import geocoder

def main():
    st.title("위치 업데이트 및 지도 표시 앱")

    # 위치 권한을 허용하는 버튼
    allow_location = st.button("내 위치 허용하기")

    # 위치 정보 초기화
    lat, lon = 0, 0

    # 위치 권한을 허용한 경우
    if allow_location:
        st.write("내 위치 허용됨.")
        st.write("버튼을 클릭하여 위치를 업데이트하세요.")
        location = geocoder.ip("me")  # 사용자의 현재 위치를 얻어옵니다.
        if location.ok:
            lat, lon = location.latlng
            st.write(f"현재 위치: 위도 {lat}, 경도 {lon}")

    # Leaflet 지도 생성
    map = folium.Map(location=[lat, lon], zoom_start=13)
    marker = folium.Marker([lat, lon], tooltip="내 위치")
    marker.add_to(map)
    st.write(map)

if __name__ == "__main__":
    main()
