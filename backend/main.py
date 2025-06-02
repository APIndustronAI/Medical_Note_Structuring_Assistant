from fastapi import FastAPI, Form
import requests

app = FastAPI()

def ollama_llama(prompt : str):
    response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama2", "prompt": prompt, "stream": False}
    )
    return response.json()["response"].strip()

@app.post("/extract/")
def llama_MedReport(note: str=Form(...)):
    prompt = (
  f"""You are a medical assistant specialized in analyzing clinical notes.

Task:
Extract the following structured information from the doctor's note below:
- symptoms
- diagnosis
- medications
- Follow-up Instructions

Instructions:
- Return the result strictly in **valid JSON format**.
- Do not include any additional text or explanations.
- If a section is not mentioned, return its value as an empty list or null.

Doctor's Note:
\"\"\"
{note}
\"\"\" """

)
    structured_data = ollama_llama(prompt)
    return {"structured": structured_data}