class ReportFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calculate_nps(self):
    detractors = sum([1 for feedback in self.feedbacks if feedback.grade <= 6])
    prosecutors = sum([1 for feedback in self.feedbacks if feedback.grade >= 9])

    # functiona lambda is a fuction anonymous, only to filter
    # this example more simple to return the same value of variables above
    # detratores = notas.apply(lambda nota: nota <= 6).sum()
    # promotores = notas[notas >= 9].count()

    return (prosecutors - detractors) / len(self.feedbacks) * 100