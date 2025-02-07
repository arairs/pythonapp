from flask import Flask, request
import psycopg2
app = Flask(__name__)
@app.route('/')
def home():
    return "Olá, Flask"

@app.route('/item', methods=['POST'])
def post_item():
    data = request.get_json()
    sql = f"INSERT INTO todolist(item, status) VALUES('{data['item']}','{data['status']}')"
    banco(sql)
    return data

def banco(sql):
    resultado = ""
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password

        )
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    except psycopg2.Error as e:
        print("Erro na conexão do banco de dados")

host = "dpg-cuhv0bdds78s73drb2l0-a.oregon-postgres.render.com"
port = "5432"
dbname = "senaidb_rz5u"
user = "senaidb_rz5u_user"
password = "6XvtSHpgvIDOzA2eLygXStXpEKsvZBpd"

if __name__ == '__main__':
    app.run(debug=True)


