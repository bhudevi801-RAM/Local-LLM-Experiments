# Experiment 04 — LLM vs Python

## Objective

To compare a traditional rule-based Python program with a large language model.

## Traditional Python Program

A traditional program follows rules written explicitly by the programmer.

```python
temperature = float(input("Enter the temperature: "))

if temperature > 35:
    print("Stay indoors and drink water.")
elif temperature >= 25:
    print("Normal outdoor activity is suitable.")
else:
    print("Carry a light jacket.")
```

## Example Output

```text
Enter the temperature: 38
Stay indoors and drink water.
```

## How the Python Program Works

The program follows fixed conditions:

- Above `35°C` → stay indoors
- From `25°C` to `35°C` → normal outdoor activity
- Below `25°C` → carry a light jacket

It cannot provide advice outside the rules written in the program.

## LLM Experiment

The following prompt was given to a local language model:

```text
The temperature today is 38°C. What precautions should I take?
```

### Example LLM Response

```text
Drink plenty of water, avoid direct sunlight during the afternoon,
wear light clothing, and stay indoors when possible.
```

## Comparison

| Feature | Traditional Python | Large Language Model |
|---|---|---|
| Behaviour | Follows fixed rules | Generates a flexible response |
| Input | Usually structured | Can understand natural language |
| Output | Predictable | May vary |
| Training data | Not required | Requires large amounts of data |
| Reasoning | Based on programmed conditions | Based on learned patterns |
| Creativity | Very limited | Can generate new text |

## Observation

The Python program produced a fixed response based on the specified condition. The LLM produced a more detailed natural-language response.

## Result

Traditional Python and LLMs solve problems differently. Python follows manually written instructions, whereas an LLM generates responses from patterns learned during training.

## What I Learned

- Traditional programs use explicit rules
- LLMs learn patterns from large datasets
- Python output is predictable for the same input
- LLM output can be flexible and detailed
- Not every Python program is artificial intelligence
