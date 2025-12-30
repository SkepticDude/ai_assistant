from .executor import run_command


def handle_intent(text: str):
    """Very small intent handler (placeholder).

    This module is intentionally minimal; the real intent parsing should
    be provided by an external model via `LOCAL_AI_CMD` or a hosted API.
    """
    text = (text or "").lower()

    if "open" in text and "brave" in text:
        run_command("brave-browser &")
    elif "open" in text and "steam" in text:
        run_command("steam &")
    elif "list files" in text:
        run_command("ls")
    else:
        print("I don't understand yet.")
