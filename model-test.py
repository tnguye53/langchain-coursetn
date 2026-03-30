from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

CANDIDATE_MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-pro-latest",
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
]

def first_working_model():
    for model_name in CANDIDATE_MODELS:
        try:
            llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
            resp = llm.invoke("Reply with only: ok")
            print(f"[OK] {model_name} -> {resp.content}")
            return llm
        except Exception as e:
            print(f"[FAIL] {model_name} -> {type(e).__name__}: {e}")
    raise RuntimeError("No candidate model worked for this API key/project.")

if __name__ == "__main__":
    first_working_model()