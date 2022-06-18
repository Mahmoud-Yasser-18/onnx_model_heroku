import librosa
from transformers import AutoFeatureExtractor,Wav2Vec2ForSequenceClassification,AudioClassificationPipeline
feature_extractor = AutoFeatureExtractor.from_pretrained( "facebook/wav2vec2-base")
model = Wav2Vec2ForSequenceClassification.from_pretrained("Mahmoud1816Yasser/tmp_trainer",num_labels=84)
pipeline_audio= AudioClassificationPipeline(model)
pipeline_audio.feature_extractor= feature_extractor
if __name__=="__main__":
  file_name="a.wav"
  print(pipeline_audio(librosa.load(file_name,sr=None)[0]))