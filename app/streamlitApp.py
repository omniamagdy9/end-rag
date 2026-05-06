import streamlit as st

# Page Configuration
st.set_page_config(page_title="Streamlit GUI Test", layout="wide")

# Header
st.title(" Streamlit Environment Test")
st.markdown("---")

# Layout Columns
col1, col2 = st.columns(2)

with col1:
    st.header("1. Interaction Test")
    user_name = st.text_input("Enter your name to test interactivity:")
    if st.button("Run Test"):
        if user_name:
            st.success(f"Connection successful! Hello, {user_name}.")
            st.balloons()
        else:
            st.warning("Please enter a name to trigger the effect.")

with col2:
    st.header("2. Media & UI Test")
    # Using 'use_container_width' to avoid the deprecation warnings 
    # you might encounter with older parameter names
    test_upload = st.file_uploader("Upload an image (Testing OCR/Image Path)", type=['png', 'jpg'])
    
    if test_upload:
        st.image(test_upload, caption="Uploaded Test Image", use_container_width=True)
        st.info("Image rendered successfully. Your GUI environment is stable.")

# System Info Check
st.sidebar.header("System Status")
st.sidebar.write(" Streamlit is running")
st.sidebar.write(" Python Environment Active")