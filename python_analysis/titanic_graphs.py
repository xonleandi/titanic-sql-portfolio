import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Connecting...")

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="titanic_db",
        user="postgres",
        password="postgres"
    )
    print("Connected!")

    df = pd.read_sql("SELECT * FROM titanic", conn)
    print(f"Loaded {len(df)} rows")

    conn.close()
    df["age"] = df["age"].fillna(df["age"].mean())

    # Graph 1
    plt.figure()
    survival = df.groupby("pclass")["survived"].mean() * 100
    plt.bar([1,2,3], survival.values, color=["red","green","blue"])
    plt.title("Survival by Class")
    plt.ylabel("Survival %")
    plt.savefig("graph_1.png")
    plt.close()
    print("graph_1.png")

    # Graph 2
    plt.figure()
    survival_sex = df.groupby("sex")["survived"].mean() * 100
    plt.bar(["Female","Male"], survival_sex.values, color=["pink","lightblue"])
    plt.title("Survival by Gender")
    plt.savefig("graph_2.png")
    plt.close()
    print("graph_2.png")

    # Graph 3
    plt.figure()
    survived_age = df[df["survived"]==1]["age"]
    died_age = df[df["survived"]==0]["age"]
    plt.hist(died_age, bins=30, alpha=0.5, label="Died", color="red")
    plt.hist(survived_age, bins=30, alpha=0.5, label="Survived", color="green")
    plt.legend()
    plt.title("Age Distribution")
    plt.savefig("graph_3.png")
    plt.close()
    print("graph_3.png")

    # Graph 4
    plt.figure()
    numeric = df[["survived","pclass","age","sibsp","parch","fare"]]
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f")
    plt.title("Correlation")
    plt.savefig("graph_4.png")
    plt.close()
    print("graph_4.png")

    print("ALL DONE!")

except Exception as e:
    print(f"ERROR: {e}")
