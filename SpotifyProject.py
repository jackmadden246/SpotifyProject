import sqlite3
conn = sqlite3.connect("spotify_artist_data.csv")
cur = conn.cursor()
print("Opened database successfully");
# cur.execute(''' CREATE TABLE spotify_artist_data_new
#  (ID INT PRIMARY KEY           NOT NULL,

#    ARTIST_NAME      TEXT        NOT NULL,

#     LEAD_STREAMS     INT         NOT NULL,

#      FEAT             INT         NOT NULL,

# TRACKS           INT         NOT NULL,
#  STREAMS_OVER_100_MILL INT NOT NULL);''')
# print("Table created successfully");
# conn.close()

# conn = sqlite3.connect("spotify_artist_data.csv")
# cur = conn.cursor()
# print("Opened database successfully");
# conn.execute(" INSERT INTO spotify_artist_data_new (ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (1, 'Drake', 50162292808, 19246513666, 262, 130 )");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (2, 'Bad Bunny', 44369032140, 5391990975, 163, 118 )");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (3, 'Ed Sheeran', 38153682361, 2791278201, 240, 62)");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (4, 'The Weeknd', 34767779741, 4288903657, 186, 72);");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (5, 'Taylor Swift', 32596728109, 424053296, 323, 96)");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT,
# TRACKS, STREAMS_OVER_100_MILL) \
# VALUES (6, 'Justin Bieber', 32465998885, 10816202075, 225, 58)");
# conn.execute(" INSERT INTO spotify_artist_data_new(ID, ARTIST_NAME, LEAD_STREAMS, FEAT, TRACKS,
# STREAMS_OVER_100_MILL) \
# VALUES (7, 'Ariana Grande', 32287682040, 2052297828, 181, 71)");
# print("Table created successfully");
# conn.commit()
# print("Records created successfully");
# conn.close()

conn = sqlite3.connect("spotify_artist_data.csv")
print("Opened database successfully")
cursor = conn.execute("SELECT * FROM spotify_artist_data_new")
for row in cursor:
    print("ID =", row[0])
    print("ARTIST_NAME =", row[1])
    print("LEAD_STREAMS =", row[2])
    print("FEAT =", row[3])
    print("TRACKS =", row[4])
    print("STREAMS_OVER_100_MILL=", row[5])
