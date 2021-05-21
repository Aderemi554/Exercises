import torch
import streamlit as st
from transformers import pipeline
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os 

summarizer = pipeline("summarization")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



st.markdown(' # **Research Literature Summarizer**')
st.image('./images/papers.png')
expander = st.sidebar.beta_expander('Want to try it out?')
expander.markdown('[click here for demo](https://ded-detector.uc.r.appspot.com)')



expander = st.sidebar.beta_expander('Meet the developer')
expander.image('./images/Aderemi_net_9760.jpg')
expander.write('Aderemi Fayoyiwa')
#expander.markdown('[Email](https://mail.google.com/mail/u/0/?fs=1&to=aderemifayoyiwa@gmail.com&su=SUBJECT&body=BODY&tf=cm)')
expander.markdown('[Email](https://mail.google.com/mail/u/0/?fs=1&to=aderemifayoyiwa@gmail.com&su=SUBJECT&body=BODY&tf=cm)   [GitHub](https://github.com/AderemiF)   [Linkedin](https://www.linkedin.com/in/aderemi-fayoyiwa)')

 
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('RLS - summarizer')
#if pressed:
#	left_column.image('images\retina.jpg')
    #left_column.write('Welcome on board!')

st.markdown('# Introduction')
st.markdown(' ### Irrespective of whether there would be a scientific publication or not, most research projects begin with literature review.')
st.markdown(' ##### \nAs the name implies, literature review involves going through related published research papers to see what has already been established in the research area. \nLiterature review answers some research questions and in some cases raises more research questions. \nsResearchers also use literature review to validate/corroborate their research findings.')
st.markdown(' ##### \nResearchers spend significant amount of time reviewing published research papers that are related to their current project or potential research publication. \nAbout half of the research papers reviewed end up not being relevant to the project or publication at hand. \nDepending on how we look at it, but it can be said that half of that time is wasted. \nIf the time lost was be somewhat saved, it can be put into more productive use, say expanding the scope of research or invested in writing research reports or paper.')


st.markdown(' # Problem Statement')
st.markdown('##### \n * A significant percentage of the total research time goes into literature review. \n * Often times, over half of these literatures do not contain any useful information pertaining to the research at hand.')

st.markdown('# Goal')
st.markdown(' ##### \nThe goal of this project is: \n * To create an application that can effectively summarize research papers. \n * To significantly reduce the amount of time researchers spend on literature review. \n * To summarize research papers in a way that keeps vital information intact.')

st.markdown('# Target')
st.markdown(' ##### \nThe target audience of the RLS are: \n * Researchers \n * University students \n * High school students')


st.markdown('# Summarizer')
expander = st.beta_expander('Model')
expander.write("NLP transformer: Huggingface's pretrained transformer")
expander.write('pipeline: summarization')


expander = st.beta_expander('Technologies Used')
expander.write('Python')
expander.write('Github/Git')
expander.write('Jupyter')
expander.write('Streamlit')
expander.write('Streamlitshare')



st.markdown('# Challenges')
expander = st.beta_expander('Limitations')
expander.write('Suitable pdf converter')
expander.write('Token constraint')


expander = st.beta_expander('What next?')
expander.write('Further optimiztion of the summarizer')
expander.write('Commercialize RLS')


#file = st.file_uploader('upload your demo file') 




