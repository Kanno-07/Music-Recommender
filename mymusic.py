import streamlit as st
import requests

st.title("Music Recommendation System")
st.write("Enter your favorite music genre and we'll recommend songs for you!")

genre = st.text_input("Enter Your Favorite Music Genre", "")

def recommend_music(genre):
    # YouTube Data API key 
    api_key = 'AIzaSyCdN4cQSiSNoZDGGSmDQHiry3osEq9NHB0'  
    # YouTube API endpoint for video search
    endpoint = 'https://www.googleapis.com/youtube/v3/search'
    # Parameters for the API request
    params = {
        'part': 'snippet',
        'q': f'{genre} music',  # Include genre in search query
        'type': 'video',
        'maxResults': 5,  # Limit the number of results to 5
        'key': api_key
    }
    
    # Make a GET request to the YouTube Data API
    response = requests.get(endpoint, params=params)
    data = response.json()
    
    # Extract video information from the API response
    videos = data.get('items', [])
    
    return videos

if st.button("Recommend Music"):
    if genre:
        recommended_music = recommend_music(genre)
        # Display the recommended music videos
        for video in recommended_music:
            video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            st.markdown(f"[{video['snippet']['title']}]({video_url})")
    else:
        st.write("Please enter a music genre to get recommendations.")
