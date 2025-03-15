

import google.generativeai as genai

# Replace 'YOUR_API_KEY_HERE' with your actual Gemini API key
# API_KEY = 'AIzaSyAdQHUUE2kFPAKTusUmobfp7vFvXwXxRyw'
API_KEY = 'AIzaSyAdQHUUE2kFPAKTusUmobfp7vFvXwXxRyw'

# Configure the Gemini API with the key
genai.configure(api_key=API_KEY)

# Initialize the model (using gemini-1.5-flash as an example)
model = genai.GenerativeModel('gemini-1.5-flash')

# System prompt to define the AI's behavior
SYSTEM_PROMPT = """
You are Kanak , an student at UAI Karjat. 
You are in the library, studying for your exams.
You are approached by a fellow student who asks you for help with a difficult question.
- Your DOB in Augst 2005
- You are a student at UAI Karjat






.
"""

# Function to get a response from the model with system prompt
def get_gemini_response(prompt):
    try:
        # Combine system prompt with user prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Main CLI loop
def chatbot():
    print("Welcome to the Grok 3 CLI Chatbot!")
    print("Type 'exit' to quit.\n")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get and display the response from Gemini
        response = get_gemini_response(user_input)
        print(f"Bot: {response}\n")

# Run the chatbot
if __name__ == "__main__":
    chatbot()