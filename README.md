# YouTube Downloader

YouTube Downloader is a web application that allows you to download videos or audio files from YouTube.

## Features

- Download YouTube videos in MP4 format.
- Download YouTube audio files in MP3 format.

## Prerequisites

Before running this application locally, make sure you have the following installed on your machine:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Flask: You can install it by running the following command: `pip install flask`
- pytube: You can install it by running the following command: `pip install pytube`

## Installation

1. Clone this GitHub repository to your local machine: `git clone https://github.com/yanislabbe/youtube-video-downloader.git`
2. Navigate to the project directory: `cd youtube-video-downloader`
3. Install the required dependencies by running the following command: `pip install -r requirements.txt`
4. Run the application by executing the `youtube.py` file: `python youtube.py`

## Usage

1. Access the application in your browser by opening the following URL: [https://yanislabbe.pythonanywhere.com/](https://yanislabbe.pythonanywhere.com/)
2. Paste the YouTube video link into the text field and select the desired format (video or audio).
3. Click the "Download" button to download the file.

**Note:** Please be aware that due to the hosting platform limitations, video/audio downloads may not work on the provided link.

## Project Structure

The project structure is as follows:

- `youtube.py`: The main file containing the application logic and Flask routes.
- `templates`: This directory contains the `youtube.html` file that defines the structure of the web page.
- `static`: This directory contains the CSS (`youtube.css`) and JavaScript (`youtube.js`) files used for styling and web page functionality.
- `tmp`: This directory is used to temporarily store the downloaded files before sending them as a response.

## Contributions

Contributions to this project are welcome. If you would like to add features, fix bugs, or improve the documentation, feel free to create a pull request.

## Disclaimer

This application is intended for personal use and should not be used to infringe on copyright or violate YouTube's terms of service. Make sure to obtain the necessary permissions before downloading a video.

## Author

[yanislabbe](https://github.com/yanislabbe)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Please see the `LICENSE` file for more information.
