
# coding: utf-8

# # Final Project
# ## 12-752: Data-Driven Building Energy Management
# ## Fall 2016, Carnegie Mellon University

# In[35]:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import types
import datetime

get_ipython().magic('matplotlib inline')


# In[41]:

# get the initial occupancy dataframe with each room in one of occupied room and occupied room2

occupancy_file = open('dataset-dred/Occupancy_data.csv','rb')
occupancy = pd.read_csv(occupancy_file, header='infer')
occupancy['Time'] = pd.to_datetime(occupancy['Time'], format="%Y-%m-%d %H:%M:%S")
occupancy = occupancy.drop_duplicates()
occupancy['Occupied Room'] = occupancy['Occupied Room'].apply(lambda x: x.split('[')[1].split(']')[0])
occupancy['Occupied Room'] = occupancy['Occupied Room'].apply(lambda x: x.split('\''))
occupancy['Occupied Room'] = occupancy['Occupied Room'].apply(lambda x: x if(len(x)>3) else x[1])
occupancy['Occupied Room2'] = occupancy['Occupied Room'].apply(lambda x: x[-2] if(isinstance(x, list)) else np.NaN)
occupancy['Occupied Room'] = occupancy['Occupied Room'].apply(lambda x: x[1] if(isinstance(x, list)) else x)
occupancy.head()


# In[43]:

# create a new dummy DataFrame. index = each second from start of occupancy to end of occupancy.
# columns in the dataframe are the different rooms. For now all values are 0.

rooms = ['Kitchen', 'LivingRoom', 'StoreRoom', 'Room1', 'Room2']
# rooms
idx = occupancy.index
st = occupancy['Time'][idx[0]]
et = occupancy['Time'][idx[-1]]
new_idx = pd.date_range(start=st, end=et, freq='S')
room_occ = pd.DataFrame(columns=rooms, index=new_idx)
room_occ = room_occ.fillna(0)
room_occ.head()


# In[44]:

# In the dataFrame created above, if value at a Time for a room is 1, it means that the room was occupied 
# at that moment. These values are set by using occupancy dataframe.

idx = occupancy.index
k = 0
for i in idx:
    timestamp, r1, r2 = occupancy[occupancy.index == i].values[0]
    room_index1 = rooms.index(r1)
    room_occ.set_value(timestamp, rooms[room_index1],1)
    if (pd.isnull(r2) == False):
        room_index2 = rooms.index(r2)
        room_occ.set_value(timestamp, rooms[room_index2],1)
room_occ.head()


# In[46]:

# Open All_data.csv, put it a DataFrame and set time as Index

alldata_file = open('dataset-dred/All_data.csv','rb')
alldata = pd.read_csv(alldata_file, header='infer', parse_dates=[1])
alldata['Time'] = alldata['Time'].str.split(pat='+').str[0]
alldata['Time'] = pd.to_datetime(alldata['Time'])
alldata = alldata.set_index('Time')
alldata['mains'] = alldata['mains'].astype(float)
power_data = alldata.resample('1S').mean()
power_data = power_data.fillna(0)
power_data


# In[47]:

alldata = pd.merge(power_data, room_occ, left_index=True, right_index=True)
alldata


# In[48]:

#rooms = occupancy['Occupied Room'].unique()
#Kitchen = occupancy[occupancy['Occupied Room'] == rooms[0]]
#LivingRoom = occupancy[occupancy['Occupied Room'] == rooms[1]]
#StoreRoom = occupancy[occupancy['Occupied Room'] == rooms[5]]
#Room1 = occupancy[occupancy['Occupied Room'] == rooms[4]]
# a = occupancy[occupancy['Occupied Room'] == rooms[6]]


# Room2 = alldata[['Time','oven','toaster']]
# #Room2['Occupancy'] = a
# result = pd.concat([a, Room2], axis=1)
# Room2


# In[49]:

# b = occupancy[occupancy['Occupied Room'] == rooms[7]]
# b


# In[50]:

# rooms


# In[ ]:



