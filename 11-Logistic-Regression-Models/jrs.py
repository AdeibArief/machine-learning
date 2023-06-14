import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk

# Sample job data
job_data = {
    'JobID': [1, 2, 3, 4, 5],
    'Title': ['Software Engineer', 'Data Analyst', 'Marketing Specialist', 'Sales Representative', 'UX Designer'],
    'Skills': ['Python, Java, SQL', 'R, Data visualization', 'Marketing strategy, SEO', 'Sales techniques, CRM', 'User research, Wireframing']
}

# Sample user data
user_data = {
    'UserID': [1, 2, 3],
    'Skills': ['Python, Java, SQL', 'R, Data visualization', 'Marketing strategy, SEO']
}

# Convert data to pandas DataFrames
jobs_df = pd.DataFrame(job_data)
users_df = pd.DataFrame(user_data)

# Preprocess skills data
jobs_df['Skills'] = jobs_df['Skills'].str.lower()
users_df['Skills'] = users_df['Skills'].str.lower()

# Create a matrix of job skills
skills_matrix = jobs_df['Skills'].str.get_dummies(sep=', ')

# Create a function to recommend jobs
def recommend_jobs():
    # Get user skills from the input field
    user_skills = entry_skills.get().lower()

    # Calculate cosine similarity between user skills and job skills
    user_skills_matrix = pd.Series(user_skills.split(', ')).str.get_dummies().reindex(columns=skills_matrix.columns, fill_value=0)
    cosine_sim = cosine_similarity([user_skills_matrix], skills_matrix)

    # Get recommended jobs based on similarity scores
    similar_jobs_indices = cosine_sim.argsort()[0][::-1]
    recommended_jobs = jobs_df.loc[similar_jobs_indices]

    # Clear previous recommendations from the text area
    text_recommendations.delete("1.0", tk.END)

    # Display recommended jobs in the text area
    for index, row in recommended_jobs.iterrows():
        text_recommendations.insert(tk.END, f"Job ID: {row['JobID']}\nTitle: {row['Title']}\n\n")

# Create the GUI
window = tk.Tk()
window.title("Job Recommendation System")

# Create labels and entry fields
label_skills = tk.Label(window, text="Enter your skills (comma-separated):")
label_skills.pack()
entry_skills = tk.Entry(window)
entry_skills.pack()

# Create a button to recommend jobs
button_recommend = tk.Button(window, text="Recommend Jobs", command=recommend_jobs)
button_recommend.pack()

# Create a text area to display recommendations
text_recommendations = tk.Text(window, height=10, width=40)
text_recommendations.pack()

window.mainloop()
