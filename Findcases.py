import settings
import urllib2

def process():
    """
         download pdf file from URL
         check data exists in database
         parse data with format
         insert data to database if data not exists
    """
    # 1. Read the configuration, download PDF
    url = '/'.join(settings.URL)
    data = down_load_pdf(url)
    # 2. Check if the PDF data is matching in PDF file log table
    if(check_in_DataBase(data)):
        # 3. If the file already exists in the table, send an email System Admin Email
        notify(data)
    # 4. Parse PDF Data
    data_parsed = parse_pdf_data(data)
    # 5. Insert data into Database
    if(insert(data_parsed)):
        print "Batch is processed"

def down_load_pdf(url):
    """
        download pdf data from url
    :param url: url pdf
    :return: data get form url
    """
    response = urllib2.urlopen(url)
    return response.read()

def check_in_DataBase(data):
    """
        check data exists in the database
    :param data: pdf data
    :return: True if exists else False
    """
    return True

def parse_pdf_data(data):
    """
       parse pdf data to json fomart
    :param data: pdf data
    :return: data is parsed
    """
    return data

def notify(data):
    """
       send an email System Admin Email
    """
    pass

def insert(data):
    """
        insert data to database
    :param data: pdf data
    :return: True if inserted else False
    """
    return True

def _main():
    process()

if __name__ == '__main__':
    _main()
