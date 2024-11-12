import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Text to be converted to speech
text = """
Machine Learning: Experienced in building and optimizing machine learning models using frameworks such as Scikit-Learn, TensorFlow, and Keras. 
"""

# Generate and save the speech to an audio file
audio_file = "output_audio.mp3"  # Filename to save the audio
engine.save_to_file(text, audio_file)

# Play the speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()

print(f"Audio saved to '{audio_file}' and played.")
