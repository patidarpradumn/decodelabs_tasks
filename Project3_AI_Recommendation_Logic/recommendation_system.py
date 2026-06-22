"""
DecodeLabs AI Internship
Task 3: AI Recommendation Logic
Author: Pradumn Patidar
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

courses = pd.DataFrame({
    "course_name": [
        "Python for Beginners",
        "Machine Learning Basics",
        "Deep Learning with Neural Networks",
        "Data Analytics with Pandas",
        "Computer Vision with OpenCV",
        "Natural Language Processing",
        "Web Development with Flask",
        "MLOps and Model Deployment",
        "SQL for Data Analysis",
        "Cloud Computing Fundamentals"
    ],
    "tags": [
        "python programming basics coding",
        "machine learning classification regression ai",
        "deep learning neural networks tensorflow ai",
        "data analytics pandas numpy visualization",
        "computer vision opencv image processing ai",
        "nlp text processing language model ai",
        "python flask web development backend",
        "mlops deployment docker github model monitoring",
        "sql database queries analytics data",
        "cloud aws deployment server computing"
    ]
})

def recommend_courses(user_interest, top_n=3):
    all_text = list(courses["tags"]) + [user_interest]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)
    course_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]
    similarity_scores = cosine_similarity(user_vector, course_vectors).flatten()
    courses["similarity_score"] = similarity_scores
    recommendations = courses.sort_values(by="similarity_score", ascending=False).head(top_n)
    return recommendations[["course_name", "similarity_score"]]

def main():
    print("=" * 60)
    print("AI Recommendation Logic System")
    print("=" * 60)
    print("Example interests: python ai, machine learning, data analytics, web development, cloud, mlops")
    print("-" * 60)
    user_interest = input("Enter your interests: ").lower().strip()
    recommendations = recommend_courses(user_interest)
    print("\nRecommended Courses:")
    for index, row in recommendations.iterrows():
        score = round(row["similarity_score"] * 100, 2)
        print(f"- {row['course_name']} | Match: {score}%")

if __name__ == "__main__":
    main()
