import ofxparse
import random
import datetime
from io import StringIO

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime('%Y%m%d%H%M%S')


def generate_random_transaction(account):
    
    transaction = ofxparse.Transaction()
    transaction.TRNTYPE = random.choice(['CREDIT', 'DEBIT'])
    transaction.DTPOSTED = generate_random_date(datetime.date(2023, 1, 1), datetime.date.today())
    transaction.TRNAMT = round(random.uniform(-1000, 1000), 2)
    transaction.FITID = str(random.randint(100000, 999999))
    transaction.MEMO = random.choice(['Supermarket', 'Restaurant', 'Salary', 'Rent', 'Utilities', 'Car', 'Phone', 'Online Shopping', 'Travel', 'Investment'])
    account.statement.transactions.append(transaction)

# Carregar um arquivo OFX existente (substitua pelo caminho do seu arquivo)
with open('test_file.ofx', 'rb') as f:
    ofx = ofxparse.OfxParser.parse(f)

#Obter a primeira conta (ajuste se necessário)
account = ofx.accounts[0]

# Gerar transações aleatórias e adicionar à conta
for _ in range(1):
    generate_random_transaction(account)

ofx.accounts.append(account)    
ofxPrinter = ofxparse.OfxPrinter(ofx = ofx, filename="teste_1.ofx")

#ofxPrinter.ofx.accounts.append(account)
ofxPrinter.write()

# ofx_data = StringIO()
# ofx_data.write("OFX\n")
# ofx_data.write("<OFX>\n")
# ofx_data.write("  <BANKMSGSRSV1>\n")
# ofx_data.write("    <STMTTRN>\n")
# ofx_data.write("      <TRNSTYPE>CHECK</TRNSTYPE>\n")
# ofx_data.write("      <DTPOSTED>20241120</DTPOSTED>\n")
# ofx_data.write("      <TRNAMT>-50.00</TRNAMT>\n")
# ofx_data.write("      <FITID>12345</FITID>\n")
# ofx_data.write("      <NAME>Pagamento de Exemplo</NAME>\n")
# ofx_data.write("      <MEMO>Descrição do pagamento</MEMO>\n")
# ofx_data.write("    </STMTTRN>\n")
# ofx_data.write("  </BANKMSGSRSV1>\n")
# ofx_data.write("</OFX>\n")

# Escrever o OFX modificado em um novo arquivo
# with open('novo_arquivo_ofx.ofx', 'wb') as f:
#    f.write(ofx_data.getvalue().encode('utf-8'))