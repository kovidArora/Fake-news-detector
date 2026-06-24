   
import streamlit as st
import os


from rag.news_loader import fetch_news
from rag.vector_store import create_vectorstore
from rag.retriever import retrieve
from llm.detector import analyze_news
print ("hello")
import newsapi
print("NEWSAPI INSTALLED")  


st.title("Fake News Detector")

news = st.text_area(
    "Enter news article"
)


if st.button("Analyze"):

    if not news:
        st.warning("Please enter a news article")
        st.stop()


    with st.spinner("Checking news..."):

        query = " ".join(news.split()[:4])

        docs = fetch_news(
            st.secrets("NEWS_API_KEY"),
            query
            )


        if len(docs) == 0:

            st.warning(
                "⚠️ No matching news articles were found. "
                "Analyzing without external evidence."
            )

            context = """
            No related news articles were found from available sources.
            There is no supporting evidence available.
            """

        else:

            db = create_vectorstore(docs)

            context = retrieve(
                db,
                news
            )
            
        


        result = analyze_news(
            news,
            context
        )


        st.subheader("Result")


        label = result["label"]
        confidence = result["confidence"]


        if label == "REAL":
            st.success(f"✅ {label}")
        else:
            st.error(f"❌ {label}")


        st.metric(
            "Confidence",
            f"{confidence}%"
        )


        st.progress(confidence / 100)


        st.subheader("Why?")


        st.write(
            result["explanation"]
        )


        st.subheader("Key Points")


        for point in result["key_points"]:
            st.write("•", point)