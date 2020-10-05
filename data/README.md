The pickled data are daily return of gold future, silver future and copper future from US exchanges(with prefix s) and CN exchanges(with prefix c) respectively.  
Each pickle file contains a pandas.DataFrame with 3 columns: day, intraday and overnight(day = intraday + overnight).  
The return data was generated from market quotes, with labourious data cleaning. The data came from the most active contract at each day.  

数据来源于wind，分别是中国市场（前缀c）和美国市场（前缀s）的黄金期货、白银期货、铜期货每日收益数据。  
每个pickle文件是一个pandas.DataFrame，有3列：day, intraday和overnight，分别代表整日收益，交易时段收益和隔夜收益(day = intraday + overnight)。  
收益数据由每天最活跃合约（主力合约）编制而成。  
