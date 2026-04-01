import pandas as pd
df = pd.read_csv("12payton/imdb_top_250_movie.csv")  # read_file
print(df.head())
print(df.columns)  # see just columns

top_movie = df.loc[df["num_votes"].idxmax()]  # top movie from people votes
print("Top movie based on votes :")
print(top_movie)

# value_counts ,count how many time repited(about genres)
genre_count = df["genres"].value_counts()
print("most common genres:")
print(genre_count)

top_genre = genre_count.idxmax()  # top gener
print("Top genre:", top_genre)

# average time of the all the movies with .mean() from "runtime_minutes"
avg_runtime = df["runtime_minutes"].mean()
print("Average runtime:", avg_runtime)

# long_movie with .idxmax()
longest_movie = df.loc[df["runtime_minutes"].idxmax()]
print("longest movie:")
print(longest_movie)

summary = pd.DataFrame({
    "metric": [
        "top movie (votes)",
        "top genre",
        "average runtime",
        "longest movie"
    ],
    "value": [
        top_movie["title"],
        top_genre,
        avg_runtime,
        longest_movie["title"]
    ]
})

summary.to_excel("imdb_summary.xlsx", index=False)
