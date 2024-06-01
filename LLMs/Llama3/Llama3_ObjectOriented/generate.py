import csv
import json
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ResponseGenerator:
    
    #initiate Llama3 8B model in constructor and load it once 
    def __init__(self, model_id):
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )
    
    #generate a response on certain prompt
    def generate_response(self, prompt, max_new_tokens=256, temperature=1.0, top_p=1.0):
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        messages = [
            {"role": "user", "content": prompt}
        ]

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)

        terminators = [
            self.tokenizer.eos_token_id,
        ]

        outputs = self.model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            eos_token_id=terminators,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
        )

        response = outputs[0][input_ids.shape[-1]:]
        return self.tokenizer.decode(response, skip_special_tokens=True)

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
