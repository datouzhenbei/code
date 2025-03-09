def proof_of_work(block, difficulty):
    target = '0' * difficulty  # 目标前导零的数量
    while True:
        block.nonce += 1
        block_hash = block.calculate_hash()
        if block_hash.startswith(target):
            return block_hash
