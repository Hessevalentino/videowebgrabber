#!/usr/bin/env python3
"""
Batch Video Downloader
Simple wrapper for batch downloading videos from addresses.txt file.
"""

import sys
from video_downloader import VideoDownloader


def main():
    """Simple batch downloader that reads from addresses.txt."""
    
    print("=== Batch Video Downloader ===")
    print("Reading URLs from addresses.txt...")
    
    # Initialize downloader
    downloader = VideoDownloader("downloads", "INFO")
    
    # Read URLs from file
    urls = downloader.read_urls_from_file("addresses.txt")
    
    if not urls:
        print("❌ No valid URLs found in addresses.txt")
        print("Please add video URLs to addresses.txt (one per line)")
        sys.exit(1)
    
    print(f"📋 Found {len(urls)} URLs to download")
    
    # Ask user for confirmation
    response = input(f"Start downloading {len(urls)} videos? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Download cancelled")
        sys.exit(0)
    
    # Ask for number of workers
    try:
        workers = int(input("Number of concurrent downloads (1-5, default 3): ") or "3")
        workers = max(1, min(5, workers))  # Limit between 1-5
    except ValueError:
        workers = 3
    
    print(f"🚀 Starting batch download with {workers} workers...")
    
    # Start batch download
    results = downloader.download_batch(urls, workers)
    
    # Print final summary
    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful
    
    print(f"\n{'='*50}")
    print(f"📊 FINAL SUMMARY")
    print(f"{'='*50}")
    print(f"✅ Successful downloads: {successful}")
    print(f"❌ Failed downloads: {failed}")
    print(f"📁 Files saved to: downloads/")
    
    if failed > 0:
        print(f"\n❌ Failed URLs:")
        for result in results:
            if not result['success']:
                print(f"   • {result['url']}")
                if result['error']:
                    print(f"     Error: {result['error']}")
    
    print(f"\n🎉 Batch download completed!")


if __name__ == "__main__":
    main()
