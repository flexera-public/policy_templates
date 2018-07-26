# Helper function to get account's shard from an account hash

def rs_account_shard(account_hash): 
    account_href = account_hash["legacy"]["account_url"]
    shard = account_href.split(".")[0]
    shard = shard.split("-")[1]
    return shard