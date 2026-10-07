# mac_in_orbit

![](./assets/cover.png)

> MAC **Secret Key**, recovery

A Python cryptography challenge focused on recovering a secret key from a known message and its corresponding Message Authentication Code (MAC).


## Table of Contents

- [Overview](#overview)
- [Test The Project](#test-the-project)
- [Included Files](#included-files)
- [Project Structure](#project-structure)
- [Conventions](#conventions)
- [Roadmap Seed](#roadmap-seed)
- [License](#license)

## Overview

This challenge implements a custom MAC algorithm that combines:

- Character-to-number conversion;  
- Key repetition to match the message length;  
- XOR operations between the message and key;  
- Mathematical operations between consecutive elements;  
- Analysis of a known plaintext and known tag to recover the secret key 

This repository is intentionally generic. Replace placeholders and keep only the sections/files that match your generated project.

### Goals

The goal is to understand how the custom MAC works, identify the mathematical relationships within it, and use the intercepted data to reconstruct the original key.

## Test The Project

1. Python`3` required.
3. Clone repository:

```bash
git clone https://github.com/fevunge/mac_in_orbit.git
cd mac_in_orbit

python mac.py
```

## Included Files

| File | Purpose |
|---|---|
| `mac.py` |  the reference implementation of the MAC. Put your candidate into KEY_CANDIDATE and run the file. |
| `intercepted-pair.txt` | command and tag, ready to copy. |


## Project Structure

```text
 .
├──  __pycache__
│   └──  mac.cpython-314.pyc
├──  assets
│   └── 󰕙 MAC.svg
├──  intercepted-pair.txt
├──  mac.py
└── 󰂺 README.md
```

## Roadmap Seed

- [x] Python 3
- [ ] Bitwise Operations
- [ ] Cryptography & Cryptanalysis

## License

Copyright 2026 fevunge

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

