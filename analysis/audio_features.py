from pyAudioAnalysis import audioBasicIO, ShortTermFeatures
import numpy as np

def get_pacing(file_path):
    [Fs, x] = audioBasicIO.read_audio_file(file_path)
    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.025*Fs)
    energy = F[1]
    avg_energy = np.mean(energy)
    return avg_energy
