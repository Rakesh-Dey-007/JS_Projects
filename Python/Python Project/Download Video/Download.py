from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length, "seconds")
    print("Description: ", yt.description)
    print("Ratings: ", yt.rating)

    # Get the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Download completed!!")


# url = input("Enter the YouTube video URL: ")
url = "https://youtu.be/CYLkFD1z8DU?si=mvE7GR-zsaV5gG72"
download_video(url)

# Example usage
# download_youtube_video(url, output_path='F:\VS_CODING\Advance_PYTHON\Python Project\Download Video')