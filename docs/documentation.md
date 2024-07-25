# Blockchain-Based Asset Tracking (BBAT) Documentation

## Overview
Blockchain-Based Asset Tracking (BBAT) is a blockchain algorithm for secure and transparent tracking of physical and digital assets.

## Algorithms and Methods
### Block Hashing
SHA-256 Hash function:
```
H(B) = SHA-256(B)
```

### Proof of Work
Hash operation to meet difficulty:
```
H(P^2 - P_prev^2) = 0000...
```

## Usage Examples
### Example Data
```python
bbat = BlockchainAssetTracking()
previous_block = bbat.get_previous_block()
proof = bbat.proof_of_work(previous_block['proof'])
block = bbat.create_block(proof, bbat.hash(previous_block))
print(f"New Block: {block}")
print(f"Is blockchain valid? {bbat.is_chain_valid()}")
```
