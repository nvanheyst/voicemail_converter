# voicemail_converter
Trancribes .wav files to .txt

# Required Libraries:

**pydub:**
pip install pydub

**ffmpeg (or avconv):**
download and install ffmpeg: https://ffmpeg.org/download.html
add the bin file to PATH

# Background

A transcription is an efficient way to help deliver the voicemail to the right person and know if it's worth listening to

# Current state and future additions

It's not a perfect transcription but can help with a quick understanding of the voicemail

- Could automate this further. Currently automates transciption, but could set it up as a server to automatically trancribe new voicemails as they come in
- Could implement an LLM to automate qualification of the voicemail
