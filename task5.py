"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbsol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

 
def find_by_symbol(input_sym):
    dict = {}

    with open('task5.csv') as f:
        for line in f:
            symbol, stock = line.split(',',1)
            stl_list = []
            if (symbol != 'Symbol'):
                if (symbol in dict):
                    curr_list = dict[symbol]
                    curr_list.append(stock.strip())
                else: 
                    stl_list.append(stock.strip())
                    dict[symbol] = stl_list
    #print(dict)
    
    if input_sym not in dict:
        print ("No matches")
    else :
        if len(dict[input_sym]) > 1:
            print ( "There are " + str(len(dict[input_sym])) + " stocks with that symbol")   
        else: 
            print (str(dict[input_sym][0]))
 
if __name__=="__main__":
    
    while True:
        stock_sym = str(input("Enter stock symbol: "))
        find_by_symbol(stock_sym)