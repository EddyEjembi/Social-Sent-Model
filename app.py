import os
import openai

from flask import Flask, request, jsonify
from werkzeug.exceptions import InternalServerError


app = Flask(__name__)


openai.api_type = "azure"
openai.api_base = "https://socialsent.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.errorhandler(InternalServerError)
def handle_internal_server_error(error):
  
    error_message = "The prompt was filtered due to triggering Azure OpenAI’s content filtering system. Reason: This prompt contains flagged contents"
    response = jsonify({"error": error_message})
    response.status_code = error.code
    return response

@app.route('/', methods=["POST", "GET"])
def index():
  #enter = str(input("The Tweet:"))
  tweets = request.get_json()
  input = (tweets['tweet'])

  message_text = [{"role":"system","content":"You are acting as an emotion classifier for some social media post. Take other emotions like fear, scared, happy, etc. into consideration, and only return back the emotion you detect."},
                  {"role":"user","content":input},                  
  ]

  completion = openai.ChatCompletion.create(
    engine="SocialMediaSent",
    messages = message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )
  output = completion.choices[0].message.content
  return {"response": output}
  print(output)


if __name__ == '__main__':
    app.run(debug=True)