from backend.util.cryptohash import crypto_hash

def test_crypto_hash():
    #The function is supposed to create same hash for same input in different order
    assert crypto_hash('one',3,[2]) == crypto_hash(3,[2],'one')
