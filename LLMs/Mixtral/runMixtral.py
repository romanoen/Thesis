import os
import json
from generate import ResponseGenerator

def main():
    
    #delete existing file to avoid overwriting
    if os.path.exists('responsesMixtral.csv'):
        os.remove('responsesMixtral.csv')
    
    
    model_id = "mistralai/Mistral-7B-Instruct-v0.2"
    output_file = 'responsesMixtral.csv'

    #create an array that contains the original tweets as jsons
    original_data = []
    with open('../../datasets/original.json', 'r', encoding='utf-8') as file:
        for line in file:
            original_data.append(json.loads(line.strip()))

    #create an array of prompts from all orginal tweets
    prompts = [f"Generate one tweet similar to the following one: {entry['tweets']}" for entry in original_data]

    #create 10000 artificial tweets to balance it
    num_lines = len(prompts)

    generator = ResponseGenerator(model_id)
    generator.generate_responses_to_csv(prompts, num_lines, output_file)

if __name__ == "__main__":
    main()

