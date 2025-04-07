import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Greg Liszt</h4>
        <p>Recent Bachelor's Graduate in EECS<br>
        Massachusetts Institute of Technology.<br>
        77 Massachusetts Avenue, Cambridge, MA 02139, USA<br>
        <a href="mailto:greg.lizst@gmail.com">greg.lizst@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.JPG")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=150)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a current undergraduate student in Computer Science and Engineering at the Massachusetts Institute of Technology (MIT), seeking to apply my knowledge and skills in a professional setting. During my academic journey, I developed a solid foundation in programming, system design, and algorithms.

        As part of my program, I completed several projects that involved working with real-world datasets and applying various computer science techniques. These projects provided hands-on experience in software development, data analysis, and machine learning.

        I am committed to leveraging technology to drive innovation and solve complex problems. I am a quick learner, a collaborative team player, and possess strong problem-solving skills. I look forward to contributing my skills and growing as a computer science professional in a dynamic and challenging environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow, Keras
        - Database: SQL, MongoDB
        - Data Visualization: Tableau, Power BI
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Technical Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
