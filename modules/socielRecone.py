#!/usr/bin/env python3
"""
Social Media Reconnaissance Module
"""

import requests
import json
import re
from datetime import datetime

class SocialRecon:
    def __init__(self, username):
        self.username = username
        self.results = {
            "username": username,
            "timestamp": datetime.now().isoformat(),
            "platforms": {}
        }
    
    def scan_instagram(self):
        try:
            url = f"https://www.instagram.com/{self.username}/"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Extract profile data
                if 'profile_pic_url' in response.text:
                    self.results["platforms"]["instagram"] = {
                        "exists": True,
                        "url": url,
                        "public": "private" not in response.text.lower()
                    }
                else:
                    self.results["platforms"]["instagram"] = {"exists": False}
            else:
                self.results["platforms"]["instagram"] = {"exists": False}
        except:
            self.results["platforms"]["instagram"] = {"error": "Connection failed"}
    
    def scan_twitter(self):
        try:
            url = f"https://twitter.com/{self.username}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200 and "This account doesn’t exist" not in response.text:
                self.results["platforms"]["twitter"] = {
                    "exists": True,
                    "url": url
                }
            else:
                self.results["platforms"]["twitter"] = {"exists": False}
        except:
            self.results["platforms"]["twitter"] = {"error": "Connection failed"}
    
    def scan_github(self):
        try:
            url = f"https://api.github.com/users/{self.username}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.results["platforms"]["github"] = {
                    "exists": True,
                    "name": data.get("name"),
                    "bio": data.get("bio"),
                    "location": data.get("location"),
                    "public_repos": data.get("public_repos"),
                    "followers": data.get("followers"),
                    "following": data.get("following"),
                    "url": data.get("html_url")
                }
            else:
                self.results["platforms"]["github"] = {"exists": False}
        except:
            self.results["platforms"]["github"] = {"error": "Connection failed"}
    
    def scan_tiktok(self):
        try:
            url = f"https://www.tiktok.com/@{self.username}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200 and "This user does not exist" not in response.text:
                self.results["platforms"]["tiktok"] = {
                    "exists": True,
                    "url": url
                }
            else:
                self.results["platforms"]["tiktok"] = {"exists": False}
        except:
            self.results["platforms"]["tiktok"] = {"error": "Connection failed"}
    
    def scan_facebook(self):
        try:
            url = f"https://www.facebook.com/{self.username}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200 and "Page Not Found" not in response.text:
                self.results["platforms"]["facebook"] = {
                    "exists": True,
                    "url": url
                }
            else:
                self.results["platforms"]["facebook"] = {"exists": False}
        except:
            self.results["platforms"]["facebook"] = {"error": "Connection failed"}
    
    def scan_all(self):
        print(f"\n{YELLOW}[*] Scanning {self.username} on all platforms...{RESET}")
        
        platforms = [
            self.scan_instagram,
            self.scan_twitter,
            self.scan_github,
            self.scan_tiktok,
            self.scan_facebook
        ]
        
        for platform in platforms:
            platform()
            time.sleep(0.5)
        
        return self.results
