"""
DNS Publisher - Core module for publishing and monitoring URLs
"""

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

@dataclass
class ProjectURL:
    name: str
    url: str
    description: Optional[str] = None
    last_checked: Optional[str] = None
    is_alive: Optional[bool] = None
    added_date: Optional[str] = None

class DNSPublisher:
    def __init__(self, storage_path: str = None):
        self.storage_path = storage_path or str(Path.home() / '.public_dns_tool' / 'urls.json')
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Ensure the storage directory and file exist"""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump([], f)
    
    def add_url(self, name: str, url: str, description: str = None) -> ProjectURL:
        """Add a new URL to monitor"""
        urls = self.get_urls()
        new_url = ProjectURL(
            name=name,
            url=url,
            description=description,
            added_date=datetime.now().isoformat(),
            is_alive=None
        )
        urls.append(new_url.__dict__)
        self._save_urls(urls)
        return new_url
    
    def get_urls(self) -> List[ProjectURL]:
        """Get all registered URLs"""
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
        return [ProjectURL(**url) for url in data]
    
    def _save_urls(self, urls: List[dict]):
        """Save URLs to storage"""
        with open(self.storage_path, 'w') as f:
            json.dump([url for url in urls], f, indent=2)
    
    def remove_url(self, name: str):
        """Remove a URL by name"""
        urls = self.get_urls()
        urls = [url.__dict__ for url in urls if url.name != name]
        self._save_urls(urls) 