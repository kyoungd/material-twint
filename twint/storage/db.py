#!/usr/bin/python
from datetime import datetime, timedelta, date
from kafka import KafkaProducer
import json
import os
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db


def init(db):
    pass
    # do nothing;


def fTable(Followers):
    if Followers:
        table = "followers_names"
    else:
        table = "following_names"
    return table


def uTable(Followers):
    if Followers:
        table = "followers"
    else:
        table = "following"
    return table


def follow(conn, Username, Followers, User):
    pass


def get_hash_id(conn, id):
    return ""


def user(conn, config, User):
    pass


topic = os.getenv('KAFKA_TOPIC', 'TWEET')
bootstrap_servers = os.getenv('KAFKA_URL', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


def postToKafka(tweet):
    msg = json.dumps(tweet)
    future = producer.send(topic, key=b'TWEETS_SAVE',
                           value=msg.encode('utf-8'))
    print(f'Sending msg: {msg}')
    result = future.get(timeout=60)
    metrics = producer.metrics()
    print(metrics)


def tweets(conn, Tweet, config):
    try:
        jsondata = json.dumps(Tweet.__dict__)

        entry = {
            "tweet_text": Tweet.tweet,
            "author_id": Tweet.user_id_str,
            "tweet_id": Tweet.id_str,
            "retweet_count": Tweet.retweets_count,
            "replies_count": Tweet.replies_count,
            "likes_count": Tweet.likes_count,
            "quote_count": 0,
            "user_id": Tweet.user_id_str,
            "user_name": Tweet.username,
            "symbol": config.Database,
            "tweet_json": jsondata,
            "tweet_dt": Tweet.datetime}
        postToKafka(entry)
    except (Exception) as error:
        print(error)
        return 0


def Conn(database):
    if database:
        return ""
    else:
        return ""
