# Learn Objectives
    # Creating, Reading and Writing
        - What is DataFrame? How to use it?
            - DataFrame is a table. It contains array entries. Each entry corresponde to a row and column. 
              You can use index for row labels
            - ex: pd.DataFrame({"Yes": [10, 20], "No": [29, 40]}, index=["P1", "P2"])

        - What is Series? How to use it?
            - Series is a sequence of data values. If DataFrame is a table, a Series is a list. 
              In essence is a column of a DataFrame
            - ex: pd.Series([1, 2, 3], index = ["P1", "P2"], name="Product")

        - How save file save to other csv?
            - a.to_csv("pp.csv")
    
    # Indexing, Selecting & Assigning
        - How to access get value of a column?
            ex: review["country][0]
        
        - What is indexing in Pandas?
            - It called loc(label base selection), iloc(index-base selection) one parameter it return row
                iloc(paramter1, parameter2) => iloc(row, column) ex: iloc(:3, 0)

            # index-base selection
                - ex: reviews.iloc[0] it get row one
                country           "Italy"
                description       "This is description"
                variety           "one two three"
                ...

                - ex: reviews.iloc[:, 0] it return column

            # label-base selection
                - review.loc[0, "country"] => "Italy"
                - loc[row, column]

                

