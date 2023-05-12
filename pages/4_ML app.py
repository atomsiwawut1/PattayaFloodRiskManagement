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
import plotly.graph_objects as go

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
	
    "พื้นที่น้ำ (W)": 5,
    "พื้นที่เกษตรกรรม (A)": 4,
    "พื้นที่ชุมชนและสิ่งปลูกสร้าง (U)":3,
    "พื้นที่เบ็ดเตล็ด (M)":2,
    "พื้นที่ป่าไม้ (F)":1,
    "อื่นๆ (ETC)":0

}

st.header("Flood Susceptibility Assessment")

empty1,content1,empty2,content2,empty3,content3,empty4=st.columns([0.1,1,0.1,1,0.1,1.5,0.1])



with content1:
	st.markdown("<h4>Hazard factors</h4>", unsafe_allow_html=True)
	Annual_Rain = st.number_input("Annual_Rain",0,3000)
	Annual_Rain_slider = st.slider('', 0, 3000, Annual_Rain)
	Annual_Rain = Annual_Rain_slider
	st.write(Annual_Rain)
	
	Degree_Slope = st.number_input("Slope",0,3000)
	Degree_Slope_slider = st.slider('', 0, 100, Degree_Slope)
	Degree_Slope = Degree_Slope_slider
	st.write(Degree_Slope)
	
	Elevation = st.number_input("Elevation",0,3000)
	Elevation_slider = st.slider('', 0, 1000, Elevation)
	Elevation = Elevation_slider
	st.write(Elevation)

	Soil_Drainage_Capacity_input = st.selectbox("Select Soil_Drainage_Capacity", options=list(Soil_Drainage_Capacity_map.keys()))
	Soil_Drainage_Capacity_number = Soil_Drainage_Capacity_map[Soil_Drainage_Capacity_input]
	Soil_Drainage_Capacity = Soil_Drainage_Capacity_number
	st.write(Soil_Drainage_Capacity)
	

		
	
with content2:
	st.markdown("<h4>Vulnerability factors</h4>", unsafe_allow_html=True)
	Landuse_input = st.selectbox("Landuse", options=list(Landuse_map.keys()))
	Landuse_number = Landuse_map[Landuse_input]
	Landuse = Landuse_number
	st.write(Landuse)
	
	FAR = st.number_input("FAR (Floor to Area Ratio)",0,10)
	FAR_slider = st.slider('-', 0, 10, FAR)
	FAR= FAR_slider
	st.write(FAR)
	
	BCR = st.number_input("Building Coverage Ratio (BCR)",0,100)
	BCR_slider = st.slider('-', 0, 100, BCR )
	BCR= BCR_slider
	st.write(BCR)





#MLmodel="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/453a18c6d71b18d9b0dd55c62a8a95a489aeb557/GIS_DATA/Flood%20Hazard%20Map.joblib"

#loadmodel = joblib.load("./ML_Model\FloodRisk_ML_BGDT.joblib")
#model_file_path = "./ML_Model\FloodRisk_ML_BGDT.pkl"

# Load the pickled model ต้องใช้ pickle
#with open(model_file_path, "rb") as f:
#loaded_model = pickle.load(f)

#predictEX= loadmodel.predict(X)

#predictEX = loaded_model.predict(X)



#mLink = 'https://raw.githubusercontent.com/atomsiwawut1/PattayaFloodRiskManagement/main/ML_Model/FloodRisk_ML_BGDT.pkl'

# mLink = 'https://github.com/atomsiwawut1/FloodPrediction/blob/main/GIS_DATA/FloodModel.pkl?raw=true'


with content3:
	st.markdown("<h4>Prediction</h4>", unsafe_allow_html=True)
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
	mLink = 'https://github.com/atomsiwawut1/PattayaFloodRiskManagement/blob/main/ML_Model/FloodRisk_ML_BGDT.pkl?raw=true'
	mfile = BytesIO(requests.get(mLink).content)
	loadmodel=joblib.load(mfile)
	predictEX= loadmodel.predict(X)
	text = str(predictEX[0]) 
	#st.write(text)


if text == 'เสี่ยงภัยมาก':
    gauge_value = 100
    gauge_min = 0
    gauge_max = 100
    gauge_label = 'เสี่ยงภัยมาก'
    gauge_color = 'red'
elif text == 'เสี่ยงภัยปานกลาง':
    gauge_value = 50
    gauge_min = 0
    gauge_max = 100
    gauge_label = 'เสี่ยงภัยปานกลาง'
    gauge_color = 'orange'
elif text == 'เสี่ยงภัยน้อย':
    gauge_value = 30
    gauge_min = 0
    gauge_max = 100
    gauge_label = 'เสี่ยงภัยน้อย'
    gauge_color = 'yellow'
else:
    gauge_value = 0
    gauge_min = 0
    gauge_max = 100
    gauge_label = 'ไม่มีความเสี่ยง'
    gauge_color = 'green'



# Create the Gauge Chart using plotly
fig = go.Figure(go.Indicator(
    mode='gauge+number',
    value=gauge_value,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [gauge_min, gauge_max]},
           'bar': {'color': gauge_color},
           'steps': [
               {'range': [gauge_min, gauge_max], 'color': 'lightgray'}],
           'threshold': {
               'line': {'color': 'red', 'width': 4},
               'thickness': 0.75,
               'value': gauge_value}
           },
    title={'text': gauge_label}))

#fig.update_layout(height=400)

fig.update_layout(height=400)
# Display the Gauge Chart
content3.plotly_chart(fig)
               

      



