from artifacts import crop_model_path, crop_transformer_path, crop_target_encoder_path
from artifacts import fertilizer_model_path, fertilizer_transformer_path, fertilizer_target_encoder_path
from artifacts import plant_diseases_classifier_model_path

from utils import load_model_and_encoders
from ultralytics import YOLO

crop_model, crop_pipeline_encoder, crop_label_encoder = load_model_and_encoders(model_path=crop_model_path, 
                                                                                transformer_path=crop_transformer_path,
                                                                                target_encoder_path=crop_target_encoder_path)

fertilizer_model, fertilizer_pipeline_encoder, fertilizer_label_encoder = load_model_and_encoders(model_path=fertilizer_model_path, 
                                                                                transformer_path=fertilizer_transformer_path,
                                                                                target_encoder_path=fertilizer_target_encoder_path)

plant_diseases_classifier_model = YOLO(plant_diseases_classifier_model_path)
