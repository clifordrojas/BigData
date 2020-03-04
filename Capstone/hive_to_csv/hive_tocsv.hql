insert overwrite local directory "~/Desktop/weed.csv"
     row format delimited
     fields terminated by ','
     select * from weed;

