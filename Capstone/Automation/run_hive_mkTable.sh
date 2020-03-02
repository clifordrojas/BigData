#!/bash/sh

cd

hive -e "drop table weed"
echo "weed table droopped"

hive -f "/home/desktop/Desktop/BigData/Capstone/Processing_to_warehouse/createTable.hql"
echo "weed table created"
