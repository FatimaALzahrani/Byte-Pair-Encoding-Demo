![header](<https://capsule-render.vercel.app/api?type=cylinder&height=150&color=gradient&customColorList=22&text=Simple%20Byte%20Pair%20Encoding%20(BPE)%20Tokenizer&fontSize=40&animation=fadeIn>)

# Simple Byte Pair Encoding (BPE) Tokenizer

This repository provides a **clean**, **educational**, and **visual** implementation of the Byte Pair Encoding (BPE) algorithm, commonly used in NLP models like GPT and BERT.

> It merges frequent character pairs step-by-step to create an efficient subword vocabulary.

---

## What is BPE?

**Byte Pair Encoding (BPE)** is a tokenization technique that:

- Helps handle unknown words in NLP.
- Splits rare words into frequent subword units.
- Builds a vocabulary of commonly seen character combinations.

BPE is widely used in transformer-based models such as:

- GPT (OpenAI)
- BERT (Google)
- RoBERTa, T5, etc.

---

## Features

- Simple character-level BPE logic
- Step-by-step merging visualization
- Dynamic vocabulary growth tracking
- Auto-stops when no more frequent pairs exist
- Pure Python (no external libraries)

---

## File Overview

| File                 | Description                                      |
| -------------------- | ------------------------------------------------ |
| `bpe_tokenizer.py`   | Detailed BPE implementation with verbose logging |
| `bpe_tokenizer_2.py` | Concise, functional BPE version                  |
| `image.png`          | Visual explanation of BPE process                |

---

## Algorithm Summary

1. Split each word into characters.
2. Count all adjacent character pairs.
3. Merge the most frequent pair into a new token.
4. Repeat until no frequent pairs remain or a stop condition is reached.
5. Return final vocabulary and encoded corpus.

---

## BPE in Action

### Input:

```python
"set new new renew reset renew"
```

### Example Output:

```python
Merging: n e → ne (count 3)
Updated Corpus:
_ s e t
_ ne w
_ re ne w
...
Updated Vocabulary: ['_', 'e', 'n', 'ne', 'r', 's', 't', 'w']
...
Final Tokenized Corpus:
_ s e t
_ ne w
_ re ne w
...
Learned Merge Operations:
n e → ne (count 3)
...
```

![BPE Process Diagram](./image.png)

---

## Example Usage

```python
from bpe_tokenizer import byte_pair_encoding

byte_pair_encoding("set new new renew reset renew")
```

Or using the compact version:

```python
from bpe_tokenizer_2 import byte_pair_encoding

vocab, encoded = byte_pair_encoding("set new new renew reset renew", num_merges=5)
print(vocab)
print(encoded)
```

## Output Explanation

The algorithm shows how subwords like:

- `ne`
- `re`
- `set`
- `new`

...are learned and combined through frequency-based merging.

This makes the BPE tokenizer ideal for:

- Compressing large vocabularies
- Handling rare or unseen tokens
- Improving model generalization in NLP tasks
- Reducing out-of-vocabulary (OOV) issues
