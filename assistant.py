from executor import run_command
from intents import handle_intent

while True:
    user_input = input("assistant> ").strip()

    if user_input in ("exit", "quit"):
        break

    if user_input.startswith("!"):
        run_command(user_input[1:])
    else:
        handle_intent(user_input)
