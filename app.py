import twint
import os
'''
app.py - Make twint into an API
'''

def search_result_db(c, run):
    print("[+] Beginning DB test in {}".format(str(run)))
    c.Since = "2021-5-14"
    c.Verified=True,
    c.Search = "AAPL"
    c.Database = "AAPL"
    c.Limit = 1000
    c.Store_object = True
    c.User_full = True
    run(c)


def main():
    conn = twint.storage.db.Conn('random-id')
    rules = twint.storage.db.get_search_rules(conn)
    for rule in rules:
        print(rules)
        c = twint.Config()
        c.Since = rule.last_searched_on.strftime("%Y-%m-%d %H:%M:%S")
        c.Verified=True,
        c.Search = rule.symbol
        c.Database = rule.symbol
        c.Limit = 1000
        c.Store_object = True
        c.User_full = True
        twint.run.Search(c)
        print("[+] Run complete!")


if __name__ == '__main__':
    main()
