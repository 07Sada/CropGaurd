---
title: CropGaurd
emoji: 🏢
colorFrom: indigo
colorTo: red
sdk: gradio
sdk_version: 3.39.0
app_file: app.py
pinned: false
---

# CropGaurd
## Agriculture and Farming Machine Learning Project

Developed a comprehensive web application that harnesses the power of machine learning to provide valuable insights and recommendations to farmers, agriculture enthusiasts, and stakeholders.

![CropGaurd-thumbnail](https://github.com/07Sada/CropGaurd/assets/112761379/fd5f1726-7450-4758-952e-23e7f7b9da06)

# Disclaimer
This project serves as a Proof of Concept (PoC) and is not intended for making actual farming decisions. The data utilized within this project is provided without any guarantee from the creator. Therefore, it is strongly advised not to utilize the information for real-world agricultural choices. Should you choose to do so, please be aware that the creator bears no responsibility for the outcomes.

It's important to note that this project primarily demonstrates the application of Machine Learning (ML) and Deep Learning (DL) concepts within precision farming. The hypothetical scenario presented here underscores the potential benefits of deploying ML/DL techniques on a larger scale, provided that authentic and verified data sources are used.

For reliable and accurate farming decisions, always rely on verified agricultural data sources, expert advice, and industry standards.

## Project Links

- **Application Link:** Check out the live application on Hugging Face Spaces: [Application Link](https://huggingface.co/spaces/Sadashiv/CropGaurd)

- **Demo Video:** For a visual walkthrough of the application's features, watch demo video: [Demo Video Link](<insert_demo_video_link_here>)

## Project Overview
The application integrates several key features to assist users in making informed decisions for their agricultural activities. These features include:

- ***Crop Recommendation System:*** Leveraging advanced machine learning techniques, the system recommends suitable crops based on various factors such as soil chemical contents, and climate conditions.

- ***Fertilizer Recommendation System:*** The application also offers personalized fertilizer recommendations, ensuring that crops receive the optimal nutrients for healthy growth and abundant yields.

- ***Plant Disease Classification:*** By employing cutting-edge image classification models, incorporated a feature that enables users to detect and diagnose diseases in plants. Users can simply upload images of their plants, and our system will accurately identify any diseases present and provide relevant information about them.

- ***Real-time Commodity Price Updates:*** To empower users with current market insights, we have integrated a government API that provides daily commodity prices across different Indian states. This information assists farmers and traders in making pricing and distribution decisions.

## Purpose
The aim of project to revolutionize the agricultural sector by offering data-driven solutions that enhance productivity, reduce risks, and promote sustainable practices. By amalgamating technology and agriculture, we strive to address critical challenges faced by farmers and contribute to the growth of the farming community.

Whether you're a seasoned farmer seeking optimized strategies or an individual interested in sustainable agriculture, our application provides the tools you need to make well-informed decisions.

## Additional Details
Here are some additional aspects of the project that contribute to its effectiveness and uniqueness:

- ***Machine Learning Models:*** We have trained our recommendation and classification models on extensive datasets specific to Indian agriculture. This ensures that the recommendations and classifications are accurate and relevant to the local context.

- ***User-Friendly Interface:*** Our web application boasts an intuitive and user-friendly interface designed to make navigation and interaction seamless, even for users with limited technological experience.

- ***Informational Insights:*** Apart from recommendations, our application provides detailed information about recommended crops, fertilizers, and identified plant diseases. This information helps users understand the rationale behind the suggestions and take well-informed actions.

- ***Scalability:*** Our project's architecture is designed to accommodate future expansions and enhancements. We are committed to continuously improving the application by incorporating user feedback and integrating emerging technologies.

## Getting Started
- Clone or download the parent repository from [GitHub Repository Link](https://github.com/07Sada/CropGaurd)

    ```
    git clone --recurse-submodules https://github.com/07Sada/CropGaurd
    ```
- The total project is divided into 4 repositories: one parent repository and 3 child repositories. The child repositories are dedicated to specific functionalities, namely [[crop recommendations](https://github.com/07Sada/crop-recommendation)], [[fertilizer recommendations](https://github.com/07Sada/Fertilizer-Recommendation)], and [[image classification](https://github.com/07Sada/plant-diseases-classifier)].
- The parent and child repositories are connected using Git submodules. This approach is taken to keep each recommendation system separate, as they contain their end-to-end pipelines – from data ingestion to model training and deploying the best models for inference.
- This modular structure allows us to maintain clean and organized code while efficiently managing updates and changes to each submodule.
- The data ingestion pipeline is flexible, as it is integrated with a MongoDB database. You can set up a scheduler to periodically update the training data. After new data is ingested, the models are trained and evaluated against the existing models. The best model is then pushed for inference, all of which is seamlessly automated through the pipeline, reducing the potential for errors.
- To get started, navigate to the parent repository and install the required dependencies.
- Explore each child repository for more specific details on their functionalities and pipelines.
- Launch the web application by running command in terminal.

  ```
  python app.py
  ```
- Start exploring the features and making use of the insightful recommendations provided.


