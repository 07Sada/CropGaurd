import os

MODEL_NAME = "model.pkl" 
TARGET_ENCODER_OBJECT_NAME = "target_encoder.pkl"
TRANSFORMER_OJBCET_NAME = "transformer.pkl"

crop_recommendation_artifacts_path = "./crop-recommendation/saved_models"
fertilizer_recommendation_artifacts_path = "./Fertilizer-Recommendation/saved_models"

plant_diseases_classifier_model_path = "./plant-diseases-classifier/custom_model_weights/best.pt"


## crop recommendation artifacts
latest_crop_recommendation_artifacts = max(os.listdir(crop_recommendation_artifacts_path)) #0, 1, 2

latest_crop_recommendation_artifacts_path = os.path.join(crop_recommendation_artifacts_path, latest_crop_recommendation_artifacts)

crop_model_path = os.path.join(latest_crop_recommendation_artifacts_path, 'model', MODEL_NAME)
crop_transformer_path = os.path.join(latest_crop_recommendation_artifacts_path,'transformer', TRANSFORMER_OJBCET_NAME)
crop_target_encoder_path = os.path.join(latest_crop_recommendation_artifacts_path, 'target_encoder', TARGET_ENCODER_OBJECT_NAME)


## fertilizer recommendation artifacts
latest_fertilizer_recommendation_artifacts = max(os.listdir(fertilizer_recommendation_artifacts_path)) #0, 1, 2

latest_fertilizer_recommendation_artifacts_path = os.path.join(fertilizer_recommendation_artifacts_path, latest_fertilizer_recommendation_artifacts)

fertilizer_model_path = os.path.join(latest_fertilizer_recommendation_artifacts_path, 'model', MODEL_NAME)
fertilizer_transformer_path = os.path.join(latest_fertilizer_recommendation_artifacts_path,'transformer', TRANSFORMER_OJBCET_NAME)
fertilizer_target_encoder_path = os.path.join(latest_fertilizer_recommendation_artifacts_path, 'target_encoder', TARGET_ENCODER_OBJECT_NAME)

