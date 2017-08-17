# YouTube Watch Later Backup

Scrapes user's Watch Later playlist and backs up the content. Currently only able to back up the first 100 videos.

This script is meant to address the poor design decisions by YouTube, where a deleted video is listed as `[Deleted Video]`, resulting in no details concerning the original video, and thus no good way to locate the content elsewhere.

## Installation

1. Navigate to the script's directory.
2. Run `pip install -r requirements.txt` from Command Prompt/Terminal.

## Usage

1. Open a command line / terminal window in the project directory.
2. Decide on which browser you wish to use to cookies from, and add it as a command-line argument. If no options are chosen, the script will default to using Chrome's cookies.
    - For Chome: Run `python application.py -c`.
    - For Firefox: Run `python application.py -f`.
    - For All browsers: Run `python application.py -a`.  
2. The script will output the backup of the Watch Later playlist.

## Contributing

Contributions / optimizations always welcome.

## License

GNU GPL v3
