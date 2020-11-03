from pandakungfu import Pandakungfu as pdf
import sys

if __name__ == "__main__":
    argv = sys.argv
    args = len(argv)
    print(argv)
    
    try:
        filename = argv[1]
        df = pdf(filename)
    except:
        print("Error filename input")
    
    method = argv[2]
    if args == 3:
        # Chuc nang 1: Liet ke cac cot bi thieu du lieu
        if method == "-method=list-missing-col":
            print(df.get_list_col_less_data())
            
        # Chuc nang 2: Dem so dong bi thieu du lieu
        elif method == "-method=get-number-missing-row":
            print('number of missing-row:',  df.get_number_of_row_less_data())
        
        else:
            print("no option" + method)
    elif args == 4:
        filename_out = argv[3]
        
        # Chuc nang 6: Xoa cac mau bi trung lap
        if method == "-method=remove-duplicate":
            df.remove_duplicate_row()
            df.write_csv(filename_out)
        
    elif args == 5:
        option = argv[3]
        filename_out = argv[4]
        
        # Chuc nang 4: Xoa cac dong bi thieu du lieu voi nguong ti le cho truoc
        if method == "-method=remove-row-missing":
            df.remove_row_by_percent_missing(percent=float(option))
            df.write_csv(filename_out )
            
        # Chuc nang 5: Xoa cac cot bi thieu du lieu voi nguong ti le cho truoc
        elif method == "-method=remove-col-missing":
            df.remove_col_by_percent_missing(percent=float(option))
            df.write_csv(filename_out )
        
        # Chuc nang 7: Chuan hoa mot thuoc tinh bang phuong phap Z-core
        elif method == "-method=normalize-z-score":
            df.normalize_by_zcore(option)
            df.write_csv(filename_out )
        else:
            print("no option" + method)
    
    elif args == 6:
        option1, option2 = argv[3], argv[4]
        filename_out = argv[5]
        
        #Chuc nang 3
        if method=="-method=fill-missing-value":
            #ex: python3 main.py test.csv -method=fill-missing-value --mean $all
            func = option1[2:] #ex: --mean => mean
            if option2 == "@all":
                df.fill_all_missing(func)
            else:
                df.fill_missing_value_of_col(option2, func)

            df.write_csv(filename_out)
            
        # Chuc nang 8
        elif method=='-method=calcu-express':
            df.calculate_express(option1, option2)
            
            df.write_csv(filename_out)
            
        else:
            print("no option" + method)
    elif args == 7:
        option1, option2, option3 = argv[3:-1]
        filename_out = argv[-1]
        # Chuc nang 7: Chuan hoa mot thuoc tinh numeric bang phuong phap min-max
        
        if method=="-method=normalize-min-max":
            df.normalize_by_minmax(option3, float(option1), float(option2))
        else:
            print("no option " + method)  
    else:
        pass
#$ python3 main.py house-prices.csv -method=calcu-express ('OverallQual'-'OverallCond')/'OverallQual' newcol new_house-prices.csv
    print(df)
