#This Script creates the most detailed preset

import librosa
import numpy as np
import json

# Load the audio file
audio_path = '1.wav'
y, sr = librosa.load(audio_path, sr=None)

# Feature Extraction
features = {
    "mfccs": librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).tolist(),             # MFCCs
    "spectral_centroid": librosa.feature.spectral_centroid(y=y, sr=sr).tolist(), # Spectral centroid
    "chroma_stft": librosa.feature.chroma_stft(y=y, sr=sr).tolist(),             # Chroma
    "spectral_bandwidth": librosa.feature.spectral_bandwidth(y=y, sr=sr).tolist(), # Spectral bandwidth
    "rms": librosa.feature.rms(y=y).tolist(),                                    # Root mean square energy
    "zero_crossing_rate": librosa.feature.zero_crossing_rate(y).tolist()         # Zero-crossing rate
}

# Save features as JSON
with open("audio_features.json", "w") as json_file:
    json.dump(features, json_file, indent=4)

print("Audio features saved to audio_features.json")
