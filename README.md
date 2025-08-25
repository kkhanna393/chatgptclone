# ChatGPT Clone with Django

This is a simple Django application that connects to OpenAI's API to generate responses based on user prompts, similar to ChatGPT.

## Features

- Simple and clean user interface
- Connects to OpenAI API for generating responses
- Displays responses with proper HTML formatting
- Easy to use and extend

## Setup Instructions

1. Clone the repository
2. Install the required packages:
   ```
   pip install django openai python-dotenv
   ```
3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```
5. Open your browser and navigate to http://127.0.0.1:8000/

## Usage

1. Enter your prompt in the text field
2. Click "Submit" to send your prompt to OpenAI
3. View the generated response displayed below the form

## Project Structure

- `chatbot/` - The main Django app
  - `views.py` - Contains the logic for interacting with OpenAI's API
  - `urls.py` - URL routing for the app
- `templates/chatbot/` - HTML templates
  - `index.html` - The main interface template
- `openai_chat/` - The Django project settings
  - `settings.py` - Project settings including OpenAI configurations
  - `urls.py` - Main URL routing

## Customization

You can customize the following in the settings.py file:
- `OPENAI_MODEL` - Change the OpenAI model used (default is 'gpt-3.5-turbo')

## License

This project is open-source and available under the MIT License.
