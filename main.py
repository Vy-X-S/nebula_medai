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
    #####
    # Your code for error handling here
    ####
  
    # Establish API Key
    api_key = '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'
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
  
@app.post("/treatment_proposal/")
async def create_treatment_proposal(request: TreatmentRequest):
    """
    Processes a medical treatment request, generates a treatment proposal using OpenAI,
    converts the proposal to a PDF, and returns the PDF file as a response.

    Parameters:
    request (TreatmentRequest): An object containing necessary data for the treatment proposal,
                                structured according to the TreatmentRequest Pydantic model.

    Returns:
    FileResponse: A FastAPI FileResponse object that serves the generated PDF file.

    Notes:
    - The function converts the OpenAI response into HTML format before transforming it into a PDF.
    - The PDF is temporarily stored on the server and should be deleted after serving to save space and ensure data privacy.
    - The function is set up to handle exceptions and errors, particularly for scenarios where the PDF generation might fail.
    - Make sure the path for temporarily storing the PDF (`pdf_path`) is correctly set and accessible.
    - Ensure compliance with data privacy regulations, as the process involves handling sensitive medical data.
    - The response is of type 'application/pdf', suitable for PDF file responses.
    - It's essential to test the end-to-end functionality thoroughly, from receiving data to returning the PDF.
    """
    
    # Convert the request to a dictionary and call OpenAI API
    request_data = request.dict()
    openai_response = await call_openai_api(request_data)

    # Check if OpenAI response is valid
    if not openai_response:
        raise HTTPException(status_code=500, detail="Failed to generate response from OpenAI")
    else:
        return openai_response # Remove this for your solution

    ###### Convert the response to HTML and then to a PDF
    ###### (Add your logic here for HTML conversion and PDF generation)
    # html_content = f"<html><body><p>{openai_response}</p></body></html>"
    # pdf_path = "path_to_your_pdf.pdf"
    ###### (Use a library like PDFKit to convert html_content to a PDF stored at pdf_path)

    ###### Return the PDF file as a response
    # return FileResponse(pdf_path, media_type='application/pdf', filename="treatment_proposal.pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
