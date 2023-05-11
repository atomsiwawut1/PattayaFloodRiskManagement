import streamlit as st 
import pandas as pd 
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz
import sys
import os
import joblib
import streamlit as st
import leafmap.kepler as leafmap
from io import BytesIO
import pickle
import requests
from io import BytesIO
import pickle
import requests
import numpy as np

st.set_page_config(page_title='Flood Risk MAP BY ML',page_icon=":robot_face:",layout='wide')
css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model



Soil_Drainage_Capacity_map = {
    "ดินที่การระบายน้ำไม่ดี": 3,
    "ดินที่มีการระบายน้ำปานกลาง": 2,
    "ดินที่มีการระบายน้ำดี": 1
}

Landuse_map= {
	
    "W": 5,
    "A": 4,
    "U":3,
    "M":2,
    "F":1,
    "ETC":0

}



empty1,content1,empty2,content2,empty3=st.columns([0.1,7,0.1,6,0.1])



with content1:
	Annual_Rain = st.number_input("Annual_Rain",0,3000)
	Annual_Rain_slider = st.slider('Annual Rainfall : Slider bar', 0, 3000, Annual_Rain)
	Annual_Rain = Annual_Rain_slider
	st.write(Annual_Rain)
	
	Degree_Slope = st.number_input("Slope",0,3000)
	Degree_Slope_slider = st.slider('Slope : Slider bar', 0, 100, Degree_Slope)
	Degree_Slope = Degree_Slope_slider
	st.write(Degree_Slope)
	
	Elevation = st.number_input("Elevation",0,3000)
	Elevation_slider = st.slider('Elevation: Slider bar', 0, 1000, Elevation)
	Elevation = Elevation_slider
	st.write(Elevation)

	Soil_Drainage_Capacity_input = st.selectbox("Select Soil_Drainage_Capacity", options=list(Soil_Drainage_Capacity_map.keys()))
	Soil_Drainage_Capacity_number = Soil_Drainage_Capacity_map[Soil_Drainage_Capacity_input]
	Soil_Drainage_Capacity = Soil_Drainage_Capacity_number
	st.write(Soil_Drainage_Capacity)
	

		
	
with content2:
	Landuse_input = st.selectbox("Select Landuse", options=list(Landuse_map.keys()))
	Landuse_number = Landuse_map[Landuse_input]
	Landuse = Landuse_number
	st.write(Landuse)
	
	FAR = st.number_input("FAR",0,10)
	FAR_slider = st.slider('FAR : Slider bar', 0, 10, FAR)
	FAR= FAR_slider
	st.write(FAR)
	
	BCR = st.number_input("BCR",0,100)
	BCR_slider = st.slider('BCR : Slider bar', 0, 100, BCR )
	BCR= BCR_slider
	st.write(BCR)



data = pd.DataFrame(columns=['Annual_Rain', 'Soil_Drainage_Capacity', 'Elevation', 'Degree_Slope', 'Landuse', 'FAR', 'BCR'])

data = data.append({
        'Annual_Rain': Annual_Rain,
        'Soil_Drainage_Capacity': Soil_Drainage_Capacity,
        'Elevation': Elevation,
        'Degree_Slope': Degree_Slope,
        'Landuse': Landuse,
        'FAR': FAR,
        'BCR': BCR
    }, ignore_index=True)

st.dataframe(data)


feature_cols=['Annual_Rain','Elevation','Degree_Slope','Landuse','Soil_Drainage_Capacity','BCR','FAR']

X=data[feature_cols]

#MLmodel="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/453a18c6d71b18d9b0dd55c62a8a95a489aeb557/GIS_DATA/Flood%20Hazard%20Map.joblib"

#loadmodel = joblib.load("./GIS_DATA\FloodRiskMap_ML_BGT.joblib")
#predictEX= loadmodel.predict(X)


#st.write(predictEX)        



