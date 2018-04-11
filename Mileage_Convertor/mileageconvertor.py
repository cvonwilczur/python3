print("How many kilometers did you cycle today?")
kms = float(input())

miles = round(kms/1.60934, 2)

print(f"Your { kms } km ride was equal to { miles } miles!")
