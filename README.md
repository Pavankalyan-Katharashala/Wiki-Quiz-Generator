# Wiki-Quiz-Generator
Wiki Quiz Generator 🧠📚
=======================

A full-stack web application that generates intelligent quizzes from any Wikipedia article using
web scraping and a free-tier Large Language Model (LLM). The system dynamically creates multiple-
choice questions, explanations, difficulty levels, and related topics for further reading.

--------------------------------------------------
PROJECT OVERVIEW
--------------------------------------------------

The Wiki Quiz Generator allows users to:
- Paste a Wikipedia article URL
- Automatically extract article content
- Generate 5–10 quiz questions using an LLM
- View previously generated quizzes
- Reopen full quiz details from history

The application is designed to be simple, minimal, and user-friendly, while demonstrating
real-world integration of scraping, AI, backend APIs, and frontend UI.

--------------------------------------------------
TECHNOLOGIES USED
--------------------------------------------------

Backend:
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- BeautifulSoup (Web Scraping)

LLM:
- Google Gemini (Free Tier)
- Model used: gemini-flash-latest

Frontend:
- HTML
- CSS (Modern, minimal UI with animated gradient background)
- JavaScript (Fetch API)

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

wiki-quiz-app/
│
├── backend/
│   ├── main.py            # FastAPI routes
│   ├── database.py        # Database connection
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── scraper.py         # Wikipedia scraping (BeautifulSoup)
│   ├── llm.py             # Gemini LLM integration
│   ├── crud.py            # Database operations
│   └── prompts/           # Prompt templates
│
├── frontend/
│   └── index.html         # UI (Tabs, Modal, Styling)
│
├── sample_data/
│   ├── urls.txt
│   └── sample_outputs.json
│
└── README.txt

--------------------------------------------------
FEATURES
--------------------------------------------------

TAB 1 – Generate Quiz
- Accepts any Wikipedia URL
- Scrapes article content
- Generates quiz using Gemini LLM
- Displays:
  • Question
  • Options (A–D)
  • Correct answer
  • Difficulty level
  • Explanation
  • Related topics

TAB 2 – Past Quizzes (History)
- Displays all previously processed Wikipedia URLs
- Shows article title and URL
- “Details” button opens a modal with full quiz content

--------------------------------------------------
HOW IT WORKS
--------------------------------------------------

1. User enters a Wikipedia URL
2. BeautifulSoup scrapes the article content
3. Clean text is sent to Gemini LLM
4. Gemini generates:
   - Quiz questions
   - Explanations
   - Difficulty levels
   - Related topics
5. Results are stored in SQLite
6. User can revisit quizzes via History tab

--------------------------------------------------
SETUP INSTRUCTIONS
--------------------------------------------------

1. Clone the repository
   git clone <your-github-repo-url>
   cd wiki-quiz-app

2. Install dependencies
   pip install fastapi uvicorn sqlalchemy requests beautifulsoup4 google-genai

3. Add your Gemini API key
   - Create a key at https://aistudio.google.com/app/apikey
   - Paste it inside backend/llm.py (temporary for demo)

4. Run the backend
   python -m uvicorn backend.main:app

5. Open the application
   - API Docs: http://127.0.0.1:8000/docs
   - Frontend: open frontend/index.html in browser

--------------------------------------------------
API ENDPOINTS
--------------------------------------------------

POST /generate-quiz
- Input: Wikipedia URL
- Output: Quiz JSON

GET /history
- Returns list of all generated quizzes

GET /quiz/{id}
- Returns full quiz details for selected article

--------------------------------------------------
LLM USAGE EXPLANATION
--------------------------------------------------

The project uses Google Gemini (free-tier) to generate quiz content dynamically.
The model processes scraped Wikipedia text and produces structured quiz data
including explanations and difficulty levels.

The architecture is LLM-agnostic and can support other free-tier models if required.

--------------------------------------------------
FUTURE ENHANCEMENTS
--------------------------------------------------

- User authentication
- Quiz scoring and evaluation
- Export quizzes as PDF
- Dark mode toggle
- Support for multiple languages

--------------------------------------------------
DISCLAIMER
--------------------------------------------------

This project is for educational purposes only.
Wikipedia content is used under its respective license.
API keys should not be exposed in public repositories.

--------------------------------------------------
AUTHOR
--------------------------------------------------

Developed by: <Your Name>
Project Type: Academic / Learning Project
