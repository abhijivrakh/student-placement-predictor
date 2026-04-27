import streamlit as st
from src.predict import predict

st.set_page_config(
    page_title="Student Placement Intelligence System",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.header-box {
    background: linear-gradient(135deg, #111827, #1f2937);
    color: white;
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-box">
    <h1>🎓 Student Placement Intelligence System</h1>
    <h4>Developed by: Abhishek Jivrakh</h4>
    <p>
    An AI-powered placement prediction system built for training institutes to identify
    student placement readiness using academic performance, technical skills,
    project work, attendance, communication ability, and overall readiness score.
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("🏢 Business Context", expanded=True):
    st.write("""
    This project was designed for a training institute environment where mentors and placement teams
    need to track student readiness before campus drives or company interviews.

    Instead of judging students manually, this system provides a data-driven placement prediction
    based on measurable learning and readiness indicators.
    """)

with st.expander("📊 Dataset & Features Used"):
    st.write("""
    The model uses student-level training and readiness data.

    **Input Features:**
    - Maths Score
    - Python Score
    - SQL Score
    - Attendance Percentage
    - Number of Mini Projects
    - Communication Score
    - Placement Readiness Score

    **Target:**
    - Placement outcome: Placed / Not Placed

    This type of dataset is useful for institutes because it connects technical learning,
    consistency, project exposure, and interview readiness with placement probability.
    """)

with st.expander("🤖 Model Purpose"):
    st.write("""
    The model predicts whether a student is likely to be placed and provides a probability score.

    This helps the institute:
    - Identify students who are interview-ready
    - Find students who need extra mentoring
    - Improve training batches using data
    - Prioritize mock interviews and revision sessions
    - Track placement preparation progress
    """)

with st.expander("⚙️ Production Readiness"):
    st.write("""
    This system is designed as a production-ready ML application.

    **Production/MLOps Components:**
    - Modular prediction function using `src.predict`
    - Streamlit frontend
    - Docker-ready project structure
    - CI/CD-ready deployment workflow
    - Easy model updates when new student data is collected

    Because the prediction logic is separated from the frontend, the model can be retrained,
    updated, and redeployed without changing the complete application.
    """)

st.divider()

st.subheader("📝 Enter Student Details")

left, right = st.columns(2)

with left:
    maths = st.number_input("Maths Score", min_value=0, max_value=100, step=1)
    python_score = st.number_input("Python Score", min_value=0, max_value=100, step=1)
    sql = st.number_input("SQL Score", min_value=0, max_value=100, step=1)
    attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, step=1)

with right:
    mini_projects = st.number_input("Number of Mini Projects", min_value=0, step=1)
    communication = st.number_input("Communication Score (1–10)", min_value=1, max_value=10, step=1)
    readiness = st.number_input("Placement Readiness Score", min_value=0, max_value=100, step=1)

st.divider()

if st.button("Predict Placement Readiness", use_container_width=True):
    input_data = {
        "Maths": maths,
        "Python": python_score,
        "SQL": sql,
        "Attendance": attendance,
        "Mini_Projects": mini_projects,
        "Communication_Score": communication,
        "Placement_Readiness_Score": readiness
    }

    prediction, probability = predict(input_data)

    st.subheader("📌 Prediction Result")

    col1, col2, col3 = st.columns(3)

    col1.metric("Placement Prediction", "Likely" if prediction == 1 else "Unlikely")
    col2.metric("Placement Probability", f"{probability:.2f}")
    col3.metric("Risk Level", "Low" if probability >= 0.70 else "Medium" if probability >= 0.45 else "High")

    if prediction == 1:
        st.success(
            f"✅ Student is likely to be placed with a probability of {probability:.2f}."
        )
        st.info("""
        Recommendation: This student appears placement-ready. The institute can prioritize
        company-specific preparation, mock interviews, resume polishing, and final HR practice.
        """)
    else:
        st.error(
            f"⚠️ Student is currently unlikely to be placed with a probability of {probability:.2f}."
        )
        st.warning("""
        Recommendation: This student needs additional support. Focus areas may include
        Python/SQL revision, mini projects, attendance improvement, communication practice,
        and placement readiness mentoring.
        """)

    st.subheader("📊 Student Skill Snapshot")

    skill_data = {
        "Maths": maths,
        "Python": python_score,
        "SQL": sql,
        "Attendance": attendance,
        "Readiness": readiness
    }

    st.bar_chart(skill_data)

st.markdown("---")
st.caption(
    "🎓 Student Placement Intelligence System | Built for Training Institutes | "
    "Docker + CI/CD Ready | Developed by Abhishek Jivrakh"
)
