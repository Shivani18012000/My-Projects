
import pickle 
import streamlit as st 
import numpy as np


st.header('Book Recommender System')
model=pickle.load(open('modules/model.pkl','rb'))
pivot_books=pickle.load(open('modules/pivot_books.pkl','rb'))
ratings_books_final=pickle.load(open('modules/ratings_books_final.pkl','rb'))
books_names=pickle.load(open('modules/books_names.pkl','rb'))


selected_books=st.selectbox('Type or select a book',books_names)

def fetch_poster(suggestion):
    book=[]
    urls=[]
    idx=[]
    for book_id in suggestion:
        book.append(pivot_books.index[book_id])
    for name in book[0]:
        ids=np.where(ratings_books_final['Title']==name)[0][0]
        idx.append(ids)
    for id in idx:
        url=ratings_books_final.iloc[id]['url']
        urls.append(url)
    return urls
def recommendation(book_name):
    book_list=[]
    book_id=np.where(pivot_books.index==book_name)[0][0]
    distance,suggestion=model.kneighbors(pivot_books.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    poster_url=fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books=pivot_books.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list,poster_url
if st.button('Show Recommendation'):
    recommended_books,url=recommendation(selected_books)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(url[5])
    

