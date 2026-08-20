# Experiment 01 — Ollama Setup

## Objective

To install Ollama and run a large language model locally on my computer.

## What is Ollama?

Ollama is a tool that allows us to download and run large language models locally.

## Steps

1. Downloaded and installed Ollama.
2. Opened Command Prompt.
3. Checked the Ollama installation:

```bash
ollama --version
```

4. Viewed the locally installed models:

```bash
ollama list
```

5. Ran a local language model:

```bash
ollama run llama3.2:1b
```

6. Entered a sample prompt:

```text
Explain artificial intelligence in simple words.
```

## Observation

The model generated a response locally using Ollama.

## Result

Ollama was successfully installed, and a local language model was tested.

## Actual Local Test

### Environment

- Ollama version: `0.12.14`
- Model: `llama3.2:latest`
- Model size: `2.0 GB`

### Prompt

```text
Explain artificial intelligence in simple words.
```

### Response Summary

The model explained that AI processes data, detects patterns, makes predictions or decisions, and is used in virtual assistants, image recognition, and self-driving systems.

### Exit Command

```text
/bye
```

The local model ran successfully through Ollama.

## What I Learned

- What a local LLM is
- How to use Ollama commands
- How to download and run a model
- How local LLMs can respond without using a web-based chatbot
