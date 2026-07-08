#!/usr/bin/env python3
"""
Plex Picker - Local Server
Run this to serve the app on your local network.
Your iPhone must be on the same WiFi.

The console window hides itself a few seconds after startup — look for the
icon near your clock to open the app or quit the server.
"""
import http.server, socket, os, sys, threading, webbrowser, ctypes

PORT = 8765
DIR = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        pass  # suppress request logs

def hide_console():
    if os.name == 'nt':
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE

def show_console():
    if os.name == 'nt':
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 5)  # SW_SHOW

def main():
    os.chdir(DIR)
    ip = get_local_ip()
    url = f"http://{ip}:{PORT}"

    httpd = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    # Open the app in the default browser on launch (handy for the desktop shortcut)
    threading.Timer(0.8, lambda: webbrowser.open(f"http://localhost:{PORT}/plex_picker.html")).start()

    print("=" * 45)
    print("  Plex Picker is running!")
    print("=" * 45)
    print(f"\n  On your iPhone (same WiFi):")
    print(f"  {url}\n")
    print("  Steps:")
    print("  1. Open that URL in Safari")
    print("  2. Tap the Share button (box with arrow)")
    print("  3. Tap 'Add to Home Screen'")
    print("  4. Tap 'Add' — done!\n")

    try:
        import pystray
        from PIL import Image
    except ImportError:
        print("  [tray icon unavailable — run: pip install pystray pillow]")
        print("  Press Ctrl+C to stop the server.")
        print("=" * 45)
        try:
            server_thread.join()
        except KeyboardInterrupt:
            print("\nServer stopped.")
        return

    print("  This window will hide itself — look for the icon near your")
    print("  clock to open the app, show this window, or quit the server.")
    print("=" * 45)

    icon_image = Image.open(os.path.join(DIR, "icon.png"))

    def on_open(icon, item):
        webbrowser.open(url)

    def on_show_console(icon, item):
        show_console()

    def on_quit(icon, item):
        icon.stop()
        httpd.shutdown()

    menu = pystray.Menu(
        pystray.MenuItem(f"Open Plex Picker", on_open, default=True),
        pystray.MenuItem("Show console / logs", on_show_console),
        pystray.MenuItem("Quit", on_quit),
    )
    icon = pystray.Icon("PlexPicker", icon_image, "Plex Picker", menu)

    hide_console()
    icon.run()

if __name__ == "__main__":
    main()
