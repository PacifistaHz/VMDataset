import pandas as pd
import numpy as np

# Rastgele veri oluşturma
data = {
    'OrderID': np.arange(1, 101),
    'CustomerID': np.random.randint(1, 51, size=100),
    'ProductID': np.random.randint(1, 21, size=100),
    'ProductName': np.random.choice(['Product_A', 'Product_B', 'Product_C'], size=100),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Toys'], size=100),
    'Quantity': np.random.randint(1, 10, size=100),
    'Price': np.random.uniform(5, 100, size=100).round(2),
    'OrderDate': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Country': np.random.choice(['USA', 'UK', 'Germany', 'France', 'Canada'], size=100)
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Veriyi CSV olarak kaydetme
df.to_csv('ecommerce_data.csv', index=False)

print("Veri seti oluşturuldu ve 'ecommerce_data.csv' olarak kaydedildi.")
