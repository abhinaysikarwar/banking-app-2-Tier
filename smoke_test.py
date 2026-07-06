import boto3 ,os,sys
client=boto3.client("ssm",region_name="us-east-1")

params={
    os.path.basename(p["Name"]): p["Value"]
    for p in client.get_parameters_by_path(
        Path="/application/banking", 
        WithDecryption=True)["Parameters"]
}

required_params = ["DB_HOST", "DB_NAME", "DB_PORT", "DB_USER", "DB_PASSWORD"]
missing=[k for k in required if k not in params]

for k in required:
    if k not in required:
        print(k, "✅")
    else:
        print(k, "❌")

if missing:
    print(f"Failed : {missing}")
    sys.exit(1)


# DB  FIND banking_db and show tables
try:
    connection=pymysql.connect(
        host=params["DB_HOST"],
        user=params["DB_USER"],
        password=params["DB_PASSWORD"],
        database=param["DB_NAME"],
        port=int(params["DB_PORT"]),
        connect_timeout=10
    )

    cur=connection.cursor()
    cur.execute("SHOW DATABASES;")
    tables=[row[0] for row in cur.fetchall()]
    connection.close()
    print(f"{params['DB_NAME']}")
    print(f"tables: {tables}")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)

print("✅ smoke test done")
