import feedparser
import ssl

# https://stackoverflow.com/a/28296087
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

RSS = 'https://www.cprime.com/resources/blog/rss/'
MAX_ENTRIES = 5


def get_pybites_last_entries(**kwargs):
    """Get the last 5 entries of Cprime blog (might take a bit)"""
    data = feedparser.parse(RSS)

    output = []
    for item in data['entries'][:MAX_ENTRIES]:
        title = item['title']
        published = item['published']
        url = item['link']
        output.append('{} ({})\n{}\n'.format(title, published, url))

    return '\n'.join(output)


if __name__ == '__main__':
    output = get_pybites_last_entries()
    print(output)
