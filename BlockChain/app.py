from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route("/mine", methods=["POST"])
def mine_block():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "Missing data"}), 400

    block = blockchain.add_block(data)
    return jsonify({
        "message": "Block mined",
        "block": {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        }
    })


@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = [
        {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        }
        for block in blockchain.chain
    ]
    return jsonify({"length": len(chain_data), "chain": chain_data})


@app.route("/validate", methods=["GET"])
def validate_chain():
    valid = blockchain.is_chain_valid()
    return jsonify({"valid": valid})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
