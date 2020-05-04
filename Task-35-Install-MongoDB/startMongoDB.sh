#!/bash/bin

cd

#Start the mongo db server
sudo mongod --port 27017 --dbpath /data/db

#Run the mongo cli
mongo

