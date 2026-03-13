import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(
    page_title="Audible Book Recommendation",
    page_icon="📚",
    layout="wide"
)

# Load data
books = pickle.load(open('model/books.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

df = pd.DataFrame(books)

# Recommendation function
def recommend(book):

    index = df[df['Book Name'] == book].index[0]
    distances = similarity[index]

    book_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended = []

    for i in book_list:
        title = df.iloc[i[0]]['Book Name']

        if title not in recommended:   # remove duplicates
            recommended.append({
                "title": title,
                "author": df.iloc[i[0]]['Author'],
                "rating": df.iloc[i[0]]['Rating']
            })

    return recommended


# Header
st.markdown(
"""
<h1 style='text-align:center;'>📚 Audible Intelligent Book Recommendation System</h1>
<p style='text-align:center;font-size:18px;'>
Discover books similar to your favorite ones using NLP and Machine Learning
</p>
""",
unsafe_allow_html=True
)

st.divider()

# Sidebar
st.sidebar.title("📖 Select Book")

selected_book = st.sidebar.selectbox(
    "Choose a Book",
    df['Book Name'].values
)

if st.sidebar.button("✨ Recommend Books"):

    recommendations = recommend(selected_book)

    st.subheader("📚 Recommended Books")

    col1, col2, col3 = st.columns(3)

    for idx, book in enumerate(recommendations):

        with [col1, col2, col3][idx % 3]:

            st.markdown(
                f"""
                <div style="
                padding:15px;
                border-radius:10px;
                border:1px solid #ddd;
                margin-bottom:20px;
                background-color:#fafafa;
                ">
                <h4>📘 {book['title']}</h4>
                <p>👨‍💼 <b>Author:</b> {book['author']}</p>
                <p>⭐ <b>Rating:</b> {book['rating']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )