# Nebula MedAI: FastAPI Backend Server for Treatment Proposals

Welcome to the Nebula MedAI Hackathon! This starter code provides a pre-made FastAPI backend server integrated with Pydantic and OpenAI. It's designed to handle incoming medical treatment requests, generate treatment proposals using OpenAI's GPT-3, and return them in a PDF format.

## Getting Started

### Prerequisites
- Python 3.6+
- Git

### Setup Instructions

1. **Clone the Repository**:
   - Open your terminal.
   - Clone the repository using:
     ```
     git clone https://github.com/Vy-X-S/nebula_medai.git
     ```
   - Navigate into the cloned repository:
     ```
     cd nebula_medai
     ```

2. **Install Requirements**:
   - Ensure you have Python installed.
   - Create a virtual environment
     ```
     python -m venv env
     ```
   - Activate virtual environment (Use appropriate activation script, provided is WSL/Linux):
     ```
     source env/bin/activate
     ```
     A (env) prefix should appear to indicate an activated virtual environment
   - Install the required packages using:
     ```
     pip install -r requirements.txt
     ```
   - The `requirements.txt` file includes FastAPI, Uvicorn, Pydantic, and OpenAI.

3. **Supply Your OpenAI Key**:
   - You must provide your own OpenAI API key.
   - Set your OpenAI key as an environment variable or modify the code to include your key securely.

### Running the Server

- Run the FastAPI server using Uvicorn:
  ```
  uvicorn main:app --reload
  ```
- The server will start running on `http://127.0.0.1:8000`.

## Your Task

### Modify the Code

Your task is to enhance the functionality of this starter code. You need to:

1. **Handle the Incoming Request**:
   - Verify and process the incoming data using the Pydantic model.

2. **Create an OpenAI Prompt**:
   - Formulate a prompt from the processed data to send to the OpenAI API.

3. **Call the OpenAI API**:
   - Use the prompt to generate a treatment proposal from OpenAI.

4. **Generate a PDF**:
   - Convert the OpenAI response into a well-formatted PDF document.

5. **Return the PDF as a Response**:
   - Modify the endpoint to send back the generated PDF as the response to the client.

### Guidelines

- Ensure your code is clean, well-documented, and follows best practices.
- Consider the scalability and efficiency of your solution.
- Pay attention to error handling and edge cases.

### Testing

- Test your modifications thoroughly.
- You can use tools like Postman or the built-in FastAPI documentation at `http://127.0.0.1:8000/docs` for testing endpoints.

Good luck, and we're excited to see your innovative solutions in improving healthcare through technology!
