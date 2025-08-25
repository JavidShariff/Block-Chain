import hashlib
import json
import time


# ------------------ Block Class ------------------
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        # Proof-of-Work: hash must start with "difficulty" zeros
        while not self.hash.startswith("0" * difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()


# ------------------ Blockchain Class ------------------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3  # Increase for slower mining, decrease for faster

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(len(self.chain), time.time(), data, self.get_latest_block().hash)
        print(f"Mining block {new_block.index}...")
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        print(f"Block {new_block.index} mined with hash: {new_block.hash}\n")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True


# ------------------ Main Program ------------------
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Add some blocks
    my_blockchain.add_block({"amount": 10, "sender": "Alice", "receiver": "Bob"})
    my_blockchain.add_block({"amount": 50, "sender": "Bob", "receiver": "Charlie"})
    my_blockchain.add_block({"amount": 200, "sender": "Charlie", "receiver": "Dave"})

    # Print the blockchain
    print("\n--- Blockchain ---")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("-" * 40)

    # Validate blockchain
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())
