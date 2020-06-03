# Ingestion
Using the python scrip created it dump the json request to my S3 bucket.

#Processing
This will use spark on emr.

# send file directly to emr

scp -i ~/Desktop/RunSparkJobKey.pem /home/desktop/Desktop/BigData/aws_project/processing/emr_jbo.py  hadoop@ec2-34-237-76-170.compute-1.amazonaws.com:~/
emr_jbo.py

# Get file from EMR
scp -i RunSparkJobKey.pem hadoop@ec2-34-237-76-170.compute-1.amazonaws.com:/home/hadoop/emr_jbo.py /home/desktop/Desktop/
