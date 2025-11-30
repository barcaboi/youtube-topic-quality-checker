from utils.scraper import scrape_youtube_topic
from utils.calculations import normalize_score

from agents.keyword_agent import KeywordAgent
from agents.competition_agent import CompetitionAgent
from agents.difficulty_agent import DifficultyAgent
from agents.seo_agent import SEOAgent
from agents.trend_agent import TrendAgent
from agents.value_agent import ValueAgent
from agents.rating_agent import RatingAgent
from agents.audience_agent import AudienceAgent
from agents.aggregator_agent import AggregatorAgent


def main():
    print("\n===== YouTube Topic Quality Checker =====\n")

    # 1️⃣ Topic input
    topic = input("Enter YouTube topic: ")

    # 2️⃣ Scraper Agent → fetch data
    print("\n[Scraper] Fetching data...")
    scraped = scrape_youtube_topic(topic)
    if not scraped:
        print("❌ Error fetching topic data")
        return

    print("[Scraper] Data fetched successfully!\n")

    # 3️⃣ Initialize agents
    agents = {
        "keyword": KeywordAgent(),
        "competition": CompetitionAgent(),
        "difficulty": DifficultyAgent(),
        "seo": SEOAgent(),
        "trend": TrendAgent(),
        "value": ValueAgent(),
        "rating": RatingAgent(),
        "audience": AudienceAgent()
    }

    results = {}

    # 4️⃣ Run agents
    print("Running evaluation agents...\n")
    for name, agent in agents.items():
        try:
            score = agent.run(scraped)
            results[name] = normalize_score(score)
            print(f" - {name.capitalize()} Score: {results[name]}")
        except Exception as e:
            print(f"❌ Agent {name} failed: {e}")

    # 5️⃣ Aggregate final score
    print("\nAggregating final score...\n")
    aggregator = AggregatorAgent()
    final_score = aggregator.combine(results)

    print("\n===== FINAL QUALITY REPORT =====\n")
    print(f"Topic: {topic}")
    print(f"Final Quality Score: {final_score}/100")
    print("\nDetailed Breakdown:")
    for k, v in results.items():
        print(f" {k.capitalize()} : {v}")

    print("\n===========================================\n")


if __name__ == "__main__":
    main()

