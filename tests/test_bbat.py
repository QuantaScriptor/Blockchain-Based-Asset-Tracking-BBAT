import unittest
import hashlib
from bbat import BlockchainAssetTracking

class TestBBAT(unittest.TestCase):
    def setUp(self):
        self.bbat = BlockchainAssetTracking()

    def test_create_block(self):
        previous_block = self.bbat.get_previous_block()
        proof = self.bbat.proof_of_work(previous_block['proof'])
        block = self.bbat.create_block(proof, self.bbat.hash(previous_block))
        self.assertIsNotNone(block)

    def test_is_chain_valid(self):
        self.assertTrue(self.bbat.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
