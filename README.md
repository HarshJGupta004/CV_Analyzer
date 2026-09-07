# Intelligent CV Scoring Engine

An AI-powered CV analysis application built with Python and Streamlit. The application allows users to upload a CV in PDF format and uses a Large Language Model (LLM) to analyze the CV and generate an overall score based on skills, experience, achievements, clarity, formatting, and overall impression.

## Features

* Upload CVs in PDF format
* Extract text automatically from uploaded CVs
* Preview the extracted CV content
* AI-powered CV analysis using Groq
* Extract:

  * Name and contact details
  * Professional summary
  * Key skills
* CV scoring out of 100
* Score breakdown by category
* Visual score chart
* Overall score progress indicator
* Environment variables for securely storing API credentials

## Scoring Criteria

The CV is evaluated using the following criteria:

| Category                  | Maximum Score |
| ------------------------- | ------------: |
| Skills Match              |            30 |
| Experience & Achievements |            30 |
| Clarity & Formatting      |            20 |
| Overall Impression        |            20 |
| **Total**                 |       **100** |

## Tech Stack

* **Python**
* **Streamlit** – Web application interface
* **Groq API** – AI-powered CV analysis
* **Llama 3.1 8B Instant** – Language model
* **PyPDF2** – PDF text extraction
* **Pandas** – Score data processing
* **python-dotenv** – Environment variable management
* **JSON / Regex** – Processing AI-generated score data

## Project Structure

```text
CV_Analyzer/
│
├── main.py
├── README.md
├── .gitignore
├── .env
└── venv/
```

> `venv/` and `.env` should NOT be uploaded to GitHub.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CV_Analyzer.git
cd CV_Analyzer
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If activation is successful, your terminal should look similar to:

```text
(venv) PS C:\Users\...\CV_Analyzer>
```

### 4. Install dependencies

```powershell
pip install streamlit groq PyPDF2 python-dotenv pandas
```

### 5. Create the `.env` file

Create a file named:

```text
.env
```

Inside it, add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do not share your API key or commit the `.env` file to GitHub.

The project already includes `.env` in `.gitignore`.

## Running the Application

Make sure the virtual environment is activated:

```powershell
venv\Scripts\Activate.ps1
```

Then run:

```powershell
streamlit run main.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser.

## How It Works

1. The user uploads a CV in PDF format.
2. PyPDF2 extracts text from each page.
3. The extracted text is cleaned using regular expressions.
4. The CV content is sent to the Groq API.
5. The Llama model analyzes the CV.
6. The model returns the requested information and scoring data.
7. The application extracts the JSON score data.
8. Pandas converts the scores into a DataFrame.
9. Streamlit displays the score breakdown as a chart.
10. The total CV score is displayed out of 100.

## Environment Variables

The application requires the following environment variable:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never hard-code your API key directly into the Python source code.

## Future Improvements

Possible improvements include:

* Job description matching
* ATS compatibility scoring
* Resume keyword analysis
* Skill-gap identification
* Personalized improvement suggestions
* Resume section detection
* Multiple CV comparison
* Downloadable CV analysis reports
* Improved JSON response validation
* Support for DOCX resumes
* Database storage for analysis history
* User authentication

## Author

**Harsh Gupta**

---

## License

This project is intended for educational and portfolio purposes.
