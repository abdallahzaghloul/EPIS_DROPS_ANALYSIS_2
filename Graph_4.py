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


st.markdown(" <center>  <h1> KPC (DRLG/WO) Drops Analysis by Location </h1> </font> </center> </h1> ",
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


st.markdown("""<style>.big-font {font-size:300px !important;}</style>""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

Rig_List0= list(df.RIG_NAME.unique())
Rig_List0.insert(0,'Total_Mast_Points')
Rig_List_Mast=[(((df[(df['LOCATION_']=='Mast')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))]
for i in list(df.RIG_NAME.unique()):
    Rig_List_Mast.append(((df[(df['LOCATION_']=='Mast')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum())))
fig_0=px.bar(x=Rig_List0, y=Rig_List_Mast)


Rig_List1= list(df.RIG_NAME.unique())

Rig_List1.insert(0,'Total_Rig_Floor_Points')

Rig_List_Rig_Floor=[(((df[(df['LOCATION_']=='Rig_Floor')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))]

for i in list(df.RIG_NAME.unique()):
    Rig_List_Rig_Floor.append(((df[(df['LOCATION_']=='Rig_Floor')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum())))

fig_1=px.bar(x=Rig_List1, y=Rig_List_Rig_Floor)



Rig_List2= list(df.RIG_NAME.unique())

Rig_List2.insert(0,'Total_Mud_System_Points')

Rig_List_Mud_System=[(((df[(df['LOCATION_']=='Mud_System')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))]

for i in list(df.RIG_NAME.unique()):
    Rig_List_Mud_System.append(((df[(df['LOCATION_']=='Mud_System')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum())))

fig_2=px.bar(x=Rig_List2, y=Rig_List_Mud_System)



Rig_List3= list(df.RIG_NAME.unique())

Rig_List3.insert(0,'Total_Engine_Area_Points') ##

Rig_List_Engine_Area=[(((df[(df['LOCATION_']=='Engine_Area')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Engine_Area.append(((df[(df['LOCATION_']=='Engine_Area')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##

fig_3=px.bar(x=Rig_List3, y=Rig_List_Engine_Area) ##



Loc_List4 = list(df.LOCATION_.unique())

Rig_List4= list(df.RIG_NAME.unique())

Rig_List4.insert(0,'Total_Tank_Area_Points') ##

Rig_List_Tank_Area=[(((df[(df['LOCATION_']=='Tank_Area')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Tank_Area.append(((df[(df['LOCATION_']=='Tank_Area')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_4=px.bar(x=Rig_List4, y=Rig_List_Tank_Area) ##

Loc_List = list(df.LOCATION_.unique())

Rig_List5= list(df.RIG_NAME.unique())

Rig_List5.insert(0,'Total_Sub_Structure_Points') ##

Rig_List_Sub_structure=[(((df[(df['LOCATION_']=='Sub_structure')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Sub_structure.append(((df[(df['LOCATION_']=='Sub_structure')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_5= px.bar(x=Rig_List5, y=Rig_List_Sub_structure) ##

Rig_List6= list(df.RIG_NAME.unique())

Rig_List6.insert(0,'Total_Travelling_Equipment_Points') ##

Rig_List_Travelling_Equipment=[(((df[(df['LOCATION_']=='Travelling_Equipment')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Travelling_Equipment.append(((df[(df['LOCATION_']=='Travelling_Equipment')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_6=px.bar(x=Rig_List6, y=Rig_List_Travelling_Equipment) ##

Rig_List7= list(df.RIG_NAME.unique())

Rig_List7.insert(0,'Total_SCR_Points') ##

Rig_List_SCR=[(((df[(df['LOCATION_']=='SCR')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_SCR.append(((df[(df['LOCATION_']=='SCR')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_7=px.bar(x=Rig_List7, y=Rig_List_SCR) ##


Rig_List8= list(df.RIG_NAME.unique())

Rig_List8.insert(0,'Total_Main_Camp_Points') ##

Rig_List_Main_Camp=[(((df[(df['LOCATION_']=='Main_Camp')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Main_Camp.append(((df[(df['LOCATION_']=='Main_Camp')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_8=px.bar(x=Rig_List8, y=Rig_List_Main_Camp) ##


Rig_List9= list(df.RIG_NAME.unique())

Rig_List9.insert(0,'Total_Fly_camp_Points') ##

Rig_List_Fly_camp=[(((df[(df['LOCATION_']=='Fly_camp')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Fly_camp.append(((df[(df['LOCATION_']=='Fly_camp')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_9=px.bar(x=Rig_List9, y=Rig_List_Fly_camp) ##


Rig_List10= list(df.RIG_NAME.unique())

Rig_List10.insert(0,'Total_Carrier_Points') ##

Rig_List_Carrier=[(((df[(df['LOCATION_']=='Carrier')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Carrier.append(((df[(df['LOCATION_']=='Carrier')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_10=px.bar(x=Rig_List10, y=Rig_List_Carrier) ##


Rig_List11= list(df.RIG_NAME.unique())

Rig_List11.insert(0,'Total_Workshop_Points') ##

Rig_List_Workshop=[(((df[(df['LOCATION_']=='Workshop')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Workshop.append(((df[(df['LOCATION_']=='Workshop')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_11=px.bar(x=Rig_List11, y=Rig_List_Workshop) ##


Rig_List12= list(df.RIG_NAME.unique())

Rig_List12.insert(0,'Total_Accumulator_Points') ##

Rig_List_Accumulator=[(((df[(df['LOCATION_']=='Accumulator')& (df['FAIL/PASS']=='Fail')]['VALUE'].sum())))] ##

for i in list(df.RIG_NAME.unique()):
    Rig_List_Accumulator.append(((df[(df['LOCATION_']=='Accumulator')& (df['FAIL/PASS']=='Fail')&(df['RIG_NAME']==i)]['VALUE'].sum()))) ##
 
fig_12=px.bar(x=Rig_List12, y=Rig_List_Accumulator) ##



#####
st.plotly_chart(fig_0, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_1, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_2, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_3, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_4, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_5, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_6, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_7, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_8, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_9, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_10, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_11, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig_12, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

# streamlit run "C:\\Users\\hp\\Desktop\\EPIS\\EDC_87\\EPIS_HOME.py" 


















