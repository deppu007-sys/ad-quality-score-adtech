import pandas as pd

# Step 1: Create Ad Dataset
data = {
    "Ad": ["Ad_A", "Ad_B", "Ad_C", "Ad_D"],
    "Impressions": [1000, 1500, 1200, 900],
    "Clicks": [50, 120, 30, 45],
    "Relevance_Score": [8, 9, 6, 7],        # Out of 10
    "Landing_Page_Score": [7, 8, 5, 6]      # Out of 10
}

df = pd.DataFrame(data)

# Step 2: Calculate CTR
df["CTR"] = df["Clicks"] / df["Impressions"]

# Step 3: Normalize CTR to 10 scale
df["CTR_Score"] = df["CTR"] * 10

# Step 4: Calculate Quality Score
df["Quality_Score"] = (
    df["CTR_Score"] + df["Relevance_Score"] + df["Landing_Page_Score"]
) / 3

# Step 5: Rank Ads
df["Rank"] = df["Quality_Score"].rank(ascending=False)

# Step 6: Display Results
print(df.sort_values(by="Quality_Score", ascending=False))
