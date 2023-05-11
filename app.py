from unicodedata import name
import streamlit as st
import streamlit.components.v1 as stc 


html_temp = """
		<div style="background-color:#DFE2DB;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Flood Risk Predictor App</h1>
		<h2 style="color:white;text-align:center;">Pattaya City </h2>
		</div>
		"""

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def main():
    	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)
	st.write("""
			### Flood Risk Predictor App
			This dataset contains physical data
			#### Pattaya Events
			    https://www.pattayacityevents.com/TH/home.html.
			#### App Content
				- Map Section: Flood Hazard Map (Static Map)
				- ML Map Section: Flood Hazard Map (Interactive Map)

			""")

	st.subheader("About")
	st.text("atomsiwawut@gmail.com")
	st.text("By Siwawut Pattanasri)")

if __name__ == '__main__':
	main()
    
