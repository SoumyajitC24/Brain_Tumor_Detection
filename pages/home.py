import streamlit as st

def app():
    #title to home page
    st.title("Brain Tumor Detection")

    #Image path
    st.image(".\image.jpeg")

    #Simple text to project
    
    st.title("Content:")
    st.write("Most brain tumors are not diagnosed until after symptoms appear. Often a brain tumor is initially diagnosed by an internist or a neurologist. An internist is a doctor who specializes in treating adults. A neurologist is a doctor who specializes in problems with the brain and central nervous system.")
    st.title("Magnetic Resonance Imaging (MRI):")
    st.write("An MRI uses magnetic fields, not x-rays, to produce detailed images of the body. MRI can be used to measure the tumor’s size. A special dye called a contrast medium is given before the scan to create a clearer picture. This dye can be injected into a patient’s vein or given as a pill or liquid to swallow.")
    st.title("Project Description:")
    st.write("This project helps us identify the existence and the type of Brain Tumor, when provided with a MRI scan. This is done so using Convolutional Neural Networks.")