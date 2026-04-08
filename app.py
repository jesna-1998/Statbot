import pandas as pd
from agent import create_agent
from utils import save_chart

# load CSV
df = pd.read_csv("data/sample.csv")

# create AI agent
agent, _ = create_agent("data/sample.csv")

print("📊 StatBot Pro (Final Project)")
print("Type 'exit' to quit")

while True:
    query = input("\nAsk your question: ").lower()

    if query == "exit":
        break

    # safety
    if "delete" in query or "os" in query:
        print("❌ Unsafe query blocked")
        continue

    try:
        # ✅ 100% correct logic
        if "rows" in query:
            print("✅ Total rows:", len(df))

        elif "total revenue" in query:
            print("✅ Total Revenue:", df["Revenue"].sum())

        elif "average" in query:
            print("✅ Average Revenue:", df["Revenue"].mean())

        elif "region" in query:
            print("✅ Revenue by Region:\n", df.groupby("Region")["Revenue"].sum())

        elif "chart" in query or "plot" in query:
             save_chart(df)

        # 🤖 AI fallback
        else:
            print("🤖 Using AI...")
            response = agent.run(query)
            print("AI Response:", response)

    except Exception as e:
        print("⚠️ Error:", e)