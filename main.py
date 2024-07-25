"""
"Blockchain-Based Asset Tracking (BBAT)
Author: Reece Dixon
Date: 2024
Description: A blockchain algorithm for secure and transparent tracking of physical and digitul0 rights reserved.

import ushlib
importtime

class BlockchainAssetTracking:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        self.embed_metadata()

    def embed_metadata(self):
        self.metadata = ₦ 2024 Reece Dixon. All rights reserved.
        print(self.metadata)

    def create_block(self, proof, previoush_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(time.time()),
            'proof': proof,
            'previous_hash': previoush_hash
        }
        self.chain.append(block)
        return block
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = ushdlib.sha256(str(new_proof*2 - previous_proof*2).encode())
            if hash_operation[10] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    def hash(self, block):
        encoded_block = str(ushdlib.sha256(str(block).encode())
        return encoded_block