# OnePager
Overview
The OnePager Generator is a sophisticated application powered by the cutting-edge technology of OpenAI's GPT-4 model. It leverages the power of natural language processing to generate a OnePager document based on user inputs. The application is built with Streamlit, a fast, user-friendly framework that turns data scripts into shareable web apps.
Architecture

The application is divided into three main Python scripts: online_app.py, login.py, and main_app.py.
online_app.py
This is the entry point of the application. It sets the page configuration, applies custom CSS to hide the Streamlit toolbar and footer, and manages the user session state. Depending on the user's login status, it either displays the login form or the main application.
login.py
This script handles user authentication. It uses Pyrebase, a Python wrapper for the Firebase API, to authenticate users. Upon successful login, the user's session state is updated, granting them access to the main application. Firebase provides a secure and scalable authentication system, ensuring that only authorized users can access the application.
main_app.py
This is where the magic happens. The script uses the OpenAI API to generate a OnePager document based on various user inputs, including sender, recipient, context, document structure, formality, technicality, length, source description, call to action, action tone, additional information, and a PDF with background information. The application then generates a OnePager document and displays it in markdown format. The user can also download the document as a Word file.
Advanced Features
Natural Language Processing
The application uses OpenAI's GPT-4 model, a state-of-the-art language model that uses machine learning to generate human-like text. This allows the application to generate high-quality OnePager documents that are tailored to the user's inputs.
User Authentication
The application includes a secure login system that uses Firebase for authentication. Firebase is a comprehensive app development platform that provides a robust and secure authentication system. This ensures that only authorized users can access the main application.
Interactive User Interface
The application uses Streamlit to create an interactive user interface with various input fields and sliders. This allows users to customize their OnePager documents to their specific needs.
Document Download
The application allows users to download their generated OnePager documents as Word files. This makes it easy for users to save and share their documents.
Dependencies

The application relies on several Python libraries, including Streamlit for the web interface, Pyrebase for user authentication, OpenAI for natural language processing, PyPDF2 for PDF reading, BeautifulSoup for HTML parsing, and docx for Word document creation.
Usage

1. Run the online_app.py script to start the Streamlit application.
2. If you are not logged in, you will see the login form. Enter your username and password and click the 'Log In' button.
3. If you are logged in, you will see the main application. Enter the required information and click the 'Generate' button to generate a OnePager document.
4. You can view the generated document in the application and download it as a Word file.
Note
This application uses OpenAI's GPT-4 model, which requires an API key. The API key is stored in Streamlit's secrets, so you need to set up your Streamlit secrets before running the application.



lastly the key has to be updated all the time

