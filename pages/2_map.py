import streamlit as st 
import pandas as pd 

import sys
import os
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz


def run_map_app():
   st.subheader("Static Map")

#layout ("centered" or "wide")
st.set_page_config(page_title='Map',page_icon=":world_map:",layout='centered')
# sharing Variable amoung pages

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.subheader("Map")

tab1, tab2  = st.tabs(["GeoDataFrame","Pattaya City"])





with tab1:
   st.header("GeoDataFrame")
   import leafmap.kepler as leafmap
   m = leafmap.Map(center=[12.920912, 100.900474], zoom=8, widescreen=True)
   #gdf = gpd.read_file(r"GIS_DATA\00_SHP\TAMBON_A.shp")
   gdf = gpd.read_file(r"https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/00_SHP/TAMBON.zip")
   m.add_gdf(gdf, "Tambon")
   #in_shp ="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/00_SHP/TAMBON.zip"
   #m.add_shp(in_shp, "Tambon")
   m.to_streamlit()




  
with tab2:
   st.header("Pattaya_H3_Map")
   import streamlit as st
   import leafmap.kepler as leafmap
#12.886686,100.8527195
   
   m = leafmap.Map(center=[12.92, 100.86869255455714], zoom=11, widescreen=False)
   #in_csv=(r"C:\Users\Admin\OneDrive - Thammasat University\01_Thesis\11_ML_Model\H3_Predict.csv")
   in_csv ='https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/H3_MAP_Dataset_DEM2m_2016.csv'
   #m.add_csv(in_csv,layer_name="hex_data")
   #config=(r"./GIS_DATA\Atom.json")
   #m.add_csv(in_csv,layer_name="hex_data",config=config)
   configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mapconfig.json"
   config=configurl
   m.add_csv(in_csv,layer_name="hex_data",config=config) 
   m.to_streamlit()







   # button widget
   #st.subheader('SAVE CONFIG')
   #st.caption('')
   #if st.button('SAVE CONFIG'):
   #m.save_config("GIS_DATA/Atom111config.json")
   #st.write('save')


