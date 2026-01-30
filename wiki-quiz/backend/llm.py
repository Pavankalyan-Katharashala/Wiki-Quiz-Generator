from google import genai
import json

# 🔑 Use your VALID key (hardcoded for now to avoid env issues)
client = genai.Client(
    api_key="AIzaSyAOpDBOyzNhOFfpD_eit85JU3WG9cY0VqQ"
)

def generate_quiz_and_topics(text: str):
    prompt = f"""
You are an AI that generates quizzes strictly from the given Wikipedia content.

TASK:
- Generate 5 to 10 multiple-choice questions.
- Each question must include:
  - Question text
  - 4 options (A–D)
  - Correct answer
  - Difficulty (easy, medium, hard)
  - Short explanation explaining WHY the answer is correct
- Suggest 5 related Wikipedia topics for further reading.

RULES:
- Use ONLY the provided content.
- Do NOT add outside knowledge.
- Output MUST be valid JSON ONLY (no markdown, no commentary).

FORMAT:
{{
  "quiz": [
    {{
      "question": "...",
      "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
      "answer": "A. ...",
      "difficulty": "easy|medium|hard",
      "explanation": "..."
    }}
  ],
  "related_topics": ["Topic1", "Topic2", "Topic3", "Topic4", "Topic5"]
}}

CONTENT:
{text[:12000]}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    result = json.loads(clean_text)

    return result["quiz"], result["related_topics"]
