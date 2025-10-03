#!/usr/bin/env python3
"""
Video Downloader Script
Downloads videos from various platforms in original quality and resolution.
"""

import os
import sys
import logging
import argparse
from pathlib import Path
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
import yt_dlp
from config import SITE_CONFIGS, QUALITY_PRESETS, DEFAULT_OPTIONS


class VideoDownloader:
    """Main video downloader class using yt-dlp."""
    
    def __init__(self, download_dir: str = "downloads", log_level: str = "INFO"):
        """
        Initialize the video downloader.
        
        Args:
            download_dir: Directory to save downloaded videos
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        """
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('downloader.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Base yt-dlp configuration
        self.base_opts = {
            'format': 'best[ext=mp4]/best',  # Best quality, prefer mp4
            'outtmpl': str(self.download_dir / '%(title)s.%(ext)s'),
            'extractaudio': False,
            'audioformat': 'best',
            'allow_unplayable_formats': True,  # Allow unusual extensions like v1683208203
            'extractor_args': {
                'xhamster': {'allow_unplayable_formats': True},
                'videa': {'allow_unplayable_formats': True}
            },
            'ignoreerrors': False,  # Will be overridden by site configs if needed
            'no_warnings': False,
        }

    def get_site_config(self, url: str) -> Dict[str, Any]:
        """
        Get site-specific configuration based on URL.

        Args:
            url: Video URL

        Returns:
            Dict with site-specific options
        """
        try:
            domain = urlparse(url).netloc.lower()

            # Check for exact domain match
            for site, config in SITE_CONFIGS.items():
                if site in domain:
                    return config

            # Return default config if no match found
            return {**DEFAULT_OPTIONS, 'format': 'best[ext=mp4]/best'}

        except Exception:
            return {**DEFAULT_OPTIONS, 'format': 'best[ext=mp4]/best'}
    
    def download_video(self, url: str, custom_opts: Optional[Dict[str, Any]] = None) -> bool:
        """
        Download a video from the given URL.

        Args:
            url: Video URL to download
            custom_opts: Custom yt-dlp options to override defaults

        Returns:
            bool: True if download successful, False otherwise
        """
        try:
            self.logger.info(f"Starting download from: {url}")

            # Get site-specific configuration
            site_config = self.get_site_config(url)

            # Merge configurations: base -> site-specific -> custom
            opts = self.base_opts.copy()
            opts.update(site_config)
            if custom_opts:
                opts.update(custom_opts)
            
            # Special handling for sites with unusual extensions
            if 'xhamster.com' in url.lower() or 'videa.hu' in url.lower():
                site_name = "XHamster" if 'xhamster.com' in url.lower() else "Videa.hu"
                self.logger.info(f"{site_name} video detected - using direct yt-dlp with allow_unplayable_formats")
                import subprocess
                import os

                # Use direct yt-dlp command with allow_unplayable_formats
                cmd = [
                    'yt-dlp',
                    '--allow-unplayable-formats',
                    '--format', opts.get('format', 'best'),
                    '--output', opts.get('outtmpl', '%(title)s.%(ext)s'),
                    url
                ]

                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
                    if result.returncode == 0:
                        self.logger.info(f"{site_name} video downloaded successfully via direct yt-dlp")
                        return True
                    else:
                        self.logger.error(f"Direct yt-dlp failed: {result.stderr}")
                        return False
                except Exception as e:
                    self.logger.error(f"Error running direct yt-dlp: {str(e)}")
                    return False

            with yt_dlp.YoutubeDL(opts) as ydl:
                # Extract video info first
                info = ydl.extract_info(url, download=False)
                self.logger.info(f"Video title: {info.get('title', 'Unknown')}")
                self.logger.info(f"Duration: {info.get('duration', 'Unknown')} seconds")
                self.logger.info(f"Uploader: {info.get('uploader', 'Unknown')}")
                
                # Download the video
                ydl.download([url])
                self.logger.info("Download completed successfully!")
                return True
                
        except yt_dlp.DownloadError as e:
            self.logger.error(f"Download error: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            return False
    
    def get_video_info(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Get video information without downloading.
        
        Args:
            url: Video URL
            
        Returns:
            Dict with video information or None if error
        """
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'uploader': info.get('uploader'),
                    'view_count': info.get('view_count'),
                    'upload_date': info.get('upload_date'),
                    'formats': len(info.get('formats', [])),
                    'resolution': info.get('resolution'),
                    'filesize': info.get('filesize'),
                }
        except Exception as e:
            self.logger.error(f"Error getting video info: {str(e)}")
            return None

    def read_urls_from_file(self, file_path: str) -> List[str]:
        """
        Read URLs from a text file.

        Args:
            file_path: Path to the text file containing URLs

        Returns:
            List of valid URLs
        """
        urls = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue

                    # Basic URL validation
                    if line.startswith(('http://', 'https://')):
                        urls.append(line)
                        self.logger.info(f"Added URL from line {line_num}: {line}")
                    else:
                        self.logger.warning(f"Invalid URL on line {line_num}: {line}")

            self.logger.info(f"Loaded {len(urls)} URLs from {file_path}")
            return urls

        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            return []
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {str(e)}")
            return []

    def download_single_video_safe(self, url: str, custom_opts: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Thread-safe wrapper for downloading a single video.

        Args:
            url: Video URL to download
            custom_opts: Custom yt-dlp options

        Returns:
            Dict with download result information
        """
        thread_id = threading.current_thread().ident
        start_time = time.time()

        try:
            self.logger.info(f"[Thread {thread_id}] Starting download: {url}")
            success = self.download_video(url, custom_opts)
            duration = time.time() - start_time

            result = {
                'url': url,
                'success': success,
                'duration': duration,
                'thread_id': thread_id,
                'error': None
            }

            if success:
                self.logger.info(f"[Thread {thread_id}] Completed in {duration:.1f}s: {url}")
            else:
                self.logger.error(f"[Thread {thread_id}] Failed after {duration:.1f}s: {url}")

            return result

        except Exception as e:
            duration = time.time() - start_time
            self.logger.error(f"[Thread {thread_id}] Exception after {duration:.1f}s: {str(e)}")
            return {
                'url': url,
                'success': False,
                'duration': duration,
                'thread_id': thread_id,
                'error': str(e)
            }

    def download_batch(self, urls: List[str], max_workers: int = 3,
                      custom_opts: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Download multiple videos concurrently.

        Args:
            urls: List of video URLs to download
            max_workers: Maximum number of concurrent downloads
            custom_opts: Custom yt-dlp options

        Returns:
            List of download results
        """
        if not urls:
            self.logger.warning("No URLs provided for batch download")
            return []

        self.logger.info(f"Starting batch download of {len(urls)} videos with {max_workers} workers")
        results = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all download tasks
            future_to_url = {
                executor.submit(self.download_single_video_safe, url, custom_opts): url
                for url in urls
            }

            # Process completed downloads
            for future in as_completed(future_to_url):
                result = future.result()
                results.append(result)

                # Log progress
                completed = len(results)
                total = len(urls)
                self.logger.info(f"Progress: {completed}/{total} downloads completed")

        # Summary statistics
        successful = sum(1 for r in results if r['success'])
        failed = len(results) - successful
        total_time = sum(r['duration'] for r in results)

        self.logger.info(f"Batch download completed: {successful} successful, {failed} failed")
        self.logger.info(f"Total processing time: {total_time:.1f}s")

        return results


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description='Download videos in original quality')

    # URL input options (mutually exclusive)
    url_group = parser.add_mutually_exclusive_group(required=False)
    url_group.add_argument('url', nargs='?', help='Single video URL to download')
    url_group.add_argument('-b', '--batch', nargs='?', const='addresses.txt', metavar='FILE',
                          help='Batch download from file (default: addresses.txt)')

    # General options
    parser.add_argument('-d', '--dir', default='downloads',
                       help='Download directory (default: downloads)')
    parser.add_argument('-l', '--log-level', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    parser.add_argument('-i', '--info-only', action='store_true',
                       help='Only show video information, do not download')
    parser.add_argument('-f', '--format',
                       help='Custom format selector (e.g., "best[height<=720]")')

    # Batch download options
    parser.add_argument('-w', '--workers', type=int, default=3,
                       help='Number of concurrent downloads for batch mode (default: 3)')

    args = parser.parse_args()

    # Validate arguments
    if not args.url and not args.batch:
        parser.error("Either provide a URL or use --batch option")
    
    # Initialize downloader
    downloader = VideoDownloader(args.dir, args.log_level)

    # Prepare custom options
    custom_opts = {}
    if args.format:
        custom_opts['format'] = args.format

    if args.batch:
        # Batch download mode
        print(f"Loading URLs from: {args.batch}")
        urls = downloader.read_urls_from_file(args.batch)

        if not urls:
            print("No valid URLs found in the file")
            sys.exit(1)

        if args.info_only:
            # Show info for all URLs
            print(f"\n=== Information for {len(urls)} videos ===")
            for i, url in enumerate(urls, 1):
                print(f"\n--- Video {i}/{len(urls)} ---")
                print(f"URL: {url}")
                info = downloader.get_video_info(url)
                if info:
                    for key, value in info.items():
                        print(f"{key.replace('_', ' ').title()}: {value}")
                else:
                    print("Failed to get video information")
        else:
            # Batch download
            print(f"Starting batch download of {len(urls)} videos with {args.workers} workers")
            results = downloader.download_batch(urls, args.workers, custom_opts)

            # Print summary
            successful = sum(1 for r in results if r['success'])
            failed = len(results) - successful

            print(f"\n=== Download Summary ===")
            print(f"Total videos: {len(results)}")
            print(f"Successful: {successful}")
            print(f"Failed: {failed}")

            if failed > 0:
                print(f"\nFailed downloads:")
                for result in results:
                    if not result['success']:
                        print(f"  - {result['url']}")
                        if result['error']:
                            print(f"    Error: {result['error']}")
                sys.exit(1)

    else:
        # Single URL mode
        if args.info_only:
            # Show video info only
            info = downloader.get_video_info(args.url)
            if info:
                print("\n=== Video Information ===")
                for key, value in info.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("Failed to get video information")
                sys.exit(1)
        else:
            # Download single video
            success = downloader.download_video(args.url, custom_opts)
            if not success:
                sys.exit(1)


if __name__ == "__main__":
    main()
