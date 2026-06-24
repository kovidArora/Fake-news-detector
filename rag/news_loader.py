from newsapi import NewsApiClient


def fetch_news(api_key, query):

    newsapi = NewsApiClient(api_key=api_key)

    articles = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=20
    )


    print("TOTAL ARTICLES:", len(articles["articles"]))


    docs=[]

    for a in articles["articles"]:

        if a["title"]:

            text = f"""
            Title:
            {a['title']}

            Description:
            {a.get('description','')}

            Source:
            {a['source']['name']}
            """

            docs.append(text)


    print("DOCS CREATED:", len(docs))

    return docs