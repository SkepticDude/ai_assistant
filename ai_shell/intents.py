from executor import run_command

def handle_intent(text):
    text = text.lower()

    if "open" in text and "brave" in text:
        run_command("brave-browser &")
    elif "open" in text and "steam" in text:
        run_command("steam &")
    elif "list files" in text:
        run_command("ls")
    else:
        print("I don't understand yet.")
