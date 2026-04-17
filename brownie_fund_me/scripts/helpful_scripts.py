from brownie import MockV3Aggregator, accounts, config, network

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    
    if network.show_active() == "ganache-local":
        if len(accounts) > 0:
            return accounts[0]
        local_test_key = config["wallets"].get(
            "ganache_local_key",
            "0xa8629b37eeecd622152b836ebb038efa781c5b009c5cba83f8ac431185e0092d",
        )
        return accounts.add(local_test_key)
    
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(decimals=DECIMALS, starting_price=STARTING_PRICE):
    """Deploy mock contracts for local testing"""
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    
    account = get_account()
    
    if len(MockV3Aggregator) <= 0:
        mock_price_feed = MockV3Aggregator.deploy(
            decimals,
            starting_price,
            {"from": account},
        )
        print(f"MockV3Aggregator deployed to {mock_price_feed.address}")
    else:
        print("Mock already deployed!")
    
    return MockV3Aggregator[-1]
