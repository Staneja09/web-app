import streamlit as st
import pandas as pd

def load_scholarship_data():
    # Load the scholarships data from a CSV file
    scholarships = pd.read_csv('scholarships.csv')
    return scholarships

def scholarship_finder():
    st.title("Scholarship Finder")
    st.write("Find scholarships based on your qualifications and interests.")

    # Load scholarship data
    scholarships = load_scholarship_data()

    # User inputs for qualifications and interests
    qualification = st.selectbox("Select Your Qualification", options=scholarships['Qualification'].unique())
    interest = st.selectbox("Select Your Interest", options=scholarships['Interest'].unique())

    if st.button("Find Scholarships"):
        # Filter scholarships based on user inputs
        filtered_scholarships = scholarships[
            (scholarships['Qualification'] == qualification) & 
            (scholarships['Interest'] == interest)
        ]

        if not filtered_scholarships.empty:
            st.write("### Scholarships Found:")
            for index, row in filtered_scholarships.iterrows():
                st.write(f"**Name:** {row['Name']}")
                st.write(f"**Qualification:** {row['Qualification']}")
                st.write(f"**Interest:** {row['Interest']}")
                st.write(f"**Deadline:** {row['Deadline']}")
                st.write(f"**Application Tips:** {row['Application_Tips']}")
                st.write("---")
        else:
            st.write("No scholarships found for your selected qualifications and interests.")

def load_career_data():
    # Load the careers data from a CSV file
    careers = pd.read_csv('careers.csv')
    return careers

def career_exploration_tool():
    st.title("Career Exploration Tool")
    st.write("Explore potential careers based on your interests and skills.")

    # Load career data
    careers = load_career_data()

    # User inputs for skills and interests
    skills = st.multiselect("Select Your Skills", options=careers['Skills'].unique())
    interests = st.multiselect("Select Your Interests", options=careers['Interests'].unique())

    if st.button("Explore Careers"):
        # Filter careers based on user inputs
        filtered_careers = careers[
            careers['Skills'].apply(lambda x: any(skill in x for skill in skills)) &
            careers['Interests'].apply(lambda x: any(interest in x for interest in interests))
        ]

        if not filtered_careers.empty:
            st.write("### Potential Careers:")
            for index, row in filtered_careers.iterrows():
                st.write(f"**Career:** {row['Career']}")
                st.write(f"**Required Skills:** {row['Skills']}")
                st.write(f"**Interests:** {row['Interests']}")
                st.write(f"**Education Requirement:** {row['Education_Requirement']}")
                st.write(f"**Job Prospects:** {row['Job_Prospects']}")
                st.write("---")
        else:
            st.write("No careers found based on your selected skills and interests.")


