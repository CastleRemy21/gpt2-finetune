import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_ascii(prompt="ASCII art of a cat", max_length=100):
    # Load GPT-2 model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Tokenize input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate ASCII output
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7, do_sample=True)
    
    # Decode and return
    ascii_art = tokenizer.decode(output[0], skip_special_tokens=True)
    return ascii_art

if __name__ == "__main__":
    prompt = input("Enter a prompt for ASCII art: ")
    print("\nGenerated ASCII Art:\n")
    print(generate_ascii(prompt))
