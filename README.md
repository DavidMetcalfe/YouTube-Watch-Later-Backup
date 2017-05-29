# YouTube Watch Later Backup

Scrapes user's Watch Later playlist and backs up the content. Currently only able to back up the first 100 videos.

This script is meant to address the poor design decisions by YouTube, where a deleted video is listed as `[Deleted Video]`, resulting in no details concerning the original video, and thus no good way to locate the content elsewhere.

## Installation

1. Navigate to the script's directory.
2. Run `pip install -r requirements.txt` from Command Prompt/Terminal.

## Usage

**Note:** Currently the script is configured to use Chrome's cookies under `browsercookie.chrome()`

1. Run `python application.py`. 
2. The script will output the backup of the Watch Later playlist.

## Contributing

Contributions / optimizations always welcome.

## License

GNU GPL v3
