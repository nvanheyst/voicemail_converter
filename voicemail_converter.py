# Explanation:
# Pydub: We use pydub to load the file and convert it to a more compatible format if it's in a non-PCM encoding (like format 49).
# Format Conversion: The audio is converted to 16kHz, mono, which is optimal for speech recognition.
# Required Libraries:
# Install pydub:
# pip install pydub
# If you haven’t installed ffmpeg (or avconv), you can download it or use a similar tool to ensure pydub can decode the non-PCM audio:

# ffmpeg: Download and install ffmpeg (then add to path)
# Once pydub and ffmpeg (or another backend) are properly set up, this program should be able to handle non-PCM audio formats and transcribe them.



from pydub import AudioSegment
import speech_recognition as sr
import os

def convert_audio(input_file, output_file):
    try:
        
        audio = AudioSegment.from_file(input_file)
        audio = audio.set_channels(1)  
        audio = audio.set_frame_rate(16000)
        audio.export(output_file, format="wav")
        print(f"Converted audio saved as: {output_file}")
        return output_file
    except Exception as e:
        print(f"Error during audio conversion: {e}")
        return None

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio)
        print("Speech (.WAV) to text automatic transcription: ", transcription)
        return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return None


def save_transcription_to_file(transcription, audio_file_path):
    text_file_path = os.path.splitext(audio_file_path)[0] + '.txt'
    try:
        with open(text_file_path, 'w') as text_file:
            text_file.write(transcription)
        print(f"Transcription saved to: {text_file_path}")
    except Exception as e:
        print(f"Error writing transcription to file: {e}")

def main(input_audio_file):
    converted_audio_file = "converted_audio.wav"
    
    processed_file = convert_audio(input_audio_file, converted_audio_file)
    
    if processed_file:
        transcription = transcribe_audio(processed_file)
        
        if transcription:
            save_transcription_to_file(transcription, input_audio_file)


# Replace this with the path to your WAV audio file
input_audio_file = R"C:\Users\nvheyst\Downloads\msg1626.WAV"  # Change this to your actual file path


if __name__ == "__main__":
    main(input_audio_file)

