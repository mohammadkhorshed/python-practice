# Simple Youtube Video Downloader

from pytube import YouTube
from pathlib import Path

def download_video():
    url = input("Enter YouTube Video URL: ")

    try:
        yt = YouTube(url)
        print(f"\nVideo: {yt.title}")

        streams = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution')
        if not streams:
            print("No downloadable video streams found!")
            return

        print("\nAvailable resolutions:")
        for  idx, stream in enumerate(streams):
            resolution = stream.resolution or "Unknown"
            filesize_mb = stream.filesize / (1024 * 1024) if stream.filesize else 0
            print(f"{idx + 1}. {resolution} ({filesize_mb:.1f} MB)")
        
        choice = input("\nEnter number for the resolution: ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(streams)):
            print("Invalid choice! Exiting.")
            return

        selected = streams[int(choice) - 1]

        print(f"\n Downloading {selected.resolution} version...")
        download_path = str(Path.home() / "Downloads")
        selected.download(output_path = download_path)
        print(f"\nDownload complete! Saved to {download_path}")
    
    except Exception as e:
        print(f"Error: {e}")

download_video()