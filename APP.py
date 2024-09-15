import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(layout="wide")

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background-color: white;
    }
    .nav-items {
        display: flex;
        align-items: center;
    }
    .nav-item {
        margin: 0 1rem;
        color: #1E90FF;
        text-decoration: none;
    }
    .get-started-btn {
        background-color: #FFD700;
        color: black;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        text-decoration: none;
    }
    .language-selector {
        margin-left: 1rem;
    }
    .background-shape {
        position: absolute;
        top: 0;
        left: 0;
        width: 50%;
        height: 80%;
        background-color: #FFD700;
        clip-path: polygon(0 0, 100% 0, 0 100%);
        z-index: -1;
    }
    </style>
    
    <div class="navbar">
        <h3 href="#" >Dreamore</h1>
        <div class="nav-items">
            <a href="#" class="nav-item">Our Solutions</a>
            <a href="#" class="nav-item">Who We Serve</a>
            <a href="#" class="nav-item">Our Results</a>
            <a href="#" class="nav-item">Resources</a>
            <a href="#" class="nav-item">Who We Are</a>
            <a href="#" style='background-color: #FFD700; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;'>Get started →</a>
        </div>
    </div>
    <div class="background-shape"></div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
        <div style="background: url('resources/stretch.jpg') center center; background-size: cover; opacity: 1; padding: 50px;">
            <h1 style='font-size: 48px; font-weight: bold; color: black;'>Sleep health for all</h1>
            <p style='font-size: 24px; color: black;'>We build solutions to make effective sleep health accessible to everyone – anytime, anywhere.</p>
            <a href="#" style='background-color: #FFD700; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 20px;'>Get started →</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("resources/stretch.jpg", use_column_width=True)

def show_about():
    st.title("About Page")
    st.write("This is the about page of the app.")

def show_contact():
    st.title("Contact Page")
    st.write("Feel free to contact us at example@example.com.")

