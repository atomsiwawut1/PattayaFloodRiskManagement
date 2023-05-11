import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz
import plotly.express as px

def run_map_app():
       st.subheader("Static Map")

#layout ("centered" or "wide")
st.set_page_config(page_title='Dashboard',page_icon=":world_map:",layout='wide')
# sharing Variable amoung pages

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Read data
in_csv ='https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/H3_MAP_Dataset_DEM2m_2016.csv'
df = pd.read_csv(in_csv)



st.header('Pattaya Flood Risk Dashboard')
with st.container():
# Metric
#max_rainfall = int(df["Annual_Rain_2016"].max(),)
    max_rainfall = round(df["Annual_Rain_2016"].max(),2)
    average_rainfall = round(df["Annual_Rain_2016"].mean(), 2)
    min_rainfall= round(df["Annual_Rain_2016"].min(), 2)
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
    #st.subheader("min_rainfall:")
    #st.subheader(f"{max_rainfall} mm")
        st.metric(label="Minimum rainfall", value=f"{min_rainfall} mm", delta=None)
    with middle_column:
    #st.subheader("Average Rainfall:")
    #st.subheader(f"{average_rainfall} mm")
        st.metric(label="Average rainfall", value=f"{average_rainfall} mm", delta=None)
    with right_column:
    #st.subheader("Max Rainfall:")
        st.metric(label="Maximum rainfall", value=f"{max_rainfall} mm", delta=None)

st.markdown("""---""")



empty1,content1,empty2,content2,empty3=st.columns([0.1,7,0.1,6,0.1])
with empty1:
        st.empty()
with content1:
    st.subheader("Pattaya_H3_Map", anchor=None)
    floodlist =df.FloodRisk.unique().tolist()
    list_default=["เสี่ยงภัยมาก","เสี่ยงภัยปานกลาง","เสี่ยงภัยน้อย"]
    choices = st.multiselect(" ",floodlist,default=list_default)
    #st.write(df[df.FloodRisk.isin(choices)])


    df=df[df.FloodRisk.isin(choices)]
    import streamlit as st
    import leafmap.kepler as leafmap
#12.886686,100.8527195
    m = leafmap.Map(center=[12.92, 100.86869255455714],zoom=11, widescreen=False)
    #in_csv=(r"C:\Users\Admin\OneDrive - Thammasat University\01_Thesis\11_ML_Model\H3_Predict.csv")
    #m.add_csv(in_csv,layer_name="hex_data")
    #config=(r"./GIS_DATA\Atom.json")
    #m.add_csv(in_csv,layer_name="hex_data",config=config)
    configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mapconfig.json"
    config=configurl
    m.add_df(df,layer_name="hex_data",config=config) 
    m.to_streamlit()



with empty2:
        st.empty()
with content2:
    st.subheader("Data Visualization", anchor=None)
    fig = px.histogram(data_frame=df,x='FloodRisk',color='FloodRisk', color_discrete_map={
                "ไม่มีความเสี่ยง": "#A6D96A",
                "เสี่ยงภัยปานกลาง": "#FDAE61",
                "เสี่ยงภัยมาก": "#D7191C",
                "เสี่ยงภัยน้อย": "#FFFFBF"
                },
             title="BarChart", height = 400)
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    

    count1 = df["FloodRisk"].value_counts()
    dff = pd.DataFrame()
    palette={"ไม่มีความเสี่ยง": "#A6D96A","เสี่ยงภัยปานกลาง": "#FDAE61","เสี่ยงภัยมาก": "#D7191C","เสี่ยงภัยน้อย": "#FFFFBF"}
    dff["name"]=[str(i) for i in count1.index]
    dff["number"] = count1.values
    pie_fig=px.pie(dff, values="number", names="name",color="name", color_discrete_map=palette, hole=.6,title="PieChart", height = 400)
    pie_fig.update(layout_showlegend=False)
    #pie_fig.update_layout({‘plot_bgcolor’: ‘rgba(0, 0, 0, 0)’,‘paper_bgcolor’: ‘rgba(0, 0, 0, 0)’,})
    st.plotly_chart(pie_fig, theme="streamlit", use_container_width=True)
    
    #st.write(pie_fig)


st.markdown("""---""")
with st.expander("Video"):
    a_column, b_column, c_column = st.columns(3)
    with a_column:
        st.video('https://www.youtube.com/watch?v=qwbLITj5fMo')
    with b_column:
        st.video('https://www.youtube.com/watch?v=JHx57St8yDk')
    with c_column:
        st.video('https://www.youtube.com/watch?v=H-W1eaZ0GGw')


st.markdown("""---""")


with st.expander("Dataframe"):
    st.dataframe(df)


