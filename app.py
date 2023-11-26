import streamlit as st
import folium
import geocoder
import time

def main():
    st.title("위치 업데이트 및 지도 표시 앱")
    
    # 위치 권한을 허용하는 버튼
    allow_location = st.button("내 위치 허용하기")
    
    # 위치 권한을 허용한 경우
    if allow_location:
        st.write("내 위치 허용됨.")
        st.write("10초마다 위치가 업데이트됩니다.")
        
        # Leaflet 지도 생성
        map = folium.Map(location=[0, 0], zoom_start=13)
        marker = folium.Marker([0, 0], tooltip="내 위치")
        marker.add_to(map)
        st.write(map)

        # 10초마다 위치 업데이트
        while True:
            location = geocoder.ip("me")  # 사용자의 현재 위치를 얻어옵니다.
            if location.ok:
                lat, lon = location.latlng
                marker.location = [lat, lon]  # 마커의 위치 업데이트
                st.write(f"현재 위치: 위도 {lat}, 경도 {lon}")
            time.sleep(10)

if __name__ == "__main__":
    main()
