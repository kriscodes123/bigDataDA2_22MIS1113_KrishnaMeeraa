import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from minisom import MiniSom
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
df = pd.read_csv("C:/Users/Krishna Meeraa K S/OneDrive/Desktop/BDA DA2 SOM AIRLINE/airline_delay_synthetic.csv") 

# Display the first few rows and shape of the dataset
print(df.head())
print("Dataset shape:", df.shape)

# Step 2: Preprocess the Data
data = df[['ARR_DELAY', 'DEP_DELAY', 'DISTANCE']].values
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 3: Train the Self-Organizing Map (SOM)
# Define SOM parameters
som = MiniSom(x=10, y=10, input_len=data_scaled.shape[1], sigma=1.0, learning_rate=0.5)

# Initialize weights and train SOM
som.random_weights_init(data_scaled)
som.train_random(data_scaled, num_iteration=100)

# Step 4: Visualize the Results
plt.figure(figsize=(7, 7))
plt.bone()  # Set the colormap
plt.title('Self-Organizing Map')
for i in range(data_scaled.shape[0]):
    w = som.winner(data_scaled[i, :])  # Get the winning node
    plt.text(w[0], w[1], str(i), color=plt.cm.jet(data_scaled[i, 0]), fontsize=9)

plt.show()

