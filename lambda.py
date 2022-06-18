import sys
import logging
import rds_config
import json
import pymysql

rds_host  = "rds-instance-endpoint"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    
    print("EVENT")
    print(event)
    print("context")
    print(context)
    json_load = (json.load(event))
    name = json_load['name']    
    email = json_load['email']    
    phone = json_load['phone']    
    letter = json_load['letter']    

    
    curr = conn.cursor()
    curr.execute('insert into Student (Name, Email,Phone,letter) values(name,email,phone,letter)')
        
    conn.commit()
       
    
    return event