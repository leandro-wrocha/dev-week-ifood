class ReportFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calculate_nps(self):
    detractors = sum([1 for feedback in self.feedbacks if feedback.grade <= 6])
    prosecutors = sum([1 for feedback in self.feedbacks if feedback.grade >= 9])

    return (prosecutors - detractors) / len(self.feedbacks) * 100