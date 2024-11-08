#!/usr/bin/env python
from crew import StockAnalysisCrew   

class FinancialCrew:
  
  def __init__(self, company):
    self.company = company

  def run(self):
    inputs = {
        'TipSection': "If you do your BEST WORK, I'll give you a $10,000 commission!",
        'Company': company
    }
    
    result = StockAnalysisCrew().crew().kickoff(inputs=inputs)
    return result

if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  company = "PLTR"
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
  with open("report.txt", "w+") as f:
    f.write(result)