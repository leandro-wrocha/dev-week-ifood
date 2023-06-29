import pandas as pd
from models.feedback import Feedback
from services.reportFeedback import ReportFeedback

data = pd.read_csv('./contents/feedbacks.csv', delimiter=';')

feedbacks = [Feedback(line['grade'], line['comment']) for index, line in data.iterrows()]

# this same result of code above
# feedbacks = dados.apply(lambda linha: Feedback(linha['nota'], linha['comentario']), axis=1)

report = ReportFeedback(feedbacks)
nps = report.calculate_nps()

print(nps)