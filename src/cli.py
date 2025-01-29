"""
Command-line interface for the DNS Publisher tool
"""

import argparse
import sys
from .dns_publisher import DNSPublisher

def main():
    parser = argparse.ArgumentParser(description='Public DNS Tool - Publish and monitor URLs')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add URL command
    add_parser = subparsers.add_parser('add', help='Add a new URL')
    add_parser.add_argument('name', help='Name of the project')
    add_parser.add_argument('url', help='URL to monitor')
    add_parser.add_argument('--description', help='Project description')

    # List URLs command
    subparsers.add_parser('list', help='List all URLs')

    # Remove URL command
    remove_parser = subparsers.add_parser('remove', help='Remove a URL')
    remove_parser.add_argument('name', help='Name of the project to remove')

    args = parser.parse_args()
    publisher = DNSPublisher()

    if args.command == 'add':
        url = publisher.add_url(args.name, args.url, args.description)
        print(f"Added URL: {url.name} ({url.url})")
    elif args.command == 'list':
        urls = publisher.get_urls()
        if not urls:
            print("No URLs registered")
            return
        for url in urls:
            status = "✅" if url.is_alive else "❌" if url.is_alive is False else "?"
            print(f"{status} {url.name}: {url.url}")
            if url.description:
                print(f"   {url.description}")
    elif args.command == 'remove':
        publisher.remove_url(args.name)
        print(f"Removed URL: {args.name}")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main() 