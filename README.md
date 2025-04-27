# Backend Developer Portfolio

A clean, responsive portfolio website built with Flask, HTML, and CSS to showcase my backend development skills, projects, and experience.

## Overview

This portfolio application is built using Flask, a lightweight Python web framework. It demonstrates my ability to create structured, data-driven web applications with clean code and professional presentation.

## Features

- **Dynamic Content Rendering**: Portfolio data is stored in Python dictionaries and rendered using Flask templates
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Clean UI**: Modern, professional design with carefully chosen typography and color scheme
- **Organized Sections**: Clearly presents skills, experience, projects, education, and achievements
- **Low Code, High Impact**: Achieves an impressive result with minimal code

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS
- **Templates**: Jinja2 (Flask's templating engine)
- **Icons**: Font Awesome

## Project Structure

```
portfolio/
│
├── app.py                 # Flask application with portfolio data and routes
├── templates/
│   └── index.html         # HTML template with Jinja2 for dynamic content
├── static/
│   └── styles.css         # CSS styling
└── README.md              # Project documentation
```

## Installation & Setup

1. Clone the repository
   ```
   git clone https://github.com/Harita27/portfolio.git
   cd portfolio
   ```

2. Create a virtual environment (optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Flask
   ```
   pip install flask
   ```

4. Run the application
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`

## Customization

The portfolio is designed to be easily customizable:

- Update your information in the `data` dictionary in `app.py`
- Modify colors by changing the CSS variables in `styles.css`
- Add new sections by extending the HTML template and data structure

## Learning Goals

This project demonstrates:
- Backend data structuring and template rendering
- Responsive web design principles
- Clean code organization
- Effective presentation of professional qualifications

## Future Enhancements

Potential improvements for future versions:
- Database integration for dynamic content management
- Contact form with email functionality
- Dark/light theme toggle
- Project filtering capabilities
- Blog section with Flask-based CMS

## About Me

Backend developer specializing in Python, Flask, and Django with experience building scalable web applications and RESTful APIs. Passionate about clean code, system design, and solving real-world programming challenges.

## Contact

- Email: haritamu27@gmail.com
- Phone: (+91) 6380842816  
- LinkedIn: [www.linkedin.com/in/harita27](https://www.linkedin.com/in/harita27)
- GitHub: [github.com/Harita27](https://github.com/Harita27)

## License

This project is open source and available under the [MIT License](LICENSE).