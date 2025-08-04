import pandas as pd

# Dummy Data
data = {
    'month':['Jan', 'Feb', 'Mar'],
    'revenue' :[1000, 1500, 1230]
}

df = pd.DataFrame(data)

print("Agerage revenue:", df['revenue'].mean())