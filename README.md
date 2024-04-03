# Smart AI Based Food RAG

Smart AI Based Food RAG is an intelligent food search system that utilizes cutting-edge technologies to provide users with efficient and intuitive text and image search capabilities. The system combines the power of Retrieval Augmented Generation (RAG) techniques, computer vision, and natural language processing to enable users to discover and explore food items seamlessly.

## Overview

This project aims to develop an intelligent food search system with the following key features:

- Text-based search: Users can input text queries to search for restaurants, dishes, and menu items based on various criteria such as cuisine, location, and price range.
- Image-based search: Users can upload images of food items, and the system uses computer vision techniques to identify the dish and retrieve relevant information from the database.
- Cloud-native architecture: The backend API is designed as a cloud-native application, allowing for easy integration into cloud-based ecosystems such as Microsoft Azure.
- Cost-effective solution: The system utilizes open-source technologies, including pre-trained language models from the Hugging Face library, to optimize cost and achieve high performance and accuracy without relying on commercial APIs.

## Features

- **Text-based search**: Analyzes user input, extracts relevant entities and keywords, and retrieves the most relevant information from the database using advanced retrieval algorithms.
- **Image-based search**: Employs computer vision techniques to identify food items in uploaded images and retrieve corresponding information from the database.
- **Data sources**: Utilizes custom-made text datasets providing comprehensive information about restaurants across different cities in India and the Food-101 dataset for image-based search.
- **Vectorization**: Uses MongoDB for data storage and vectorization, enabling the application of Ranked Answer Grouping (RAG) for search functionality.
- **Custom API**: Implements a custom API using Flask, enabling users to interact with the RAG search system through a user-friendly interface.
- **Cloud deployment**: Deployed on Microsoft Azure, ensuring smooth operation, efficient inference processing, and proactive system management.
- **Open-source models**: Integrates pre-trained language models from the Hugging Face library for text and image embeddings, ensuring cost-effectiveness and customization.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/Smart-AI-Based-Food-RAG.git

   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

3. Set up MongoDB Atlas for data storage and retrieval.

4. Deploy the Flask API on Microsoft Azure or any preferred cloud platform.

## Usage

1. Access the API endpoint through the provided URL.

2. Use text queries or upload images to search for restaurants, dishes, and menu items.

3. Explore search results and discover a wide range of food options available.

## Contributors

- Neel Shah - neeldevenshah.ai@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
