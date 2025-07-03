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
    "23129001": {"name": "1", "email": "1@alumni.edu", "skills": "Python, Machine Learning, Data Analysis"},
    "23129002": {"name": "2", "email": "2@alumni.edu", "skills": "JavaScript, React, Node.js"},
    "23129003": {"name": "3", "email": "3@alumni.edu", "skills": "Java, Spring Boot, Microservices"},
    "23129004": {"name": "4", "email": "4@alumni.edu", "skills": "UI/UX Design, Figma, Adobe Creative Suite"},
    "23129005": {"name": "5", "email": "5@alumni.edu", "skills": "C++, Game Development, Unity"},
    "23129006": {"name": "6", "email": "6@alumni.edu", "skills": "DevOps, AWS, Docker, Kubernetes"},
    "23129007": {"name": "7", "email": "7@alumni.edu", "skills": "Cybersecurity, Network Security, Ethical Hacking"},
    "23129008": {"name": "8", "email": "8@alumni.edu", "skills": "Mobile Development, Swift, iOS"},
    "23129009": {"name": "9", "email": "9@alumni.edu", "skills": "Blockchain, Solidity, Smart Contracts"},
    "23129010": {"name": "10", "email": "10@alumni.edu", "skills": "Data Science, R, Statistical Analysis"},
    "23129011": {"name": "11", "email": "11@alumni.edu", "skills": "Cloud Computing, Azure, Google Cloud"},
    "23129012": {"name": "12", "email": "12@alumni.edu", "skills": "Product Management, Agile, Scrum"},
    "23129013": {"name": "13", "email": "13@alumni.edu", "skills": "Full Stack Development, MERN Stack"},
    "23129014": {"name": "14", "email": "14@alumni.edu", "skills": "Artificial Intelligence, TensorFlow, PyTorch"},
    "23129015": {"name": "15", "email": "15@alumni.edu", "skills": "Database Design, SQL, NoSQL"},
    "23129016": {"name": "16", "email": "16@alumni.edu", "skills": "Digital Marketing, SEO, Social Media"},
    "23129017": {"name": "17", "email": "17@alumni.edu", "skills": "System Architecture, Enterprise Solutions"},
    "23129018": {"name": "18", "email": "18@alumni.edu", "skills": "Quality Assurance, Testing, Automation"},
    "23129019": {"name": "19", "email": "19@alumni.edu", "skills": "Business Intelligence, Tableau, Power BI"},
    "23129020": {"name": "20", "email": "20@alumni.edu", "skills": "Project Management, Leadership, Strategy"}
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
