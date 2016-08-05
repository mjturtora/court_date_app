import pandas as pd
from app import engine

# first attempt function. No longer called anywhere but no reason to delete yet:
def search_last(last):
    sql_text = 'SELECT * FROM odyssey WHERE lastname_stripped LIKE "%' + last + '%";'
    df = pd.read_sql_query(sql_text, engine)
    return df


def sql_search(field_value, field_name):
    wrapped_field = '%' + field_value + '%'
    sql_text = \
        'SELECT * FROM odyssey WHERE %s LIKE :wrapped_field;' % (field_name)
    print 'wrapped_field = ', wrapped_field
    print sql_text
    df = pd.read_sql_query(sql_text, engine, params=[wrapped_field])
    return df


def search_all(first, last, case):
    if case:
        print 'Searching for case = ', case
        df = sql_search(case, '"Case Number"')
    elif last:
        print 'Searching for last = ', last
        df = sql_search(last, 'lastname_stripped')
    elif first:
        print 'Searching for first = ', first
        df = sql_search(first, 'firstname_stripped')
    if len(df) > 1:
        #print 'len(df) = ', len(df)
        if first:
            print 'Searching for first after initial search. First = ', first
            df = df.loc[df['firstname_stripped'].str.contains(first)]
    print 'Done with search'

    df.drop(['index',
             'lastname_stripped',
             'firstname_stripped',
             'last_name',
             'first_name'
             ], axis=1, inplace=True)

    return df


if __name__ == "__main__":

    last_name = 'AAGAARD'
    df_db_out = search_last(last_name)
    print
    print "FROM MAIN:"
    print df_db_out.to_html()
