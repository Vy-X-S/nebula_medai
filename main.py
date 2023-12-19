from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date
from openai import OpenAI

app = FastAPI()

class Symptom(BaseModel):
  symptom_id: str
  symptom_name: str

class TreatmentRequest(BaseModel):
  session_id: str
  clinic_id: str
  user_id: str
  patient_id: str
  patient_symptoms: List[Symptom]
  doctor_id: str
  date: date
  treatment: str
  tx_id: str

#########################################################
# Your function to create a PDF Here #
#########################################################

# Function to call OpenAI API
async def call_openai_api(data: dict):
    """
    Asynchronously calls the OpenAI API to generate a medical treatment proposal.

    This function takes medical data as input, formats it into a prompt, and sends it to the OpenAI API. 
    The API is expected to return a structured response containing a medical document based on the treatment proposal data provided.

    Parameters:
    data (dict): A dictionary containing key medical information required for generating the treatment proposal.
                 The structure of this dictionary should align with the expected format for the prompt.

    Returns:
    dict: A dictionary containing the generated medical treatment proposal as returned by the OpenAI API.
          The response will include structured data, such as the proposal text, which can be further processed or formatted.

    The function establishes a connection with the OpenAI API using the provided API key. 
    It then creates a chat-based prompt using the input data and sends a request to the OpenAI API. 
    The response from the API, structured as a dictionary, is processed and returned, which represents the medical treatment proposal.

    Note: The API key should be securely stored and accessed. 
    The function assumes that 'YOUR OPENAI_KEY' is replaced with the actual API key before deployment.
    """
  
    # Establish API Key
    api_key = 'YOUR OPENAI_KEY'
    client = OpenAI(api_key=api_key)

    # Create a prompt from the request data
    # Customizing the prompt to output your desired result is best
    prompt = f"Generate a medical treatment proposal based on the following data: {data}"

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a medical assistant. You create medical documents based on treatment proposal data."},
        {"role": "user", "content": prompt}
      ]
    )
    return response.choices[0].message.content
  
# Define the endpoint
@app.post("/treatment_proposal/")
async def create_treatment_proposal(request: TreatmentRequest):
    """
    API endpoint to create a medical treatment proposal based on provided patient data.

    This endpoint receives medical data encapsulated within a TreatmentRequest object, 
    processes it, and utilizes the OpenAI API to generate a treatment proposal.

    Parameters:
    request (TreatmentRequest): An object of the TreatmentRequest Pydantic model, 
                                containing all necessary data for treatment proposal generation.
                                This includes patient symptoms, doctor ID, clinic ID, and other relevant information.

    Returns:
    dict: A dictionary containing the treatment proposal generated by the OpenAI API. 
          The response is keyed by 'openai_response'.

    The function converts the incoming Pydantic model object into a dictionary, 
    which is then passed to the 'call_openai_api' function. The response from the OpenAI API, 
    which is an AI-generated medical treatment proposal, is returned as a JSON response.

    This endpoint serves as the primary interface for users to submit treatment proposal requests 
    and receive AI-generated responses.
    """
    request_data = request.dict()
    openai_response = await call_openai_api(request_data)
    return {"openai_response": openai_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)