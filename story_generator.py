import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_story(prompt="Once upon a time", max_length=1000):
    # Load GPT-2 model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Tokenize input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate story output
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7, do_sample=True)
    
    # Decode and return
    story = tokenizer.decode(output[0], skip_special_tokens=True)
    return story

if __name__ == "__main__":
    prompt = input("Enter a story prompt: ")
    print("\nGenerated Story:\n")
    print(generate_story(prompt))
