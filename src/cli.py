from .intents import handle_intent
from .executor import run_command


def main():
    while True:
        try:
            user_input = input("assistant> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if user_input in ("exit", "quit"):
            break
        if not user_input:
            continue
        if user_input.startswith("!"):
            run_command(user_input[1:])
            continue
        handle_intent(user_input)


if __name__ == '__main__':
    main()