def show_forms():
    st.markdown("""
        <style>
        .title {
            font-size: 60px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .panel {
            background-color: #87CEEB;
            border-radius: 10px;
            padding: 5px 0px 33px 0px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
            max-width: 400px;
            margin: auto;
        }
        
        .form-row {
            text-align: center;
            margin-top: 30px;
        }
        
        .form-label {
            width: 120px;
            margin-right: 10px;
            text-align: left;
        }
        
        .form-input {
            width: 200px;
            border-radius: 10px;
            padding: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="title">Login</div>', unsafe_allow_html=True)
    
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


st.markdown("# Most people in need of sleep health support don't receive it")
st.markdown("In addition to stigma, access to care and financial barriers keep millions from accessing the quality care they need.")

st.markdown("""
    <style>
    .rounded-box {
        background-color: #f8f3f0;
        border-radius: 20px;
        padding: 20px;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .stat-container {
        text-align: center;
    }
    </style>
    
    <div class="rounded-box">
        <div class="stat-container">
            <h2>62%</h2>
            <p>suffers from sleep issues</p>
        </div>
        <div class="stat-container">
            <h2>4.6 years</h2>
            <p>lost from sleep deprivation</p>
        </div>
        <div class="stat-container">
            <h2>73%</h2>
            <p>productivity lost</p>
        </div>
    </div>
    """, unsafe_allow_html=True)



    # import plotly.graph_objects as go

    # fig = go.Figure(data=[go.Pie(labels=['Category A', 'Category B'], values=[65, 35], hole=.3)])
    # fig.update_layout(
    #     autosize=False,
    #     width=200,
    #     height=200,
    #     margin=dict(l=20, r=20, t=20, b=20),
    # )
    # st.plotly_chart(fig)

colB, colG = st.columns([1, 1])

with colB:
    st.image("resources/bad.jpg", use_column_width=True)

with colG:
    st.image("resources/good.jpg", use_column_width=True)

testimonials = [
    {
        "quote": "I wake up refreshed and ready for the day ahead.",
        "author": "Laura Smith, Teacher",
        "image": "teacher.jpg"
    },
]

col3, col4 = st.columns([1, 1])


with col3:
    st.markdown(f"""
<style>
    .testimonial-container {{
        display: flex;
        align-items: center;
        background-color: #FFF5E6;
        padding: 40px;
        border-radius: 20px;
    }}
    .quote-container {{
        flex: 1;
        padding-right: 40px;
    }}
    .image-container {{
        flex: 1;
    }}
    .quote {{
        font-size: 48px;
        font-weight: bold;
        line-height: 1.2;
        margin-bottom: 20px;
    }}
    .author {{
        font-size: 18px;
        color: #666;
    }}
    .read-testimonials {{
        background-color: #FFD700;
        color: black;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin-top: 20px;
        cursor: pointer;
        border-radius: 5px;
        border: none;
    }}
    .nav-buttons {{
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
    }}
    .nav-button {{
        background-color: #FFD700;
        border: none;
        color: black;
        padding: 10px;
        margin-left: 10px;
        cursor: pointer;
        border-radius: 50%;
        font-size: 18px;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .image-container img {{
        width: 100%;
        border-radius: 20px;
    }}
</style>

<div class="testimonial-container" id="testimonial-container">
    <div class="quote-container">
        <p class="quote">"I wake up refreshed and ready for the day ahead."</p>
        <p class="author">Laura Smith, teacher</p>
        <button class="read-testimonials">Read testimonials →</button>
    </div>  
</div>


<script>
    let currentSlide = 0;
    const testimonials = {json.dumps(testimonials)};

    function changeSlide(direction) {{
        currentSlide = (currentSlide + direction + testimonials.length) % testimonials.length;
        updateTestimonial();
    }}

    function updateTestimonial() {{
        const testimonial = testimonials[currentSlide];
        document.querySelector('.quote').textContent = `"${{testimonial.quote}}"`;
        document.querySelector('.author').textContent = testimonial.author;
        document.querySelector('.image-container img').src = testimonial.image;
    }}
</script>
""", unsafe_allow_html=True)

with col4:
    st.image("resources/teacher.jpg", use_column_width=True)


st.markdown("""
<style>
    .footer {
        display: flex;
        flex-direction: column;
        padding: 20px;
        background-color: #222;
        color: white;
    }
    .mission-row {
        width: 100%;
        margin-bottom: 30px;
    }
    .content-row {
        display: flex;
        justify-content: space-between;
    }
    .footer-left {
        flex: 0 0 60%;
        display: flex;
        justify-content: space-between;
    }
    .footer-column {
        flex: 1;
        margin-right: 20px;
    }
    .footer-right {
        flex: 0 0 35%;
    }
    .footer h3 {
        font-size: 18px;
        margin-bottom: 10px;
        color: #888;
    }
    .footer ul {
        list-style-type: none;
        padding: 0;
    }
    .footer li {
        margin-bottom: 5px;
    }
    .footer a {
        text-decoration: none;
        color: white;
    }
    .social-icons {
        display: flex;
        gap: 10px;
    }
    .social-icons img {
        width: 24px;
        height: 24px;
    }
    .subscribe-form input, .subscribe-form select {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #333;
        border: none;
        color: white;
    }
    .subscribe-form button {
        width: 100%;
        padding: 10px;
        background-color: #ffd700;
        border: none;
        cursor: pointer;
        color: black;
    }
</style>

<div class="footer">
    <div class="mission-row">
        <h3 src="resources/night.png" alt="Dreamore" ">Dreamore</h3>
        <p>Our mission is to help millions back to good sleep health with evidence-based digital programs for the most prevalent sleep health conditions.</p>
    </div>
    <div class="content-row">
        <div class="footer-left">
            <div class="footer-column">
                <h3>Company</h3>
                <ul>
                    <li><a href="#">About us</a></li>
                    <li><a href="#">News</a></li>
                    <li><a href="#">Research</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Privacy Policy</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Resources</h3>
                <ul>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">Webinars</a></li>
                    <li><a href="#">Reports</a></li>
                    <li><a href="#">Request Demo</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Who We Serve</h3>
                <ul>
                    <li><a href="#">Employers</a></li>
                    <li><a href="#">Health Plans</a></li>
                    <li><a href="#">Benefits Consultants</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-right">
            <h4>Stay in the loop on the latest in sleep health news</h4>
            <form class="subscribe-form">
                <input type="text" placeholder="First Name*">
                <input type="text" placeholder="Last Name*">
                <input type="email" placeholder="Email Address*">
                <select>
                    <option value="">I am a*</option>
                    <!-- Add options here -->
                </select>
                <input type="text" placeholder="Company Name*">
                <input type="text" placeholder="Job Title*">
                <select>
                    <option value="">Number of Employees Range*</option>
                    <!-- Add options here -->
                </select>
                <select>
                    <option value="">State/Province</option>
                    <!-- Add options here -->
                </select>
                <p>By submitting my email address, I agree to receive occasional emails containing tips, resources, and other promotional materials from Big Health. I understand I can opt out anytime.</p>
                <button type="submit">Subscribe</button>
            </form>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
