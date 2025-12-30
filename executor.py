import os
import signal
import subprocess
import readline
import sys

HISTORY_FILE = os.path.expanduser("~/.ai_assistant_history")
HISTORY_LENGTH = 1000


def _setup_readline():
    try:
        readline.read_history_file(HISTORY_FILE)
    except FileNotFoundError:
        pass
    readline.set_history_length(HISTORY_LENGTH)
    try:
        readline.parse_and_bind("tab: complete")
    except Exception:
        pass


def _save_history():
    try:
        readline.write_history_file(HISTORY_FILE)
    except Exception:
        pass


def run_command(cmd):
    """Run a shell command, forwarding SIGINT to the child process group.

    Returns the child process return code, or 1 on error.
    """
    if not cmd or not cmd.strip():
        return 0
    try:
        # Start the subprocess in its own process group so we can forward signals
        proc = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
        try:
            return proc.wait()
        except KeyboardInterrupt:
            # Forward Ctrl+C to the child process group
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGINT)
            except Exception:
                pass
            proc.wait()
            return proc.returncode
    except Exception as e:
        print("Error:", e)
        return 1


def interactive_shell(prompt='> '):
    """Simple interactive shell with history and line-editing.

    - Up/Down arrows work via readline history.
    - Ctrl+C during input cancels the current prompt.
    - Ctrl+C while a child is running is forwarded to the child.
    - Ctrl+D (EOF) or typing `exit`/`quit` exits cleanly and saves history.
    """
    _setup_readline()
    try:
        while True:
            try:
                line = input(prompt)
            except EOFError:
                print()
                break
            except KeyboardInterrupt:
                # User pressed Ctrl+C at prompt — show a fresh prompt
                print()
                continue

            line = line.strip()
            if not line:
                continue
            if line in ("exit", "quit"):
                break
            # add to history and run
            try:
                readline.add_history(line)
            except Exception:
                pass
            run_command(line)
    finally:
        _save_history()


if __name__ == '__main__':
    try:
        interactive_shell()
    except KeyboardInterrupt:
        # Ensure a clean exit on Ctrl+C at top-level
        print()
        sys.exit(0)
