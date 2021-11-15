import pandas as pd
import random
import datetime
    


def to_md(df, column_alignments = []):
    
    '''
    args: Pandas data frame
    
    returns: String, markdown fomratted table.
    
    '''
    
    column_map = {'l':':---',
                  'c':':---:',
                  'r':'---:'}

    
    if type(column_alignments) in (list,tuple,set):
        pass
    else:
        raise TypeError('Make sure column_alignments are eitehr a list or a tuple')
        
    if len(column_alignments) != df.shape[1]:
        return 'Number of alignments should be the same as number of columns'
            
        
        # alignment_string = '|'.join(':--' for _ in df.columns) + '|\n'
    
    else:
    
        alignment_string = '|'.join(':--' for _ in df.columns) + '|\n'
        columns_string = '|'.join(col for col in df.columns) + '|\n'
        markdown_string = columns_string + alignment_string 
        
        for _,row in df.iterrows():
            markdown_string += '|'.join(str(elem) for elem in row) + '|\n' 
        
        return markdown_string


if __name__ == '__main__':
    """
    Dummy dataframe to test out the function.
    
    """

    dates = [datetime.date.today() + datetime.timedelta(days= days)\
             for days in range(15)]
    dates_formatted = [date.strftime('%d-%B')[0:6] for date in dates]
    nums = [random.randint(1500-m,1600-m) for _,m in zip(dates_formatted,range(0,1500,100))]
    
    
    d = {'Date':dates_formatted,
         'Nums':nums,
         }
    
    dz = pd.DataFrame(data=d)
    
    test_func = to_md( dz, column_alignments = [] )
    
    print(test_func)


