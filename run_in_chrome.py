import os
import socket
import subprocess
import sys
import time
import webbrowser
from shutil import which

HOST = "localhost"
PORT = 8501
URL = f"http://{HOST}:{PORT}"


def wait_for_server(host: str, port: int, timeout: int = 30) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            try:
                sock.connect((host, port))
                return True
            except OSError:
                time.sleep(0.5)
    return False


def find_chrome() -> str | None:
    candidates = [
        which("chrome"),
        which("chrome.exe"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            return candidate
    return None


if __name__ == "__main__":
    streamlit_cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
    subprocess.Popen(streamlit_cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)

    print("Starting Streamlit server...")
    if wait_for_server(HOST, PORT, timeout=30):
        chrome_path = find_chrome()
        if chrome_path:
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get("chrome").open_new(URL)
        else:
            print("Chrome not found on this system. Opening default browser instead.")
            webbrowser.open_new(URL)
    else:
        print(f"Streamlit server did not start on {URL} within 30 seconds.")
