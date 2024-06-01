import csv
import json
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ResponseGenerator:
    
    #initiate Mixtral model in constructor and load it once 
    def __init__(self, model_id):
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id)
    
    #generate a response on certain prompt
    def generate_response(self, prompt, max_new_tokens=256, temperature=1.0, top_p=1.0):
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        messages = [
            {"role": "user", "content": prompt}
        ]

        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        
        model_inputs = encodeds.to(device)
        self.model.to(device)
        
        generated_ids = self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)
        
        response = decoded[0]
        
        start_index = response.find('[/INST]') + len('[/INST]')
        end_index = response.rfind('</s>')
        cleaned_string = response[start_index:end_index]

        return cleaned_string

    #write into the csv file
    def generate_responses_to_csv(self, prompts, num_lines, output_file):
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Prompt', 'Response'])
            
            for i in range(num_lines):
                print(i, " from ", num_lines)
                prompt = prompts[i % len(prompts)]
                response = self.generate_response(prompt)
                writer.writerow([prompt, response])
