# Image Analytics - Medical Image Analysis Using Google AI

## Overview
This project provides an interactive web application for analyzing medical images using Google AI's Generative Model. Built with Streamlit, the application allows users to upload medical images and receive detailed analysis.

**Live Deployment**: [Medical Image Analysis App](https://medical-image-analysis-a.streamlit.app/)

## Features
- Upload and analyze medical images (JPEG, PNG, JPG formats)
- Uses Google AI's **Gemini** model for analysis
- Provides detailed feedback on findings, including diagnosis, medications, symptoms, and preventive measures
- Simple and user-friendly web interface using Streamlit

## Tech Stack
- **Python** (Backend processing)
- **Streamlit** (Web UI framework)
- **Google Generative AI (Gemini 1.5 Flash)** (AI-powered analysis) -change it according to the updated gemini model
- **OpenCV & PIL** (Image handling)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

### Steps
1. **Clone the repository**
   ```bash
   https://github.com/Srija-Lattala/medical-image-analysis.git
   cd image-analytics
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google API key**
   - Obtain an API key from Google AI.
   - Store it securely in `.streamlit/secrets.toml`:
     ```toml
     [google]
     api_key = "your_api_key_here"
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage
- Upload a medical image
- Click **"Generate the analysis"**
- AI processes the image and returns an analysis
- View recommendations, symptoms, and preventive measures

## Troubleshooting
- **API Key Issues**: Ensure your Google API key is correct and has access to Generative AI models.
- **Model Deprecation**: The previous `gemini-1.0-pro-vision-latest` model has been deprecated. Ensure you're using `gemini-1.5-flash`.
- **Streamlit Not Found**: Install dependencies using `pip install -r requirements.txt`.

## Contribution
Feel free to open issues and submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License.

---
### Made with ❤️ by Srija

