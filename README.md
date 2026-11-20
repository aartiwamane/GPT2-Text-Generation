# GPT-2 Text Generation

## Overview

This repository demonstrates text generation using **GPT-2 (Generative Pre-trained Transformer 2)** with PyTorch and the Hugging Face Transformers library.

The implementation uses a pretrained GPT-2 language model to generate text based on a user-defined input prompt. It demonstrates the fundamental workflow of loading a pretrained language model, tokenizing input text, generating new tokens, and decoding the generated output.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- GPT-2
- Pretrained Language Models (LLMs)

## Model Information

| Parameter | Details |
|---|---|
| Model | GPT-2 |
| Model ID | `openai-community/gpt2` |
| Architecture | Transformer Decoder |
| Framework | PyTorch |
| Library | Hugging Face Transformers |
| Task | Causal Language Modeling |

## Implementation Workflow

The implementation follows these steps:

1. **Load Pretrained Model:** Load the GPT-2 tokenizer and causal language model using Hugging Face Transformers.
2. **Model Initialization:** Set the model to evaluation mode using `model.eval()`.
3. **Input Prompt:** Define an input text prompt for the model.
4. **Tokenization:** Convert the input prompt into PyTorch tensors using the tokenizer.
5. **Text Generation:** Generate additional tokens using the model's `generate()` method.
6. **Decoding:** Convert the generated token IDs back into readable text.
7. **Output:** Display the original input prompt and generated text.

## Key Concepts Demonstrated

- Pretrained Transformer Language Models
- Tokenization and Token IDs
- Causal Language Modeling
- Autoregressive Text Generation
- Greedy Decoding
- Inference using PyTorch
- Hugging Face Model Integration

## Installation

Clone the repository:

```bash
git clone https://github.com/aartiwamane/GPT2-Text-Generation.git
```

Navigate to the project directory:

```bash
cd GPT2-Text-Generation
```

Install the required dependencies:

```bash
pip install torch transformers
```

## Execution

Run the Python implementation:

```bash
python GPT2_Text_Generation.py
```

The pretrained GPT-2 model and tokenizer are downloaded automatically from Hugging Face during the first execution.

## Configuration

The current implementation uses the following generation parameters:

| Parameter | Value | Purpose |
|---|---|---|
| `max_new_tokens` | 40 | Limits the number of newly generated tokens |
| `do_sample` | False | Uses greedy decoding |
| `pad_token_id` | EOS Token ID | Handles padding during generation |
| `model.eval()` | Enabled | Sets the model to evaluation mode |

## Future Enhancements

- Implement prompt-based text generation using Ollama.
- Support user-defined input prompts.
- Experiment with different text generation parameters.
- Compare Hugging Face and Ollama-based inference approaches.

## Learning Objectives

This project provides practical exposure to Transformer-based language models and the fundamental process of generating text using pretrained GPT architectures.

It serves as an introductory implementation for understanding LLM inference and exploring different approaches to local language model execution.

## Author

**Aarti Wamane**

- GitHub: [aartiwamane](https://github.com/aartiwamane)
- LinkedIn: [Aarti Wamane](https://linkedin.com/in/aarti-wamane-5276562a6)
