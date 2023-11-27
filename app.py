from rpunct import RestorePuncts
import streamlit as st
# The default language is 'english'
rpunct = RestorePuncts()
r = rpunct.punctuate("Hello my name is Marcello how are you")
st.write(r)
