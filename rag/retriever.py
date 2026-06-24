def retrieve(db, query):

    results = db.similarity_search(
        query,
        k=8
    )

    context="\n\n".join(
        [r.page_content for r in results]
    )

    return context