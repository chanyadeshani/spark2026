start hadoop cluster
- start-dfs.sh
- start-yarn.sh

Copy the test.py to Desktop
- **Submit SPARK job**
'''spark-submit   --master yarn   --deploy-mode cluster   Desktop/test.py'''
- ** See the sttus of the Spark job and output **
From the browser navigate to http://localhost:8088/cluster

check here for sample csvs
https://www.datablist.com/learn/csv/download-sample-csv-files

-**Load CSV from Downloads folder**
download the csv file 'customers-100.csv'
download the test_with_csv.py to Desktop
run the code
'''spark-submit   --master yarn   --deploy-mode cluster   Desktop/test_with_csv.py'''





