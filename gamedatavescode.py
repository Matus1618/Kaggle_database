# 1. Import knižníc

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print("\n","import","\n")

# 2. Načítanie CSV súboru

df = pd.read_csv("Games.csv")
print("\n","načítanies csv","\n")

# 3. Prvá kontrola dát

print(df.head()) # prvé riadky
print(df.info()) # typy stĺpcov a chýbajúce hodnoty
print(df.describe()) # štatistiky číselných stĺpcov
print("\n","prvá 3","\n")

# 4. Top 10 najpredávanejších hier

top_games = df.nlargest(10, "Sales")
print(top_games[["Name","Sales"]])
print("\n","print 4","\n")

# 5. Pedaj podľa žánrov

sales_by_genre = df.groupby("Genre")["Sales"].sum().sort_values(ascending=False)
print(sales_by_genre)
print("\n","print 5","\n")

# 6. Najčastejší vývojári a vydavatelia

print(df["Developer"].value_counts().head(10))
print(df["Publisher"].value_counts().head(10))
print("\n","print 6","\n")

# 7. Graf

df["Release"]=pd.to_datetime(df["Release"], format="%b-%y", errors="coerce")

plt.figure(figsize=(10, 6))
df["Release"].dropna().dt.year.hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Game Release Years")
plt.xlabel("Release Year")
plt.ylabel("Frequency")
plt.show()
print("\n","print 7 graf","\n")

# 8. Top 10 žánrov

plt.figure(figsize=(10,6))
df["Genre"].value_counts().head(10).plot(kind="bar", color="purple")
plt.title("Top 10 Games Genres")
plt.xlabel("Genre")
plt.ylabel("Frequency")
plt.show()
print("\n","print 8 top 10 žánrov","\n")

# 9. Top 10 vývojárov

plt.figure(figsize=(10,6))
df["Developer"].value_counts().head(10).plot(kind="bar", color="green")
plt.title("Top 10 Developers by Games Count")
plt.xlabel("Developer")
plt.ylabel("Frequency")
plt.show()
print("\n","print 9 part 1/2","\n")

# Histogram predajov

plt.figure(figsize=(10,6))
df["Sales"].dropna().hist(bins=30, color="orange", edgecolor="black")
plt.title("Distribution of Sales")
plt.xlabel("Sales (milions)")
plt.ylabel("Frequency")
plt.show()
print("\n","print 9 part 2/2","\n")