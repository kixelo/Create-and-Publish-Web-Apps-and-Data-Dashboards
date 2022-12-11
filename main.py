import streamlit as st
import pandas

data = {
  "Series_1":[1,3,4,5,7], 
  "Series_2": [10,30,40,100,250]}

df=pandas.DataFrame(data)
#print(df)

st.title('Our first Streamlit App')
st.subheader('Introduction to Streamlit and Python')
st.write('''This is our first Web App
Enjoy it!
''')
st.write(df)
st.line_chart(df)
st.area_chart(df)
myslider = st.slider("Celsius")
st.write(myslider, "in Fahrenheit is", myslider * 9/5 + 32)

km_slider = st.slider("Km")
st.write(km_slider, "in Miles is", km_slider / 1.609)