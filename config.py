"""
Configuration file for video downloader.
Contains various presets and settings for different use cases.
"""

# Quality presets
QUALITY_PRESETS = {
    'best': 'best[ext=mp4]/best',
    'high': 'best[height<=1080][ext=mp4]/best[height<=1080]',
    'medium': 'best[height<=720][ext=mp4]/best[height<=720]',
    'low': 'best[height<=480][ext=mp4]/best[height<=480]',
    'audio_only': 'bestaudio[ext=m4a]/bestaudio',
}

# Default yt-dlp options for different scenarios
DEFAULT_OPTIONS = {
    'writeinfojson': True,
    'writesubtitles': True,
    'writeautomaticsub': True,
    'writethumbnail': True,
    'writedesctription': True,
    'embed_subs': True,
    'ignoreerrors': False,
    'no_warnings': False,
    'allow_unplayable_formats': True,  # Allow unusual extensions globally
}

# Options for adult content sites (more permissive)
ADULT_SITE_OPTIONS = {
    'writeinfojson': True,
    'writesubtitles': False,  # Often not available
    'writeautomaticsub': False,
    'writethumbnail': True,
    'writedesctription': False,
    'embed_subs': False,
    'ignoreerrors': True,  # More tolerant of errors
    'no_warnings': True,
    'age_limit': 18,
    'allow_unplayable_formats': True,  # Allow unusual extensions
}

# Common user agents for different scenarios
USER_AGENTS = {
    'chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'safari': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
}

# Site-specific configurations
SITE_CONFIGS = {
    'xhamster.com': {
        'format': 'best[ext=mp4]/best',
        'http_headers': {
            'User-Agent': USER_AGENTS['chrome'],
            'Referer': 'https://xhamster.com/',
        },
        'allow_unplayable_formats': True,  # Allow unusual extensions
        **ADULT_SITE_OPTIONS
    },
    'videa.hu': {
        'format': 'best[ext=mp4]/best',
        'http_headers': {
            'User-Agent': USER_AGENTS['chrome'],
            'Referer': 'https://videa.hu/',
        },
        'allow_unplayable_formats': True,  # Allow unusual extensions for Videa.hu
        'ignoreerrors': True,  # More tolerant of errors
        'no_warnings': True,
        **DEFAULT_OPTIONS
    },
    'youtube.com': {
        'format': 'best[ext=mp4]/best',
        **DEFAULT_OPTIONS
    },
    'vimeo.com': {
        'format': 'best[ext=mp4]/best',
        **DEFAULT_OPTIONS
    }
}
