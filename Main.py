import datetime
import hashlib
import json
import binascii
class Blockchain:

    def __init__(self):
        self.chain =[]
        self.mine_block(prev_hash='0',vin_number=0,description="Genesis")



    def mine_block(self,prev_hash,vin_number,description):
        block= { 'height':len(self.chain)+1,
                  'timestamp': str(datetime.datetime.now()),
                  'previous_block_hash': prev_hash,
                  'VIN': vin_number,
                  'Description': description}
        self.chain.append(block)
        return block
    
    def hash(self,block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        first_encode= hashlib.sha256(encoded_block).hexdigest()
        first_encode_binary = binascii.unhexlify(first_encode)
        second_encode = hashlib.sha256(first_encode_binary).hexdigest()
        return second_encode
    
    def prev_block(self):
        return self.chain[-1]

    def verify_chain(self):
        prev_block = self.chain[0]
        index = 1
        results = []

        while index <len(self.chain):

            curr_block = self.chain[index]
            if  curr_block['previous_block_hash'] != self.hash(prev_block):
                results.append( {"block": index, "Valid": "False", 'stored': curr_block['previous_block_hash'], "calculated":self.hash(prev_block) })
                
            else:
                results.append( {"block": index, "Valid": "True", 'stored': curr_block['previous_block_hash'], "calculated":self.hash(prev_block) })
            prev_block = curr_block
            index+=1
        return results
        
