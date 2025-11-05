import pandas as pd

df = pd.DataFrame({
    'Name': ['Laptop', 'Phone', 'Tablet'],
    'Price': [1250, 900, 750],
    'Quantity': [21, 20,0]
})

df['Total'] = df['Price'] * df['Quantity']
df = df.sort_values('Total', ascending=False)
df.to_csv('products.csv', index=False)
df_loaded = pd.read_csv('products.csv')

print(df_loaded)
