import datetime
import hashlib

class Blockchain:

    def __init__(self):
        self.chain =[]
        self.mine_block(prev_hash='0',vin_number=0)


    def mine_block(self,prev_hash,vin_number):
        block= { 'height':len(self.chain)+1,
                  'timestamp': str(datetime.datetime.now()),
                  'proof':proof,
                  'previous_block_hash': prev_hash,
                  'VIN': vin_number}

        self.chain.append(block)
        return block
    
    def hash(self,block):
        encoded_block = json.dumps(block).encode()
        first_encode= hashlib.sha256(encoded_block).hexdigest()
        second_encode = hashlib.sha256(first_encode)
        return second_encode
    




