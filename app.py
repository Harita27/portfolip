
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    # Your resume data in structured format
    data = {
        'name': 'Harita M U',
        'title': 'Backend Developer',
        'contact': {
            'email': 'haritamu27@gmail.com',
            'phone': '(+91) 6380842816',
            'linkedin': 'www.linkedin.com/in/harita27',
            'github': 'https://github.com/Harita27'
        },
        'summary': 'Engineering student specializing in Backend Development with strong proficiency in Python, Java, Flask, and Django. Skilled in building scalable, secure web applications, RESTful APIs, and database-driven systems.',
        'skills': {
            'languages': ['Python', 'Java', 'C'],
            'frameworks': ['Django', 'Flask'],
            'databases': ['MySQL', 'MongoDB'],
            'web': ['HTML'],
            'version_control': ['Git', 'GitHub'],
            'concepts': ['Data Structures and Algorithms', 'OOP', 'REST API Development', 'Backend Architecture']
        },
        'experience': [
            {
                'title': 'Software Development Engineer Intern',
                'company': 'BlueStock',
                'period': 'Jan 2025 - Feb 2025',
                'location': 'Online',
                'responsibilities': [
                    'Developed backend modules using Python and Flask',
                    'Built and tested REST APIs to support frontend integrations',
                    'Participated in code reviews and optimized backend performance'
                ]
            },
            {
                'title': 'Python Programming Intern',
                'company': 'Codsoft',
                'period': 'June 2024 - July 2024',
                'location': 'Online',
                'responsibilities': [
                    'Designed automation scripts in Python to streamline tasks',
                    'Collaborated on web application projects, applying Flask for server-side development',
                    'Gained hands-on exposure to agile project management'
                ]
            }
        ],
        'projects': [
            {
                'name': 'Cattlex - Livestock Health Monitoring',
                'tech': 'Flask, MySQL',
                'description': [
                    'Developed a web application with user authentication and database integration',
                    'Designed secure backend systems and implemented REST APIs',
                    'Built responsive data input forms and stored health records in MySQL'
                ]
            },
            {
                'name': 'Job Recommendation System',
                'tech': 'Flask, MySQL, REST APIs',
                'description': [
                    'Built a web app to analyze resumes and match with job listings',
                    'Designed RESTful API endpoints to fetch and process real-time job data',
                    'Integrated backend algorithms for skill extraction and matching'
                ]
            }
        ],
        'education': [
            {
                'degree': 'BTech, Artificial Intelligence and Machine Learning',
                'institution': 'St. Joseph\'s College Of Engineering, Chennai',
                'period': '2023 - Present',
                'score': 'CGPA: 9.19'
            },
            {
                'degree': '12th Grade (Higher Secondary)',
                'institution': 'Aditya Vidyashram Residential School, Puducherry',
                'period': '2022 - 2023',
                'score': 'Percentage: 90.6%'
            },
            {
                'degree': '10th Grade (Secondary School)',
                'institution': 'Sai Ram Vidyalaya, Puducherry',
                'period': '2020 - 2021',
                'score': 'Percentage: 95%'
            }
        ],
        'certifications': [
            'Programming, Data Structures and Algorithms using Python - NPTEL',
            'Problem Solving Through Programming in C - NPTEL',
            'Database Management Systems - NPTEL',
            'Java Fundamentals - Oracle Academy'
        ],
        'achievements': [
            'Awarded 10,000 INR cash prize for securing above 9.0 CGPA and being the Department Topper',
            'Solved 1000+ problems on SkillRack and 100+ problems on LeetCode, focusing on DSA',
            'Selected among the Top 70 teams across India in the MHTECHIN Innovation Challenge 2024',
            'Notable participation in IIT Bombay Mapathon for flood risk mapping'
        ]
    }
    
    # Make sure to pass the data to the template
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)