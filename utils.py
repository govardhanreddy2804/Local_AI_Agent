from datetime import datetime

def log_interaction(question, answer, filename="history.log"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n\n--- {datetime.now()} ---\n")
        f.write(f"Q: {question}\n")
        f.write(f"A: {answer}\n")
