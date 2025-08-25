from django.shortcuts import render
from django.conf import settings
import openai
import html

# Initialize the OpenAI client
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(prompt):
    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        
        # Extract the response content
        if response and response.choices and len(response.choices) > 0:
            response_text = response.choices[0].message.content
            
            # Format the response with HTML preserved
            if response_text:
                formatted_response = response_text.replace('\n', '<br>')
                return formatted_response
            
        return "<p>No response received from OpenAI.</p>"
    except Exception as e:
        return f"<p>Error: {str(e)}</p>"

def index(request):
    context = {}
    
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        if prompt:
            context['prompt'] = prompt
            context['response'] = generate_response(prompt)
    
    return render(request, 'chatbot/index.html', context)
