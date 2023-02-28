import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.title('Onlei Technology')
st.header('By Shruti')
st.text('This is a tutorial on stramlit library')
st.image('C:/Users/Shruti/AppData/Local/Programs/Python/Python311/greenary.jpg')

if mymenu=="Home":
	st.markdown('<center><h1>WELCOME</h1>',unsafe_allow_html=True)
	st.video('https://youtu.be/TKTCdN51dig')
elif mymenu=="FillForm":
	with st.form('My Form'):
		name=st.text_input('Enter Name')
		dob=st.date_input('Choose DOB')
		marks=st.slider('Choose Marks')
		k=st.form_submit_button('Submit Form')
		if  k:
			st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif mymenu=="Downloads":
	st.header('Downloads')
	st.download_button('Download now','hello this is the downloaded data','onlei.txt')