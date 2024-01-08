import streamlit as st
st.set_page_config(page_title='Birds')
st.header("Types of Birds")

col1,col2=st.columns(2)
with col1:
     st.subheader("Parrot")
     st.image("./parrot.jpg",caption="Parrot",width=300,use_column_width=True)
     st.write("Parrots are cute")
with col2:
      st.subheader("Dove")
      st.image("./dove.jpg",caption="Dove",width=300,use_column_width=True)
      st.write("Doves are cute")
