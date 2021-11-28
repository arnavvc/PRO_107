import pandas as bear
import plotly.express as px

df = bear.read_csv("data.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(
    mean,
    x = "student_id", 
    y = "level", 
    size = "attempt",
    size_max = 20,
    color = "attempt",
)
fig.show()