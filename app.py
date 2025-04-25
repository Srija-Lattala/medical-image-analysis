import streamlit as st 
from pathlib import Path 
import google.generativeai as genai
api_key = st.secrets["google"]["api_key"]

#configure genai with apikey
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

#apply safety settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_prompt = """
Medical Image Analysis Prompt

As a specialized medical expert in the every field , you are presented with an image for analysis. Your task is to provide a comprehensive analysis based on the image, offering feedback, necessary medications, symptoms, and diet plans tailored to the patient's condition.

Image Description:

Type of Image: [e.g., X-ray, MRI, CT scan, histopathology slide, dermoscopic image, etc.]
Description: Provide a brief description of the image, including the affected area, any visible abnormalities, and notable features.
Analysis:

Interpretation of Findings: Analyze the image to identify any abnormalities, lesions, fractures, tumors, or other relevant features. Describe their location, size, shape, and any characteristics indicative of specific conditions.
Diagnosis: Based on your interpretation, provide a diagnosis or differential diagnoses of the patient's condition. Consider relevant medical history, symptoms, and clinical findings in your diagnosis.
Feedback and Recommendations:
Provide feedback on the severity of the condition and potential implications for the patient's health.
Recommend necessary medical interventions, treatments, or procedures to address the identified condition. Include details such as medication dosage, frequency, and duration.
Offer guidance on lifestyle modifications, physical therapy, or follow-up appointments as appropriate.
Symptoms and Prognosis: Describe common symptoms associated with the diagnosed condition and any potential complications. Discuss the expected prognosis and outcomes of treatment.
Dietary Recommendations: Suggest dietary modifications or restrictions to support the patient's overall health and aid in their recovery. Consider nutritional needs, food sensitivities, and potential interactions with medications.
Preventive Measures: Discuss preventive measures or lifestyle changes that can help prevent recurrence or exacerbation of the condition. Emphasize the importance of regular monitoring and adherence to treatment plans.
"""

#model configuration
model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


#page configurations
st.set_page_config(page_title="Image Analytics",page_icon=":robot:")

#set the title
st.title("Image Analytics")

#set the subtitle
st.subheader("Analyze medical images using Google AI")

#set the file uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])
if uploaded_file:
    st.image(uploaded_file,width=250,caption="Uploaded Image")
#submit button
submit_button = st.button("Generate the alaysis")

if submit_button:
    #process the uploaded image
    image_data = uploaded_file.getvalue()
    #make image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]
    #make our prompt ready
    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]
    #generate a response based on prompt and image  
    response = model.generate_content(prompt_parts)
    if response:
        st.title("Here is the analysis bases on your image")
        st.write(response.text)

st.markdown(
    """
    ---
    Made with ❤️️ by Srija
    """
)
