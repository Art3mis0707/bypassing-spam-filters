import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\Hackathon\\spam_ham_dataset.csv')

spam_messages = df[df['label'] == 'ham']

random_spam_messages = spam_messages.sample(n=50, random_state=42)

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 1, 1)
time_diff = end_date - start_date

random_timestamps = [start_date + timedelta(seconds=np.random.randint(time_diff.total_seconds())) for _ in range(50)]

data = {'messages': random_spam_messages['text'].tolist(),
        'timestamp': [timestamp.strftime('%Y-%m-%d %H:%M:%S') for timestamp in random_timestamps]}


random_spam_df = pd.DataFrame(data)


random_spam_df.to_csv('modified_ham.csv', index=False)

print("CSV file created successfully.")
