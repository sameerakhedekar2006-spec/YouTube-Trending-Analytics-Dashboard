import pandas as pd
import mysql.connector

df = pd.read_csv('C:/Users/Dev/Downloads/USvideos_clean.csv', encoding='utf-8-sig')
df = df[['video_id','trending_date','title','channel_title','category_id','publish_time','views','likes','dislikes','comment_count']]
df = df.fillna(0)

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='root1234', database='youtube_analytics')
cursor = conn.cursor()
cursor.execute('TRUNCATE TABLE youtube_videos')

for _, row in df.iterrows():
    cursor.execute('INSERT INTO youtube_videos (video_id, trending_date, title, channel_title, category_id, publish_time, views, likes, dislikes, comment_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', tuple(row))

conn.commit()
print('Done! Rows inserted:', len(df))
conn.close()