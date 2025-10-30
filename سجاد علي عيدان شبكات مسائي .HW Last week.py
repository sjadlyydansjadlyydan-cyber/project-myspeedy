import numpy as np
import pandas as pd


np.random.seed(22)
temps = np.random.randint(15, 41, size=10)


print("Temperature readings:")
for i, t in enumerate(temps, start=1):
    print(f"{i}) {t}°C")


avg = np.mean(temps)
print("Average temperature:", round(avg, 2))


temps = temps.copy()
temps[temps < avg] += 2


print("Original:", temps)
print("Fixed   :", temps)


print("\n--- Statistics ---")
print(f"Original -> Min: {temps.min()}, Max: {temps.max()}, Mean: {temps.mean():}")
print(f"Fixed    -> Min: {temps.min()}, Max: {temps.max()}, Mean: {temps.mean():}")


df = pd.DataFrame({
    "Original": temps,
    "Fixed": temps
})

print("First 5 rows of DataFrame:")
print(df.head())