from scrapers.ScraperMercator import ScraperMercator


def main():
    scm = ScraperMercator(fetch_limit=100, fetch_offset=0, waiting_time=5)
    scm.work()


if __name__ == "__main__":
    main()
