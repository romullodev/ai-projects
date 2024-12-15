#!/usr/bin/env python
from CrewAi_Projects.stockanalysis.src.stockanalysis.crew import StockAnalysisCrew, GenerateResearchReportCrew, GenerateFinancialReportCrew, GenerateFillingReportCrew, GenerateRecommendReportCrew
import os


def execute_stock_analysis():
  company = "PLTR"
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  
  unique_recommend_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/unique_recommend"
  report_name = f"unique_recommend_report_{len(os.listdir(unique_recommend_directory_path))}" 
  full_path = f"{unique_recommend_directory_path}/{report_name}.txt"
  with open(full_path, "w+") as f:
    f.write(str(result))       

def generate_research_report():
  company = "PLTR"
  
  research_crew = ResearchReportCrew(company)
  result = research_crew.run()
  
  print(result)
  research_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/research"
  report_name = f"research_report_{len(os.listdir(research_directory_path))}" 
  full_path = f"{research_directory_path}/{report_name}.txt"
  with open(full_path, "w+") as f:
    f.write(str(result))    

def generate_financial_report():
  company = "PLTR"
  research_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/research"
  report_name = "research_report_0" 
  full_path = f"{research_directory_path}/{report_name}.txt"
  with open(full_path, 'r') as arquivo:
    summary = arquivo.read()

  previousSummary = f"""
  Previous Summary Report: 
  {summary}
  """    
  
  research_crew = FinancialReportCrew(company, previousSummary)
  result = research_crew.run()
  
  financial_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/financial_analysis"
  report_name = f"financial_analysis_report_{len(os.listdir(financial_directory_path))}" 
  full_path = f"{financial_directory_path}/{report_name}.txt"
  with open(full_path, "w+") as f:
    f.write(str(result)) 

def generate_filling_report():
  company = "PLTR"
  financial_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/financial_analysis"
  report_name = "financial_analysis_report_0" 
  full_path = f"{financial_directory_path}/{report_name}.txt"
  with open(full_path, 'r') as arquivo:
    summary = arquivo.read()
  
  previousSummary = f"""
  Previous Summary Report: 
  {summary}
  """
  research_crew = FillingAnalysisReportCrew(company, previousSummary)
  result = research_crew.run()
  
  filling_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/filling_analysis"
  report_name = f"filling_analysis_report_{len(os.listdir(filling_directory_path))}" 
  full_path = f"{filling_directory_path}/{report_name}.txt"
  with open(full_path, "w+") as f:
    f.write(str(result))   

def generate_recommend_report():
  company = "PLTR"
  filling_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/filling_analysis"
  report_name = "filling_analysis_report_0" 
  full_path = f"{filling_directory_path}/{report_name}.txt"
  with open(full_path, 'r') as arquivo:
    summary = arquivo.read()
  
  previousSummary = f"""
  Previous Summary Report: 
  {summary}
  """
  research_crew = RecommendReportCrew(company, previousSummary)
  result = research_crew.run()
  
  recommend_directory_path = "CrewAi_Projects/stockanalysis/src/stockanalysis/reports/recommend"
  report_name = f"recommend_report_{len(os.listdir(recommend_directory_path))}" 
  full_path = f"{recommend_directory_path}/{report_name}.txt"
  with open(full_path, "w+") as f:
    f.write(str(result))       


class FinancialCrew:
  
  def __init__(self, company):
    self.company = company

  def run(self):
    inputs = {
        "TipSection": "If you do your BEST WORK, I'll give you a $10,000 commission!",
        "Company": f"{self.company}",
        "PreviousSummary": ""
    }
    
    result = StockAnalysisCrew().crew().kickoff(inputs=inputs)
    return result
  
class ResearchReportCrew:
  
  def __init__(self, company):
    self.company = company

  def run(self):
    inputs = {
        "TipSection": "If you do your BEST WORK, I'll give you a $10,000 commission!",
        "Company": f"{self.company}",
    }
    
    result = GenerateResearchReportCrew().crew().kickoff(inputs=inputs)
    return result      
  
class FinancialReportCrew:
  
  def __init__(self, company, previousSummary):
    self.company = company
    self.previousSummary = previousSummary

  def run(self):
    inputs = {
        "TipSection": "If you do your BEST WORK, I'll give you a $10,000 commission!",
        "Company": f"{self.company}",
        "PreviousSummary": f"{self.previousSummary}"
    }
    
    result = GenerateFinancialReportCrew().crew().kickoff(inputs=inputs)
    return result   

class FillingAnalysisReportCrew:
  
  def __init__(self, company, previousSummary):
    self.company = company
    self.previousSummary = previousSummary

  def run(self):
    inputs = {
        "TipSection": "If you do your BEST WORK, I'll give you a $10,000 commission!",
        "Company": f"{self.company}",
        "PreviousSummary": f"{self.previousSummary}"
    }
    
    result = GenerateFillingReportCrew().crew().kickoff(inputs=inputs)
    return result    
  
class RecommendReportCrew:
  
  def __init__(self, company, previousSummary):
    self.company = company
    self.previousSummary = previousSummary

  def run(self):
    inputs = {
        "TipSection": "If you do your BEST WORK, I'll give you a $10,000 commission!",
        "Company": f"{self.company}",
        "PreviousSummary": f"{self.previousSummary}"
    }
    
    result = GenerateRecommendReportCrew().crew().kickoff(inputs=inputs)
    return result   