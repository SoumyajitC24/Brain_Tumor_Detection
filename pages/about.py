"""This create About me page"""

# Import necessary module
from typing import Text
from six import text_type
import streamlit as st

def app():
    st.balloons()
    st.title('Contact Me')
    st.markdown('''#### Name:
    Soumyajit Chakraborty''')
    st.markdown('''#### Email:
    soumyajitc24.170@gmail.com''')
    #with st.echo():
    st.markdown('''<p>
                    <h4>GitHub:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                        <p style="padding:10px">
                            <a href = "https://github.com/SoumyajitC24/Brain_Tumor_Detection" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New' , stroke='currentColor';"> 
                                        You can find my project here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)
    st.markdown('''<p>
                    <h4>LinkedIn:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                        <p style="padding:10px">
                            <a href = https://www.linkedin.com/in/soumyajit-chakraborty-64a9b022/" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New' , stroke='currentColor';"> 
                                        Check out my LinkedIn profile here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)