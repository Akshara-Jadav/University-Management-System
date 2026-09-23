# python + Streamlit project
# Motive of the project is to revise important pythons concept
# University Management System

import streamlit as st

st.set_page_config(
    page_title = "University System",
    layout = "wide"
)

st.title("University Management")

# create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice = st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "List of colleges"
    )
)

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, s):
        self.students.append(s)

    def add_teacher(self, t):
        self.teachers.append(t)

class person:
    def __init__(self, name, branch):
        self.branch = branch
        self.name = name

class student(person):
    def __init__(self, roll, sname, branch):
        self.roll = roll
        super().__init__(sname, branch) # call parent construtor function and store sname

class teacher(person):
    def __init__(self, subject, tname, branch):
            self.subject = subject
            super().__init__(tname, branch)

# based upon college name, college class object is find
def find_college(cname):
    for c in st.session_state.colleges:
        if c.cname == cname:
            return c
    return None

if menu_choice == "Create College":
    cname = st.text_input("Enter new college name")
    if st.button("CREATE"):
        clg_obj = college(cname) # creating a college class object
        st.session_state.colleges.append(clg_obj)  # storing a college class object in college list
        st.success(f"College created successfully : {cname}")

elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please add the college")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        roll = st.number_input("Enter Your roll number", min_value = 1, max_value = 100)
        sname = st.text_input("Enter Student Name")
        branch = st.text_input("Enter your Branch")
        if st.button("ADD STUDENT"):
            if not (roll and sname and clgname and branch):
                st.error("Please don't leave any info blank")
            else:
                clg_obj = find_college(clgname) # find the college
                stu_obj = student(roll, sname, branch) # created studen object
                clg_obj.add_student(stu_obj)
                st.success("Student added successfully")

elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please add the college")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        subject = st.text_input("Enter Your subject")
        tname = st.text_input("Enter teacher Name")
        branch = st.text_input("Enter your Branch")
        if st.button("ADD TEACHER"):
            if not (subject and tname and clgname and branch):
                st.error("Please don't leave any info blank")
            else:
                clg_obj = find_college(clgname) # find the college
                teacher_obj = teacher(subject, tname, branch) # created studen object
                clg_obj.add_teacher(teacher_obj)
                st.success("Teacher added successfully")
        
elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        clg_obj = find_college(clgname)
        st.subheader(f"List of students : {clgname}")
        if clg_obj.students:
            for i, s in enumerate(clg_obj.students, 1):
                st.write(i, " : ", s.name)
        else:
            st.warning("No student found")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        clg_obj = find_college(clgname)
        st.subheader(f"List of teachers : {clgname}")
        if clg_obj.teachers:
            for i, t in enumerate(clg_obj.teachers, 1):
                st.write(i, " : ", t.name)
        else:
            st.warning("No teacher found")

elif menu_choice == "List of colleges":
    st.subheader("List of colleges")
    if not st.session_state.colleges:
            st.info("Please add the college first")
    else:
        for i, c in enumerate(st.session_state.colleges, 1):
            st.write(f"{i} : {c.cname}")