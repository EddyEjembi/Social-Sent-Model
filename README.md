# Sentiment Analysis of Social Media Text
The *Sentiment Analysis of Social Media Text* project takes a deep dive into the emotions expressed on social media. Today, people use social platforms to share ideas, thoughts, and a wide range of feelings. Traditional sentiment analysis tools don't always capture the subtle emotions like sadness, loneliness, fear, or threat. This research project aims to fix this by using special language models that can better understand the emotions in social media posts and capture a wider range of emotions.

## Key Features
- **Focus on Overlooked Sentiments**: Addressing the limitations of existing sentiment analysis systems, this project places emphasis on sentiments that are frequently overlooked or underrepresented, including depression, suicidal thoughts, and fear.
- **Fine-Tuned Language Models**: Utilizing advanced language models (*gpt-3.5-turbo*), the project fine-tunes its analytical tools to achieve a higher level of accuracy and sensitivity in detecting a broader spectrum of emotions.
- **Data Collection and Preprocessing**: Through rigorous data collection and preprocessing techniques, the project ensures the quality and relevance of the dataset used for training and evaluation.
- **Comprehensive Evaluation**: The research project incorporates thorough evaluation processes to measure the effectiveness of the fine-tuned models in capturing and classifying a wider range of emotional states in social media text.

## How to Use
To access/use the  fine-tuned model, you make a request to the API.
The API requires just one Parameter:
The tweet by a particular user (in text)

**Project endpoint**: https://social-sent-model.vercel.app/

The fine-tuned model returns the emotion of that particular tweet.


A sample request is seen on the image below.

![Screenshot of a request made.](https://github.com/EddyEjembi/Social-Sent-Model/blob/master/post_I.png)

> [!NOTE]
> This project uses OpenAI’s content filtering system. It returns an issue when the prompt is flagged by OpenAI content monitoring system.
> 
![Screenshot of a request made.](https://github.com/EddyEjembi/Social-Sent-Model/blob/master/post_II.png)
