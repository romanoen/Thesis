from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-v0.1")#Mistral-7B-Instruct-v0.2
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-v0.1")

print("1234")

messages = [
    {"role": "user", "content": "Generate one tweet similar to the following one. It should be between 30 and 150 tokens in length and as diverse as possible using different wordings. Don't use words like 'Hey' or 'let's’. Mimic the usage of hashtags (#), user mentions (@), emojis and urls from the originals exactly as possible: No one wants to face disaster and destruction. Everyone wants to live. Unification is a real opportunity to avoid tragedy and live happily in #CreativeSociety #GlobalCrisis #Time4Truth #ClimateCrisis #ClimateChange #ClimateAction #Climate #environment #ecology #ClimateEmergency"}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
response = decoded[0]


#start_index = response.find('[/INST]') + len('[/INST]')
#end_index = response.rfind('</s>')

#cleaned_string = response[start_index:end_index]
#print(cleaned_string)
print(response)
