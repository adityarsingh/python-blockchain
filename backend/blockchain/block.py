import time

from backend.util.cryptohash import crypto_hash
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp' : 1,
    'last_hash' : 'genesis_last_hash',
    'hash'      : 'genesis_hash',
    'data'      : [] ,
    'difficulty': 3,
    'nonce'     : 'genesis_nonce'
} #it is a global varibale and global variables are declared all upper case it is also known as scream case syntax

class Block:
    """
    A unit of storage.
    Stores transactioins in blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash,data,difficulty,nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'Data: {self.data}, ' 
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )
    @staticmethod
    def mine_block(last_block,data):
        """
        Mines a block based on the last_blaock and data.It is function that generates a new block that
        then added to the block chain.It mines until a block hash is found that meets the leading 0's
        proof of work requirements.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block,timestamp)
        nonce = 0
        hash = crypto_hash(timestamp,last_hash,data,difficulty,nonce)
        while hash[0:difficulty] != '0'*difficulty:
            nonce +=1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block,timestamp)
            hash = crypto_hash(timestamp,last_hash,data,difficulty,nonce)


        return Block(timestamp, last_hash, hash,data,difficulty,nonce)
    @staticmethod   #a static method can be only called using class it does not need opject
    def genesis():
        """
        It returns the genesis block.
        """
    #    return Block(
    #           GENESIS_DATA['last_hash'],
    #           GENESIS_DATA['hash'],
    #           GENESIS_DATA['data']
    #     )
        
        return Block(**GENESIS_DATA) #we can use this line instead of the above return satement this line will unpack all the elements of genesis data.

    @staticmethod
    def adjust_difficulty(last_blaock,new_timestamp):
        """
        This function adjusts the difficulty based on the MINE_RATE.
        It increases the difficulty if blocks are mined too fast and decreases
        the difficulty if the blocks are mined too slow.
        """
        if (new_timestamp - last_blaock.timestamp) < MINE_RATE:
            return last_blaock.difficulty + 1

        if (last_blaock.difficulty - 1)> 0:  #if it is 0 then pyhton will need to find a hash with 63 0's which will take ages to find
            return last_blaock.difficulty - 1

        return 1




def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block,'test')
    print(block)

if __name__=='__main__':
    main()


