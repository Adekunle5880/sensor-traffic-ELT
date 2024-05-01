import pandas as pd 

# Load data into dataframe
data = pd.read_csv('/Users/expert/Desktop/10-Academy/week-2/sensor-data-project/utils/output.csv')

#print(data.head())
#print(data.columns)

# split data into trajectories and vehicles
trajectories = data[['track_id', ' lat', ' lon', ' speed', ' lon_acc', ' lat_acc', ' time']]
vehicles = data[['track_id', ' type', ' traveled_d', ' avg_speed']]

# save split data as csv
trajectories.to_csv('trajectories.csv', index=False)
vehicles.to_csv('vehicle.csv', index=False)
