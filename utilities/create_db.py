
import pandas as pd
import sqlalchemy as sa
from helpers import base

engine = sa.create_engine('sqlite:///' + base('..', 'app', 'odyssey.db'))
#engine = sa.create_engine('sqlite:///odyssey.db')

def read_odyssey():

    # Odyssey has the court dates.
    # filename = "Odyssey-JobOutput-June 01, 2016 06-32-43-1609654-3.TXT"
    #filename = 'Odyssey-Test Data.TXT'
    #filename = 'odyssey.txt'
    #filepath = "..\\data\\Odyssey" + '\\' + filename
    #filename = 'odyssey.txt'
    #filepath = "..\\data\\Odyssey" + '\\' + filename

    df_odyssey = pd.read_csv(base('..', 'data', 'odyssey', 'odyssey.txt'))

    # split name into first and last "parts" then remove spaces for later searching
    df_odyssey['last_name'] = df_odyssey['Party Name'].str.split(',').str[0]
    df_odyssey['lastname_stripped'] = df_odyssey['last_name'].str.replace(' ','')
    df_odyssey['first_name'] = df_odyssey['Party Name'].str.strip().str.split(',').str[1]
    df_odyssey['firstname_stripped'] = df_odyssey['first_name'].str.replace(' ','')

    print 'len(df_odyssey) = ', len(df_odyssey)
    df_odyssey.to_sql('odyssey', engine, if_exists='replace')


if __name__ == "__main__":
    read_odyssey()
