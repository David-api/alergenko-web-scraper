from scrapers.ScraperMercator import ScraperMercator
from RedisConnection import RedisConnection


def main():
    server = RedisConnection(host="localhost", port=6379, password="", decode_responses=True)
    con = server.create_connection()

    scm = ScraperMercator(connection=con, fetch_limit=100, fetch_offset=100, waiting_time=5)
    scm.work()

    con.close()


if __name__ == "__main__":
    main()
