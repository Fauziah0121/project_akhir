import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpsdh01r01qkode1atrgcpsdh01r01qkode1ats0")

    news = finnhub_client.general_news('general', min_id=0)

    return news
