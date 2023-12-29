import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
st.write("- Persian cat")
persian_cat_image = r"C:\Users\HP\Desktop\Major Project\1.JPG"
st.image(persian_cat_image, caption='Persian Cat')
st.write("- White cat")
white_cat_image = r"C:\Users\HP\Desktop\Major Project\2.JPG"
st.image(white_cat_image, caption='White Cat')
