import redis


class RedisConnection:
    def __init__(self, host: str, port: int, password: str, decode_responses: bool):
        self.host = host
        self.port = port
        self.password = password
        self.decode_responses = decode_responses
        self.con = redis.StrictRedis(host=self.host, port=self.port, password=self.password,
                                     decode_responses=self.decode_responses)

    def create_connection(self):
        return self.con
