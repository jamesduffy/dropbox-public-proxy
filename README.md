# dropbox-public-proxy
Make your Dropbox Public folder public again!

On September 1, 2017 Dropbox will disable the Public folder that was once found in Dropbox. I have shared a ton of GIFs using the Alfred Workflow originally developed by [Jonnie Hallman](http://destroytoday.com/writings/gif-workflow/).

This is a simple Flask app that will look in your /Public Dropbox folder for a file and stream that file to the browser.

# Setup

1. Go to the [Dropbox Developers Portal](https://www.dropbox.com/developers/apps)
   - Select `Dropbox API`
   - Select `Full Dropbox` (This is required to read your existing Public folder)
   - Give your app a name
2. Go to the new App's setting page
   - Generate Personal Access Token
3. Copy the `config.py.example` to `config.py`
4. Copy your Personal Access token and save in `config.py`
5. Install the project requirements `pip install -r requirements.txt`
6. Setup AWS Lambda config `zappa init`
7. Deploy to AWS Lambda `zappa deploy dev`
