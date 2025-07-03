from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random string

# 20 Registration numbers for direct access
REGISTRATION_NUMBERS = [
    "23129001", "23129002", "23129003", "23129004", "23129005",
    "23129006", "23129007", "23129008", "23129009", "23129010",
    "23129011", "23129012", "23129013", "23129014", "23129015",
    "23129016", "23129017", "23129018", "23129019", "23129020"
]

# Sample user data for demonstration
SAMPLE_USERS = {
    "23129001": {
        "name": "1",
        "email": "1@alumni.edu",
        "skills": "Python, Machine Learning, Data Analysis",
        "department": "Computer Science",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 8.9, Dean's List 2022, Hackathon Winner"
    },
    "23129002": {
        "name": "2",
        "email": "2@alumni.edu",
        "skills": "JavaScript, React, Node.js",
        "department": "Information Technology",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.5, Coding Club President"
    },
    "23129003": {
        "name": "3",
        "email": "3@alumni.edu",
        "skills": "Java, Spring Boot, Microservices",
        "department": "Software Engineering",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.7, Internship at Infosys"
    },
    "23129004": {
        "name": "4",
        "email": "4@alumni.edu",
        "skills": "UI/UX Design, Figma, Adobe Creative Suite",
        "department": "Design",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 9.1, Design Competition Winner"
    },
    "23129005": {
        "name": "5",
        "email": "5@alumni.edu",
        "skills": "C++, Game Development, Unity",
        "department": "Game Development",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.3, Game Jam Finalist"
    },
    "23129006": {
        "name": "6",
        "email": "6@alumni.edu",
        "skills": "DevOps, AWS, Docker, Kubernetes",
        "department": "Information Systems",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.8, AWS Certified"
    },
    "23129007": {
        "name": "7",
        "email": "7@alumni.edu",
        "skills": "Cybersecurity, Network Security, Ethical Hacking",
        "department": "Cybersecurity",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 9.0, CTF Winner"
    },
    "23129008": {
        "name": "8",
        "email": "8@alumni.edu",
        "skills": "Mobile Development, Swift, iOS",
        "department": "Mobile Computing",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.6, App Launch Award"
    },
    "23129009": {
        "name": "9",
        "email": "9@alumni.edu",
        "skills": "Blockchain, Solidity, Smart Contracts",
        "department": "Blockchain Technology",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.4, Blockchain Hackathon Finalist"
    },
    "23129010": {
        "name": "10",
        "email": "10@alumni.edu",
        "skills": "Data Science, R, Statistical Analysis",
        "department": "Data Science",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 9.2, Data Science Symposium Speaker"
    },
    "23129011": {
        "name": "11",
        "email": "11@alumni.edu",
        "skills": "Cloud Computing, Azure, Google Cloud",
        "department": "Cloud Computing",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.7, Google Cloud Certified"
    },
    "23129012": {
        "name": "12",
        "email": "12@alumni.edu",
        "skills": "Product Management, Agile, Scrum",
        "department": "Business Administration",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.5, Product Club Lead"
    },
    "23129013": {
        "name": "13",
        "email": "13@alumni.edu",
        "skills": "Full Stack Development, MERN Stack",
        "department": "Web Development",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 8.9, Webathon Winner"
    },
    "23129014": {
        "name": "14",
        "email": "14@alumni.edu",
        "skills": "Artificial Intelligence, TensorFlow, PyTorch",
        "department": "Artificial Intelligence",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 9.0, AI Research Paper"
    },
    "23129015": {
        "name": "15",
        "email": "15@alumni.edu",
        "skills": "Database Design, SQL, NoSQL",
        "department": "Database Systems",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.6, DBMS Project Award"
    },
    "23129016": {
        "name": "16",
        "email": "16@alumni.edu",
        "skills": "Digital Marketing, SEO, Social Media",
        "department": "Marketing",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 8.8, Social Media Campaign Winner"
    },
    "23129017": {
        "name": "17",
        "email": "17@alumni.edu",
        "skills": "System Architecture, Enterprise Solutions",
        "department": "Systems Engineering",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.7, System Design Competition"
    },
    "23129018": {
        "name": "18",
        "email": "18@alumni.edu",
        "skills": "Quality Assurance, Testing, Automation",
        "department": "Quality Assurance",
        "year_of_graduation": "2021",
        "academic_record": "CGPA: 8.5, QA Automation Project"
    },
    "23129019": {
        "name": "19",
        "email": "19@alumni.edu",
        "skills": "Business Intelligence, Tableau, Power BI",
        "department": "Business Intelligence",
        "year_of_graduation": "2023",
        "academic_record": "CGPA: 8.9, BI Dashboard Award"
    },
    "23129020": {
        "name": "20",
        "email": "20@alumni.edu",
        "skills": "Project Management, Leadership, Strategy",
        "department": "Management",
        "year_of_graduation": "2022",
        "academic_record": "CGPA: 8.6, Project Expo Winner"
    }
}

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        reg_number = request.form['reg_number'].strip()
        
        if reg_number in REGISTRATION_NUMBERS:
            session['reg_number'] = reg_number
            session['user'] = SAMPLE_USERS[reg_number]
            return redirect('/main')
        else:
            return render_template('login.html', error="Invalid registration number. Please try again.")
    
    return render_template('login.html')

@app.route('/main')
def main():
    if 'reg_number' in session and 'user' in session:
        return render_template('main.html', user=session['user'])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/confirm-logout')
def confirm_logout():
    session.clear()
    return redirect('/login')

@app.route('/registration-numbers')
def show_registration_numbers():
    """Route to display all valid registration numbers (for testing purposes)"""
    return render_template('registration_numbers.html', numbers=REGISTRATION_NUMBERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
