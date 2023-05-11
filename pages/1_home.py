import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import leafmap.foliumap as leafmap
import geopandas
from geopandas import read_file

st.set_page_config(page_title='Home',page_icon=":derelict_house_building:",layout='centered')

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#st.header('My Hobby')
#image_url="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/Media/hunt.jpg"
#st.image(image_url,caption="best survival game",width=500)
st.header('ปรับปรุงริมน้ำตลาดท่านา')

empty1,content1,empty2,content2,empty3=st.columns([0.3,5,0.3,5,0.3])
with empty1:
        st.empty()
with content1:
    st.image("Media/TANA.png",caption="ปรับปรุงริมน้ำตลาดท่านา",use_column_width=True)
    st.image("Media/TANA2.png",caption="ปรับปรุงริมน้ำตลาดท่านา",use_column_width=True)
    st.image("Media/TANA3.png",caption="ปรับปรุงริมน้ำตลาดท่านา",use_column_width=True)
with empty2:
        st.empty()
with content2:
    st.image("Media/TANA4.png",caption="โครงการปรับปรุงภูมิทัศน์บริเวณทางเข้าตลาดท่านา",use_column_width=True)
    st.image("Media/TANA5.png",caption="โครงการพัฒนาเส้นทางจักรยานท่องเที่ยวชุมชนท่านาและพื้นที่เชื่อมโยง",use_column_width=True)
    st.image("Media/TANA6.png",caption="โครงการปรับปรุงจุดรับ-ส่งรถโดยสารสาธารณะ",use_column_width=True)