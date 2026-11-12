import pandas as pd

# Importing Pandas library for data analysis and manipulation

df = pd.read_csv(r"C:\Users\aatif\OneDrive\Desktop\CricketIQ_master_v1.csv")

# Loading the cricket dataset
# r represents a raw string, useful for Windows file paths
# Filter Virat Kohli
kohli = df[df["batter"] == "Virat Kohli"].copy()
print(kohli.head())
kohli.info()
print(kohli.describe())
print(kohli.isnull().sum())
# OVERALL BATTING STATISTICS

total_runs = kohli["batter_runs"].sum()
balls_faced = kohli["counts_as_ball_faced"].sum()
fours = kohli["is_four"].sum()
sixes = kohli["is_six"].sum()
dismissals = kohli["is_kohli_out"].sum()
# Official batting strike rate

strike_rate = (total_runs / balls_faced * 100) if balls_faced > 0 else 0
# BYES AND LEGBYES
total_byes = kohli["byes"].sum()
total_legbyes = kohli["legbyes"].sum()
# Combined runs including batter runs, byes and legbyes
combined_runs = total_runs + total_byes + total_legbyes
# Custom strike rate including byes and legbyes
combined_strike_rate = (
    combined_runs / balls_faced * 100
) if balls_faced > 0 else 0
print("\n----- OVERALL PERFORMANCE -----")

print("Batter Runs:", total_runs)
print("Balls Faced:", balls_faced)
print("Fours:", fours)
print("Sixes:", sixes)
print("Dismissals:", dismissals)

print("Official Strike Rate:", round(strike_rate, 2))

print("Total Byes:", total_byes)
print("Total Legbyes:", total_legbyes)

print("Combined Runs:", combined_runs)

print("Custom Strike Rate Including Byes and Legbyes:",
      round(combined_strike_rate, 2))


# BYES AND LEGBYES ANALYSIS
bye_rows = kohli[
    (kohli["byes"] > 0) |
    (kohli["legbyes"] > 0)
].copy()

print("\n----- BYES AND LEGBYES ANALYSIS -----")

print("Bye/Legbye Deliveries:", len(bye_rows))

print("Batter Runs:", bye_rows["batter_runs"].sum())

print("Bye Runs:", bye_rows["byes"].sum())

print("Legbye Runs:", bye_rows["legbyes"].sum())

print("Balls Faced:",
      bye_rows["counts_as_ball_faced"].sum())

# SEASON-WISE ANALYSIS
seasons_stats = (
    kohli.groupby("season")
    [["batter_runs",
      "byes",
      "legbyes",
      "counts_as_ball_faced",
      "is_four",
      "is_six",
      "is_kohli_out"]]
    .sum()
    .assign(         # creat calculated coloumns
        combined_runs=lambda x:
        x["batter_runs"] + x["byes"] + x["legbyes"],

        official_strike_rate=lambda x:
        (x["batter_runs"] / x["counts_as_ball_faced"] * 100)
        .where(x["counts_as_ball_faced"] > 0, 0),
                  # First 0: Checks whether balls faced are greater than zero.
                  # Second 0: If the condition is false, replace the result with zero.

        combined_strike_rate=lambda x:
        (x["combined_runs"] / x["counts_as_ball_faced"] * 100)
        .where(x["counts_as_ball_faced"] > 0, 0)
    )
    .reset_index()
)
print("\n----- SEASON-WISE PERFORMANCE -----")
print(seasons_stats.to_string(index=False))