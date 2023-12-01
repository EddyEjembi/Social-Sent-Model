import json

def convert_dataset(input_file, training_file, validation_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    conversations = []
    count = 0
    i = 0
    for entry in data:
        sentiment = entry["sentiment"]
        content = entry["content"]
        
        system_message = {"role": "system", "content": "You are acting as an emotion classifier for some social media post. Take other emotions like fear, scared, happy, etc. into consideration, and only return back the emotion you detect."}
        user_message = {"role": "user", "content": content}
        assistant_message = {"role": "assistant", "content": sentiment}
        
        conversation = {"messages": [system_message, user_message, assistant_message]}
        conversations.append(conversation)
    
    with open(training_file, 'w') as f:
        for conv in conversations:
            f.write(json.dumps(conv) + '\n')
            count += 1
            if count >= 50:
                break

    with open(validation_file, 'w') as g:
        for conv in conversations[51:]:
            g.write(json.dumps(conv) + '\n')
            i += 1
            if i == 30:
                break

input_file = 'csvjson.json'
training_file = 'training_dataset.jsonl'
validation_file = 'validation_dataset.jsonl'
convert_dataset(input_file, training_file, validation_file)