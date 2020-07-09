from backend.blockchain.block import Block , GENESIS_DATA

def test_mine_block():
    last_block = Block.genesis()
    data = 'test'
    block = Block.mine_block(last_block, data)

    assert isinstance(block,Block)  # it will check wheather block is object of Block class
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert block.hash[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()


    assert isinstance(genesis,Block)

    # assert genesis.timestamp == GENESIS_DATA['timestamp']
    # assert genesis.last_hash == GENESIS_DATA['last_hash']
    # assert genesis.hash == GENESIS_DATA['hash']
    # assert genesis.data == GENESIS_DATA['data']

#we are using for loop instead of the above line to reduce the redundancy

    for key, value in GENESIS_DATA.items():
        getattr(genesis,key) == value
