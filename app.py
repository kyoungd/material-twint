import twint
import os
from flask import Flask, request
from flask_cors import CORS
'''
app.py - Make twint into an API
'''


def search_result_db(c, run):
    print("[+] Beginning DB test in {}".format(str(run)))
    c.Since = "2021-5-14"
    c.Verified = True,
    c.Search = "AAPL"
    c.Database = "AAPL"
    c.Limit = 1000
    c.Store_object = True
    c.User_full = True
    run(c)


def main():
    conn = twint.storage.db.Conn('random-id')
    # rules = twint.storage.db.get_search_rules(conn)
    # for rule in rules:
    #     print(rules)
    c = twint.Config()
    c.Since = "2021-05-25 00:00:00"
    c.Verified = True,
    c.Search = "gogl"
    c.Database = "gogl"
    c.Limit = 1000
    c.Store_object = True
    c.User_full = True
    twint.run.Search(c)
    print("[+] Run complete!")


# if __name__ == '__main__':
#     main()

app = Flask(__name__)
CORS(app)


@app.route("/tweets", methods=['POST'])
def score():
    try:
        messages = request.get_json()['messages']
        message = messages[0]
        if (message['key'] == 'TWEETS_GET'):
            symbol = message['value']['symbol']
            from_dt = message['value']['from_dt']
            conn = twint.storage.db.Conn(symbol)
            # ------------------------------------------------------
            c = twint.Config()
            # c.Since = from_dt.strftime("%Y-%m-%d %H:%M:%S")
            c.Since = from_dt
            c.Verified = True,
            c.Search = symbol
            c.Database = symbol
            c.Limit = 1000
            c.Store_object = True
            c.User_full = True
            twint.run.Search(c)
    except (Exception) as error:
        print(error)
    return "OK"


@app.route("/live/ping", methods=['GET'])
def test():
    return "OK"


if __name__ == '__main__':
    hostEnv = os.getenv('HOST_URL', '0.0.0.0')
    portEnv = os.getenv('HOST_PORT', 8101)
    app.run(host=hostEnv, port=portEnv, debug=False, threaded=True)
