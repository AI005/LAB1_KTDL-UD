from pandakungfu import Pandakungfu as pdf
import sys


if __name__ =="__main__":
    argv = sys.argv
    args = len(argv)
    print(sys.argv)
    
    try:
        filename = argv[1]
        df = pdf(filename)
    except:
        print("Error filename input")
    

    if args == 3:
        method = argv[2]
        if method == "--method=list-missing-col":
            print(df.get_list_col_less_data())
        elif method == "--method=get-number-missing-row":
            print('number of missing-row:',  df.get_number_of_row_less_data())
        elif method == "--method=remove-duplicate":
            df.remove_duplicate_row()
        else:
            print("no option" + method)
    elif args == 4:
    
        method = argv[2]
        option = argv[3]
        if method == "--method=remove-row-missing":
            df.remove_row_by_percent_missing(percent=float(option))
            print(df)
        elif method == "--method=remove-col-missing":
            df.remove_col_by_percent_missing(percent=float(option))
            print(df)
        else:
            print("no option" + method)
    elif args == 5:
        method = argv[2]
        option1, option2 = argv[3], argv[4]
        if method=="-method=fill-missing-value":
            if option1=="--mean":
                if option2 == "all":
                    pass
                else:
                    df.set_col_with_mean(option2)
            elif option1=="--median":
                if option2 == "all":
                    pass
                else:
                    df.set_col_with_median(option2)
            elif option1=="--mode":
                if option2 == "all":
                    pass
                else:
                    df.set_col_with_mode(option2)
            
        else:
            print("no option" + method)
    else:
        pass
    
    