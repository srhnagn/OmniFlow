import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import threading
import signal
import sys

# Paths
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
ODOO_BIN = "/Users/serhanagan/Developer/Odoo Core/odoo-bin"
VENV_PYTHON = "/Users/serhanagan/Developer/Odoo Core/venv/bin/python"
CONF_FILE = os.path.join(MODULE_DIR, "odoo.conf")
MODULE_NAME = "omni_flow"

# Global process variable
odoo_process = None

def start_odoo(update=False):
    global odoo_process
    
    # If Odoo is already running, terminate it
    if odoo_process:
        print("Stopping existing Odoo instance...")
        odoo_process.terminate()
        odoo_process.wait()
        
    cmd = [
        VENV_PYTHON,
        ODOO_BIN,
        "-c", CONF_FILE
    ]
    
    if update:
        cmd.extend(["-u", MODULE_NAME])
        print("Starting Odoo and updating module OmniFlow...")
    else:
        print("Starting Odoo...")
        
    odoo_process = subprocess.Popen(cmd)

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_reload = 0
        self.debounce_seconds = 2
        self.timer = None

    def on_any_event(self, event):
        # Ignore changes to git, idea, pycache, etc.
        if '.git' in event.src_path or '.idea' in event.src_path or '__pycache__' in event.src_path:
            return
            
        # Ignore directory modifications (we only care about file changes)
        if event.is_directory:
            return

        print(f"Detected change in: {event.src_path}")
        
        # Debounce to prevent multiple restarts for a single save
        current_time = time.time()
        if current_time - self.last_reload > self.debounce_seconds:
            if self.timer:
                self.timer.cancel()
            
            # Start a timer to actually trigger the reload
            # This handles cases where many files change at once (like a git pull)
            self.timer = threading.Timer(0.5, self.trigger_reload, args=[event.src_path])
            self.timer.start()
            self.last_reload = current_time

    def trigger_reload(self, src_path):
        is_python = src_path.endswith('.py')
        is_xml_or_css = src_path.endswith('.xml') or src_path.endswith('.css') or src_path.endswith('.scss') or src_path.endswith('.js')
        
        if is_python or is_xml_or_css:
            print(f"Triggering restart & module update due to changes...")
            start_odoo(update=True)

def signal_handler(sig, frame):
    print("Exiting...")
    if odoo_process:
        odoo_process.terminate()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start Odoo initially
    start_odoo(update=True)
    
    # Setup watcher
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.join(MODULE_DIR, MODULE_NAME), recursive=True)
    observer.start()
    
    print(f"Watching for file changes in {os.path.join(MODULE_DIR, MODULE_NAME)}...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
