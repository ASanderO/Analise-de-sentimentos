import os
import argparse
import googleapiclient.discovery
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

API_KEY = os.getenv('API_KEY')

if API_KEY is None:
    raise Exception("A chave de API não foi encontrada no arquivo .env")

youtube_service = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_video_comments(youtube, **kwargs):
    comments = []
    results = youtube.commentThreads().list(**kwargs).execute()

    while results:
        for item in results['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment_text)

        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = youtube.commentThreads().list(**kwargs).execute()
        else:
            break

    return comments

def analyze_sentiments(comments):
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        sentiment = analysis.sentiment.polarity
        sentiments.append(sentiment)
    return sentiments

def main():
    parser = argparse.ArgumentParser(description="Analyze sentiments of YouTube video comments.")
    parser.add_argument('videoid', type=str, help="YouTube video ID")

    args = parser.parse_args()
    video_id = args.videoid

    comments = get_video_comments(
        youtube_service,
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    )

    sentiments = analyze_sentiments(comments)

    for i, (comment, sentiment) in enumerate(zip(comments, sentiments), start=1):
        sentiment_label = "Positivo 😀" if sentiment > 0 else ("Negativo ☹️" if sentiment < 0 else "Neutro 😐")
        print(f"Comentário {i}:")
        print(f"Texto: {comment}")
        print(f"Sentimento: {sentiment_label}\n")


if __name__ == "__main__":
    main()
