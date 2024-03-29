from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
import json

def hello(session: Session) -> DataFrame:
    df = session.table("demodb.dev.customers")
    #df = df.groupBy("STATE").count()
    return df

# For local debugging
if __name__ == "__main__":
    session = Session.builder.configs(json.load(
      open("/change_your_path/snowflake_connection.json"))).create()
    print (hello (session).show())
