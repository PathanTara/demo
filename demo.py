import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
st.write("- Persian cat")
st.image("./1.jpg",width=500, height=400)
st.write("- White cat")
st.image("./2.jpg",width=500, height=400)
st.write("- Persian cat")
st.image("data:image/jpeg;base64,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")
