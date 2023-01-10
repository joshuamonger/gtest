import shutil
import sqlite3

connection = sqlite3.connect("/Users/WindUpBird/Library/Application Support/Dock/desktoppicture.db")
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM data ORDER BY rowID DESC LIMIT 1;').fetchall()
fileconv = [i[0] for i in rows]
file = str(fileconv[0])


# For system default pictures
fixsrc = file.replace('/System/Library/Desktop Pictures/', '')
src_path = "/System/Library/Desktop Pictures/" + str(fixsrc)
dst_path = "/Users/WindUpBird/Desktop/" + str(fixsrc)

# For other locations
# fixsrc = file.replace('~/Pictures/', '')
# src_path = "/Users/WindUpBird/Pictures/" + str(fixsrc)
# dst_path = "/Users/WindUpBird/Desktop/" + str(fixsrc)

shutil.copy(src_path, dst_path)