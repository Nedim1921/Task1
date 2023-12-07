import pandas as pd

csvFilePath = 'housing_price_dataset.csv'

df = pd.read_csv(csvFilePath)
performColumn = 'Price'

# Sortiranje podataka po najrelevatnijoj perf koloni
sortedDf = df.sort_values(by=performColumn, ascending=False)

# Najveci i najmanji performer po istoj koloni
highestPerformer = sortedDf.iloc[0]
lowestPerformer = sortedDf.iloc[-1]

# Mean, Median i Mode performer
meanPerformer = sortedDf[performColumn].mean()
medianPerformer = sortedDf[performColumn].median()
modePerformer = sortedDf[performColumn].mode()[0]

print("Sortirani podaci po Performance kolini: ")
print(sortedDf)

print("\nNajveci performer: ")
print(highestPerformer)

print("\nNajmanji performer: ")
print(lowestPerformer)

print("\nMean Performer:")
print(meanPerformer)

print("\nMedian Performer:")
print(medianPerformer)

print("\nMode Performer:")
print(modePerformer)

