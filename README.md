# 🧱 Simple Blockchain in Python

This project is a **basic implementation of a Blockchain** using pure Python.  
It demonstrates the core concepts of blockchain technology such as **blocks, hashing, and chain linking** — without relying on any external frameworks.

---

## 🚀 Features
- Creates a **Genesis Block** (first block in the chain).
- Adds new blocks automatically to the chain.
- Each block contains:
  - Index (block number)
  - Previous block hash
  - Timestamp
  - Data (custom message)
  - Current block hash
- Uses **SHA-256 hashing** for security.
- Shows how blocks are **linked together**, making tampering evident.

---

## 📂 Project Structure

---

## ⚡ How It Works
1. The blockchain starts with a **Genesis Block**.
2. Each new block stores:
   - Its own hash
   - The hash of the previous block
3. This creates a secure **chain of blocks**.
4. If someone tries to modify data in any block, the hash will change and break the chain integrity.

---

## 🛠️ Installation & Running
### Requirements
- Python 3.x

### Steps
```bash
# Clone or download the repository
git clone https://github.com/yourusername/simple-blockchain.git

# Move into project folder
cd simple-blockchain

# Run the blockchain
python blockchain.py
Genesis Block created!
Block #1 has been added to the blockchain
Hash: 000a1cfe3...

Block #2 has been added to the blockchain
Hash: 0fbd49cc5...

Block #3 has been added to the blockchain
Hash: 2b1f91ad3...
