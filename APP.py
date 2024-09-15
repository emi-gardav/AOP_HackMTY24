import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image
import streamlit.components.v1 as components
# from streamlit_extras.altex import hist_chart
# import plotly.figure_factory as ff
# import numpy as np
# import plotly.graph_objects as go
# from os import path
import io
import base64

add_logo("http://placekitten.com/120/120")

# Helper function to convert an image to base64
def get_image_as_base64(image_obj):
    buffered = io.BytesIO()
    image_obj.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Function to display the home page
def show_home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    
    # Load images
    image1_path = Image.open("C:\\Users\\mrivera6\\Documents\\Visual Studio 2022\\Projects\\Python\\TigreHacks 2024\\Image (1).jfif")
    image2_path = Image.open("C:\\Users\\mrivera6\\Documents\\Visual Studio 2022\\Projects\\Python\\TigreHacks 2024\\Image.jfif")
    image1 = get_image_as_base64(image1_path)
    image2 = get_image_as_base64(image2_path)
    
    # List of images and their corresponding labels
    # images = {
        # "": image1_path,
        # " ": image2_path
    # }

    # style="margin-left: 320px;"
    # style="margin-left: 10px;"
    
    # HTML for radio buttons and image display
    components.html(f"""
        <div class="panel" style="background-color: black; padding: 20px; border-radius: 10px; max-width: 600px; margin: auto;">
            <div class="image-container" style="text-align: center;">
                <img id="displayed-image" src="data:image/jpeg;base64,{image1}" style="max-width: 100%; border-radius: 10px;">
            </div>
            
            <div class="radio-container" style="text-align: center; margin-top: 20px;">
                <input type="radio" name="image-select" value="Image 1" id="radio1" class="radio-button" checked>
                <input type="radio" name="image-select" value="Image 2" id="radio2" class="radio-button" style="margin-left: 15px;">
            </div>
        </div>
        
        <script>
        const image1 = "data:image/jpeg;base64,{image1}";
        const image2 = "data:image/jpeg;base64,{image2}";
        
        document.querySelectorAll('input[name="image-select"]').forEach(function(radio) {{
            radio.addEventListener('change', function(event) {{
                const selectedValue = event.target.value;
                const imageElement = document.getElementById('displayed-image');
                
                if (selectedValue === "Image 1") {{
                    imageElement.src = image1;
                }} else if (selectedValue === "Image 2") {{
                    imageElement.src = image2;
                }}
            }});
        }});
        </script>
    """, height=600)
    
    # elements.radio("Select Image", options=list(images.keys()), key='radio_buttons')
        # Panel container
        # st.markdown('<div class="panel">', unsafe_allow_html=True)

        # Display the selected image
        # selected_image = st.radio("Select Image", options=list(images.keys()), key='image_selector')

        # Display image
        # st.markdown('<div class="image-container">', unsafe_allow_html=True)
        # st.image(images[selected_image], use_column_width=True)
        # st.markdown('</div>', unsafe_allow_html=True)

        # Display the radio buttons inside the panel
        # st.markdown('<div class="radio-buttons">', unsafe_allow_html=True)
        # st.radio("Select Image", options=list(images.keys()), key='radio_buttons')
        # st.markdown('</div>', unsafe_allow_html=True)

        # End of panel container
        # st.markdown('</div>', unsafe_allow_html=True)
    
    # Radio button to select the image
    # selected_image = st.radio("Select Image", options=list(images.keys()))

    # Display the selected image
    # st.image(images[selected_image], use_column_width=True)
    
    # Sample data for the pie chart
    # labels = ['A', 'B', 'C', 'D']
    # values = [10, 20, 30, 40]
    
    # Create a pie chart using Plotly
    # fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    # Display the pie chart in Streamlit
    # st.plotly_chart(fig)

# Function to display the about page
def show_about():
    st.title("About Page")
    st.write("This is the about page of the app.")

# Function to display the contact page
def show_contact():
    st.title("Contact Page")
    st.write("Feel free to contact us at example@example.com.")

def show_forms():
    # st.title("Login")
    
    # CSS for aligning label and input fields on the same line
    st.markdown("""
        <style>
        .title {
            font-size: 60px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;  /* Space below the title */
        }
        
        .panel {
            background-color: #87CEEB;  /* Sky blue color */
            border-radius: 10px;
            padding: 5px 0px 33px 0px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
            max-width: 400px;  /* Adjust the width of the panel */
            margin: auto;  /* Center the panel horizontally */
        }
        
        .form-row {
            text-align: center;
            margin-top: 30px;
        }
        
        .form-label {
            width: 120px;  /* Adjust label width to fit input fields */
            margin-right: 10px;  /* Space between label and input */
            text-align: left;  /* Align text to the right */
        }
        
        .form-input {
            width: 200px;  /* Adjust input field width */
            border-radius: 10px;
            padding: 5px;  /* Add some padding inside the input field */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title
    st.markdown('<div class="title">Login</div>', unsafe_allow_html=True)
    
    # Panel container with the title and form fields inside
    st.markdown("""
        <div class="panel">
            <div class="form-row">
                <label class="form-label">User</label>
                <input class="form-input" type="text" id="user" style="margin-right: 5px;">
            </div>
            <div class="form-row">
                <label class="form-label">Password</label>
                <input class="form-input" type="password" id="password">
            </div>
        </div>
    """, unsafe_allow_html=True)

# Horizontal menu bar using buttons
# st.markdown("""
#     <style>
#     .menu-bar button {
#         display: inline-block;
#         margin-right: 10px;
#         padding: 10px;
#         font-size: 16px;
#     }
    
#      .flex-container {
#         display: flex;
#         align-items: center;
#         margin-bottom: 20px;
#     }
    
#     .sidebar-image {
#         width: 50px;  /* Adjust the width of the image */
#         margin-right: 10px;
#     }
    
#     .sidebar-text {
#         font-size: 16px;
#         font-weight: bold;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# Horizontal menu bar using buttons
st.markdown("""
    <style>
    .menu-bar button {
        display: inline-block;
        margin-right: 10px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Create buttons for navigation
col1, col2, col3, col4 = st.columns(4)
# image_path = path.join(path.dirname(path.abspath(__file__)), 'assign.png')
# menu = st.sidebar.header("Settings")
# menu = st.sidebar.image(user)

# image_base64 = get_image_as_base64(image_path)

# Sidebar content with image and text in the same row using flexbox
# st.sidebar.markdown(f"""
#     <div class="flex-container">
#         <img src="data:image/png;base64,{image_base64}" alt="User Image" class="sidebar-image">
#         <span class="sidebar-text">User123</span>
#     </div>
#     """, unsafe_allow_html=True)

with col1:
    home = st.button("Home")
with col2:
    about = st.button("About")
with col3:
    contact = st.button("Contact")
with col4:
    form = st.button("Get Started!")

# Determine which page to show based on button clicks
if home:
    show_home()
elif about:
    show_about()
elif contact:
    show_contact()
elif form:
    show_forms()
else:
    show_home()  # Default to home page
