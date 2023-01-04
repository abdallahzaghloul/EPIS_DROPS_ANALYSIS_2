import numpy as np #1
import pandas as pd #2
import plotly.graph_objects as go  #6
import plotly.express as px  #7
from plotly.subplots import make_subplots  #8
import plotly.figure_factory as ff #21
from PIL import Image
import streamlit as st

pd.set_option('mode.chained_assignment',None)

im = Image.open("EPIS.png")
image = np.array(im)
st.image(image)


st.markdown(" <center>  <h1> KPC (DRLG/WO) Drops Analysis </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
 
st.markdown(" <left>  <h1> KPC (DRLG/WO) Drops Analysis </h1> </font> </left> </h1> ",
            unsafe_allow_html=True)
 

#####

df = pd.read_excel("Book1.xlsx")
df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]
df['LOCATION_']=df['LOCATION'].str.replace('Driller_Cabinet','Rig_Floor').str.replace('Drilling_Cabine','Rig_Floor').str.replace('Driller_Cap','Rig_Floor').str.replace('Apache_Camp','Fly_camp').str.replace('Caravan STB','Fly_camp').str.replace('DRAW-_WORKS_CARRIER','Carrier').str.replace('Light_tower','Rig_Floor').str.replace('Mess_Hall','Main_Camp')
df['LOCATION_']=df['LOCATION_'].str.replace('Caravan Service','Fly_camp')
df['LOCATION_']=df['LOCATION_'].str.replace('Travelling_Block','Travelling_Equipment')
df['LOCATION_']=df['LOCATION_'].str.replace('Rig_floor','Rig_Floor')
df['LOCATION_']=df['LOCATION_'].str.replace('TDS','Travelling_Equipment')
df['LOCATION_']=df['LOCATION_'].str.replace('MI_SWACO_UNIT','Engine_Area')
df['LOCATION_']=df['LOCATION_'].str.replace('Dog_House','Rig_Floor')
df['LOCATION_']=df['LOCATION_'].str.replace('Fire_Pump','Tank_Area')
df['LOCATION_']=df['LOCATION_'].str.replace('Engine_Room','Engine_Area')
df['LOCATION_']=df['LOCATION_'].str.replace('Pump_Room','Engine_Area')
df['LOCATION_']=df['LOCATION_'].str.replace('Travelling_Block','Travelling_Equipment').str.replace('Crown_Block','Travelling_Equipment')
df['LOCATION_']=df['LOCATION_'].str.replace('Sub-structure','Sub_structure')


df.drop(df[df['LOCATION']=='System_Area'].index, axis= 0, inplace=True)

df['VALUE']=1
Loc_List= list(df.LOCATION_.unique())
Rig_List = list(df.RIG_NAME.unique())

for i in Loc_List:

    Rig_List_Fail=[]

    for j in list(df.RIG_NAME.unique()):
        Rig_List_Fail.append(((df[(df['FAIL/PASS']=='Fail')&(df['LOCATION_']==i)&(df['RIG_NAME']==j)]['VALUE'].sum())))
        
    fig=px.bar(x=Rig_List, y=Rig_List_Fail,labels={'x':f'KPC (DRLG/WO) Rigs{i} Fail Points ', 'y':f'Total {i} Fail Points'})

    for k in list(df.RIG_NAME.unique()):
           fig.add_annotation(x=k,y=df[(df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==k)&(df['LOCATION_']==i)]['VALUE'].sum()+0.5, text=f"{df[(df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==k)&(df['LOCATION_']==i)]['VALUE'].sum()}", showarrow=False)

    fig.update_layout(title_text=f"{df[(df['FAIL/PASS']=='Fail')&(df['LOCATION_']==i)]['VALUE'].sum()} Fail Points with Rig`s Contribution", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# streamlit run "C:\\Users\\hp\\Desktop\\EPIS\\EDC_87\\EPIS_HOME.py" 


















