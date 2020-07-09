#Pyhton Blockchain
from backend.blockchain.block import Block   #importing the block class from block.py file
#from block import genesis, mine_block #we don't need to import them because now they are a part of block
#class and we have already imported the block class

class Blockchain:
    """
    Blockchain is a public ledger used to record transactions
    It is a collection of blocks which contain the data and adress
    of next and previous block
    """
    def __init__(self):
        self.chain= [Block.genesis()]   #The first item in the chain wiil be genesis block 

    def add_block(self,data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))  #This line is adding a single block to blockchain everytime we run the program
        #In the above line we have used append method which is used to add a single element in list
        
    def __repr__(self):   #repr method returns a printable representation of an object
        return f'Blockchain: {self.chain}'        #here f means formatted

def main():
    blockchain = Blockchain()  #creating an instance
    blockchain.add_block('first')
    blockchain.add_block('second')
    blockchain.add_block('third')
    print(blockchain)
    print(f'blockchain.py __name__ : {__name__}')#The __name__ method gives the value based on how we execute the script

if __name__=='__main__':
    main()

