import pandas as pd
from dotenv import load_dotenv
from models.feedback import Feedback
from services.reportFeedback import ReportFeedback
from services.generateGraphic import GenerateGraphicsNPS

load_dotenv()

data = pd.read_csv('./contents/feedbacks.csv', delimiter=';')

feedbacks = [Feedback(line['grade'], line['comment']) for index, line in data.iterrows()]

# this same result of code above
# feedbacks = dados.apply(lambda linha: Feedback(linha['nota'], linha['comentario']), axis=1)

report = ReportFeedback(feedbacks)
nps = report.calculate_nps()

responseIA = report.analyze_sentiments()
graphic = GenerateGraphicsNPS(nps)

print(responseIA)
graphic.execute()