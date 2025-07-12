# 📄 Resume Scanner using NLP | Streamlit + Python + spaCy

This project is a **Resume Scanner** built using **Python**, **spaCy**, and **Streamlit**. It allows you to upload a resume in PDF format and extracts key details like:

- ✅ Name
- ✅ Email Address
- ✅ Phone Number
- ✅ Skills
- ✅ Education
- ✅ Work Experience

You can use it in **3 ways**:
1. 📱 Through a **web app UI** using Streamlit  
2. 📓 In an **interactive Colab notebook**  
3. 🖥️ As a **command-line Python script**

---

## 🚀 Features

- Upload resume PDFs and extract structured data
- NLP-based extraction with spaCy and RegEx
- PDF text extraction using PyMuPDF
- Clean and interactive Streamlit interface
- Colab notebook for browser-based use
- CLI version (`resume_scanner.py`) for terminal usage

---

## 📁 Project Structure

| File/Folder           | Description                                  |
|-----------------------|----------------------------------------------|
| `app.py`              | Streamlit app interface                      |
| `resume_parser.py`    | Contains all core resume parsing logic       |
| `resume_scanner.py`   | Command-line tool to extract and print data  |
| `resume_scanner.ipynb`| Google Colab notebook version                |
| `sample_resume.pdf`   | Sample resume for testing                    |
| `requirements.txt`    | All required Python libraries                |
| `README.md`           | This project documentation                   |

---

## 🧠 Tech Stack

- **Python 3**
- [spaCy](https://spacy.io/) – NLP and named entity recognition
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) – PDF text extraction
- [Streamlit](https://streamlit.io/) – Web app framework
- RegEx – for emails and phone number detection

---

## 💻 How to Run the App

### 🔧 1. Install Dependencies

pip install -r requirements.txt

python -m spacy download en_core_web_sm

▶️ Run the Streamlit App

"streamlit run app.py"

If that doesn’t work, use:
"python -m streamlit run app.py" #It will open the app in your browser at http://localhost:8501


🧪 Run in Google Colab

Open resume_scanner.ipynb in Google Colab, upload a resume, and execute all cells to extract the data.


🖥️ Run from Command Line (Optional)

Use the resume_scanner.py script to test parsing directly from terminal:

"python resume_scanner.py sample_resume.pdf " #This will print the extracted data to the console.

📝 Sample Output

Name: John Doe

Email: john.doe@gmail.com

Phone: +91-9876543210

Skills: ['Python', 'SQL', 'Excel']

Education: ['B.Tech', 'M.Tech']

Experience: ['Intern at TCS', 'Data Analyst at XYZ Corp.']


📄 Sample Resume

A sample resume file sample_resume.pdf is included.

You can also upload any resume in PDF format to test your app.

🙋‍♀️ Author

Anuska Saha

📌 GitHub:Anuska-saha-25

🔗 LinkedIn:https://www.linkedin.com/in/anuska-saha-76676a2b0/ 
