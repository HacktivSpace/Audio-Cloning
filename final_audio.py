import json
import numpy as np
import librosa
from itertools import chain
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# List of audio file paths (update this list with your audio files)
audio_files = ['1.wav', '2.wav', '3.wav']  # Add your audio file paths here

# Initialize lists to store features
mfcc_list = []
spectral_centroid_list = []
chroma_stft_list = []
spectral_bandwidth_list = []
rms_list = []
zero_crossing_rate_list = []

# Function to calculate average of a list of features
def calculate_average(feature_list):
    flat_list = list(chain.from_iterable(feature_list)) if any(isinstance(i, list) for i in feature_list) else feature_list
    return sum(flat_list) / len(flat_list) if flat_list else 0

# Extract features from each audio file
for file in audio_files:
    y, sr = librosa.load(file)

    # Calculate features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)

    # Append to lists
    mfcc_list.append(np.mean(mfcc, axis=1).tolist())
    spectral_centroid_list.append(spectral_centroid[0].tolist())
    chroma_stft_list.append(chroma_stft[0].tolist())
    spectral_bandwidth_list.append(spectral_bandwidth[0].tolist())
    rms_list.append(rms[0].tolist())
    zero_crossing_rate_list.append(zero_crossing_rate[0].tolist())

# Calculate average features to create a preset
preset = {
    'mfcc': calculate_average(mfcc_list),
    'spectral_centroid': calculate_average(spectral_centroid_list),
    'chroma_stft': calculate_average(chroma_stft_list),
    'spectral_bandwidth': calculate_average(spectral_bandwidth_list),
    'rms': calculate_average(rms_list),
    'zero_crossing_rate': calculate_average(zero_crossing_rate_list),
    'brightness': 'bright' if calculate_average(spectral_centroid_list) > 2000 else 'dark',
    'noisiness': 'noisy' if calculate_average(zero_crossing_rate_list) > 0.1 else 'smooth',
    'loudness': 'loud' if calculate_average(rms_list) > 0.05 else 'soft'
}

# Save the preset to a JSON file
with open('audio_featured.json', 'w') as file:
    json.dump(preset, file, indent=4)

print("Preset generated and saved to 'audio_preset.json'")

# Generate TTS audio
text = "This is a sample audio based on the preset configuration."
tts = gTTS(text, lang='en')
tts.save('tts_output.mp3')

# Load the TTS output as an AudioSegment
audio_segment = AudioSegment.from_mp3('tts_output.mp3')

# Adjustments based on the JSON preset
# 1. Adjust loudness based on RMS or loudness value
if preset.get('loudness') == 'loud':
    audio_segment += 10  # Increase volume by 10 dB
else:
    audio_segment -= 5   # Decrease volume by 5 dB

# 2. Apply a high-pass filter to enhance brightness
if preset.get('brightness') == 'bright':
    audio_segment = audio_segment.high_pass_filter(1500)

# 3. Optionally apply noise reduction or other effects based on noisiness
if preset.get('noisiness') == 'noisy':
    # Simple reduction in high frequencies to reduce perceived "noisiness"
    audio_segment = audio_segment.low_pass_filter(5000)

# Play the resulting audio
print("Playing generated TTS audio with preset adjustments...")
play(audio_segment)

# Save the modified audio as a new file
audio_segment.export('modified_tts_output.mp3', format='mp3')
print("Modified audio saved as 'modified_tts_output.mp3'")
