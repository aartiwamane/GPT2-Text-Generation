import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "openai-community/gpt2"

# Load pretrained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

# Input prompt
prompt = "Artificial Intelligence is"

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
with torch.no_grad():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=40,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

# Decode generated tokens
generated_text = tokenizer.decode(
    output_ids[0],
    skip_special_tokens=True
)

print("Input Prompt:", prompt)
print("Generated Text:", generated_text)