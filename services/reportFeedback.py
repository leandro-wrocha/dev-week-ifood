import openai
import os

class ReportFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks
    self.apiKeyOpenia = os.getenv("API_KEY_OPENIA")
    openai.api_key = self.apiKeyOpenia

  def calculate_nps(self):
    detractors = sum([1 for feedback in self.feedbacks if feedback.grade <= 6])
    prosecutors = sum([1 for feedback in self.feedbacks if feedback.grade >= 9])

    # functiona lambda is a fuction anonymous, only to filter
    # this example more simple to return the same value of variables above
    # detratores = notas.apply(lambda nota: nota <= 6).sum()
    # promotores = notas[notas >= 9].count()

    return (prosecutors - detractors) / len(self.feedbacks) * 100

  def analyze_sentiments(self):
    comments_formated = "\n".join([f"- Grade {feedback.grade}! {feedback.comment}" for feedback in self.feedbacks])
    prompt = f"""
              Summarize a general analysis of the following comment:
              {comments_formated}"""

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
            "role": "system",
            "content": "You are a sentiment analysis model focused on feedback regarding educational experiences."
        },
        {
            "role": "user",
            "content": prompt
        }
      ]
    )

    return response.choices[0].message.content