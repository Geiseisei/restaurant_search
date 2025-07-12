#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


merged_df = pd.read_csv("merged.csv")


# In[3]:


st.title("レストランサーチ")

price_limit = st.slider("最低価格の上限", min_value=500, max_value=16000, step=200, value=2000)
score_limit = st.slider("人気スコアの下限", min_value=0.0, max_value=35.0, step=2.0, value=5.0)


# In[4]:


filtered_df = merged_df[
    (merged_df['price'] <= price_limit) &
    (merged_df['pop_score'] >= score_limit)
]


# In[5]:


fig = px.scatter(
    filtered_df,
    x='pop_score',
    y='price',
    hover_data=['name_restaurant', 'access', 'star', 'review'],
    title='人気スコアと最低価格の散布図'
)

st.plotly_chart(fig)


# In[6]:


selected_restaurant = st.selectbox('気になるレストランを選んで情を確認', filtered_df['name_restaurant'])

if selected_restaurant:
    url = filtered_df[filtered_df['name_restaurant'] == selected_restaurant]['link_detail'].values[0]
    st.markdown(f"[{selected_restaurant}のページへ移動]({url})", unsafe_allow_html=True)


# In[7]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("star", "pop_score", "review", "price")
)

ascending = True if sort_key == "price" else False


# In[8]:


st.subheader(f"{sort_key}によるサロンランキング(上位10件)")

ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)

st.dataframe(ranking_df[["name_restaurant", "price", "pop_score", "star", "review", "access"]])


# In[ ]:





# In[ ]:




