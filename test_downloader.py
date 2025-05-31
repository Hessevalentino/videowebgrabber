#!/usr/bin/env python3
"""
Test script for video downloader functionality.
"""

import os
import sys
from video_downloader import VideoDownloader


def test_url_reading():
    """Test reading URLs from addresses.txt."""
    print("🧪 Testing URL reading from addresses.txt...")
    
    downloader = VideoDownloader("test_downloads", "INFO")
    urls = downloader.read_urls_from_file("addresses.txt")
    
    print(f"✅ Found {len(urls)} URLs")
    for i, url in enumerate(urls[:3], 1):  # Show first 3
        print(f"   {i}. {url}")
    
    if len(urls) > 3:
        print(f"   ... and {len(urls) - 3} more")
    
    return len(urls) > 0


def test_video_info():
    """Test getting video information."""
    print("\n🧪 Testing video info extraction...")
    
    downloader = VideoDownloader("test_downloads", "INFO")
    urls = downloader.read_urls_from_file("addresses.txt")
    
    if not urls:
        print("❌ No URLs found")
        return False
    
    # Test first URL
    test_url = urls[0]
    print(f"Testing URL: {test_url}")
    
    info = downloader.get_video_info(test_url)
    if info:
        print("✅ Video info extracted successfully:")
        print(f"   Title: {info.get('title', 'Unknown')}")
        print(f"   Duration: {info.get('duration', 'Unknown')} seconds")
        print(f"   Resolution: {info.get('resolution', 'Unknown')}")
        print(f"   Formats available: {info.get('formats', 'Unknown')}")
        return True
    else:
        print("❌ Failed to extract video info")
        return False


def test_site_config():
    """Test site-specific configuration."""
    print("\n🧪 Testing site-specific configuration...")
    
    downloader = VideoDownloader("test_downloads", "INFO")
    
    test_urls = [
        "https://cz.xhamster.com/videos/test",
        "https://www.youtube.com/watch?v=test",
        "https://vimeo.com/test",
        "https://unknown-site.com/video"
    ]
    
    for url in test_urls:
        config = downloader.get_site_config(url)
        domain = url.split('/')[2]
        print(f"   {domain}: {len(config)} config options")
    
    print("✅ Site configuration working")
    return True


def main():
    """Run all tests."""
    print("🚀 Video Downloader Test Suite")
    print("=" * 40)
    
    tests = [
        test_url_reading,
        test_video_info,
        test_site_config,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The downloader is ready to use.")
        print("\n💡 Quick start:")
        print("   1. Add URLs to addresses.txt")
        print("   2. Run: python batch_downloader.py")
        print("   3. Or: python video_downloader.py -b")
    else:
        print("⚠️  Some tests failed. Check the configuration.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
