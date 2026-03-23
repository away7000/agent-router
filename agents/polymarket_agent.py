from core.base_agent import BaseAgent
from tools.polymarket_api import get_markets
from tools.local_ai import local_ai


class PolymarketAgent(BaseAgent):
    def run(self, input_data=None):
        markets = get_markets()

        results = []

        for m in markets:
            question = m.get("question")
            prices = m.get("outcomePrices", [])

            if not prices:
                continue

            price = float(prices[0])

            prompt = f"""
            Kamu adalah trader prediction market.

            Market: {question}
            Probability: {price}

            Kasih keputusan:
            BUY YES / BUY NO / SKIP
            """

            decision = local_ai(prompt)

            results.append({
                "market": question,
                "price": price,
                "decision": decision
            })

        return results
