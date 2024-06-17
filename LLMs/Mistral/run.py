import json
import os
from generate import ResponseGenerator

def main():
    
    #delete existing file to avoid overwriting
    if os.path.exists('responsesMistral.csv'):
        os.remove('responsesMistral.csv')
    
    model_id = "mistralai/Mistral-7B-Instruct-v0.2"
    output_file = 'responsesMistral.csv'

    #create an array that contains the original tweets as jsons
    original_data = []
    with open('../../datasets/original.json', 'r', encoding='utf-8') as file:
        for line in file:
            original_data.append(json.loads(line.strip()))

    #create an array of prompts from all original tweets
    original_tweets = [entry['tweets'] for entry in original_data]
    prompts = [f"Generate one tweet similar to the following ones,
especially try to recreate the tone and style of the
tweets. It should be between 30 and 150 tokens in
length and reflect the topic of the tweets. Mimic
the usage of hashtags (#), user mentions (@),
emojis and URLs from the originals exactly as
possible: {tweet}" for tweet in original_tweets]

    #create 10000 artificial tweets to balance it
    num_lines = len(prompts)

    generator = ResponseGenerator(model_id)
    generator.generate_responses_to_csv(original_tweets, prompts, num_lines, output_file)

if __name__ == "__main__":
    main()

