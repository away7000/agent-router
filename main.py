from core.router import Router
from agents.polymarket_agent import PolymarketAgent

def main():
    router = Router()

    router.add_agent("polymarket", PolymarketAgent())

    result = router.run("polymarket")

    for r in result:
        print("====")
        print("Market:", r["market"])
        print("Price:", r["price"])
        print("Decision:", r["decision"])


if __name__ == "__main__":
    main()
