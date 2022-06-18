import librosa
from transformers import AutoFeatureExtractor,Wav2Vec2ForSequenceClassification,AudioClassificationPipeline #, AutoModel, AutoTokenizer, 
import torch
from datasets import Dataset,Features,Value,Audio,ClassLabel
feature_extractor = AutoFeatureExtractor.from_pretrained( "facebook/wav2vec2-base")
model = Wav2Vec2ForSequenceClassification.from_pretrained("Mahmoud1816Yasser/tmp_trainer",num_labels=84)
pipeline_audio= AudioClassificationPipeline(model)
pipeline_audio.feature_extractor= feature_extractor
if __name__=="__main__":
  file_name="a.wav"
  y, sr = librosa.load(file_name,sr=None)
  print(pipeline_audio(y))