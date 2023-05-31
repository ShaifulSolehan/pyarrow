#learning pre processing data
#feather is a portable file format that stored arrow table or data frames
#pyarrow manages data in array and table, most commonly used format is Parquet and IPC
#ARROW IPC format
import pyarrow.feather as feather
read_df = feather.read_feather('air_passengers.feather')
read_dt = feather.read_table('air_passengers.feather')
print(read_df)
print(read_dt)

