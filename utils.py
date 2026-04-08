import matplotlib.pyplot as plt
import os

def save_chart(df):
    try:
        os.makedirs("charts", exist_ok=True)  # ensure folder

        df.groupby("Region")["Revenue"].sum().plot(kind="bar")
        plt.title("Revenue by Region")

        plt.savefig("charts/output.png")  # save
        plt.close()

        print("✅ Chart saved successfully!")

    except Exception as e:
        print("❌ Chart error:", e)