from sqlalchemy import create_engine, text

conn_string = "mysql+pymysql://7b2hs00qe8gb7imsur1j:pscale_pw_Ugj318BgkP6jE6UB2Pr7h1Ye2QOx8U9YCdxOdPdF4XX@aws.connect.psdb.cloud/likiscareers?charset=utf8mb4"

engine = create_engine(conn_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())