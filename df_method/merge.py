import pandas as pd

if 0:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando"],
        "temperature": [21, 14, 35]
    })
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "orlando"],
        "humidity": [65, 68, 75]
    })
elif 0:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando", "baltimore"],
        "temperature": [21, 14, 35, 38]
    })
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "san diego"],
        "humidity": [65, 68, 71]
    })
elif 0:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando", "baltimore"],
        "temperature": [21, 14, 35, 38],
        "humidity": [65, 68, 71, 75]})
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "san diego"],
        "temperature": [21, 21, 35]
    })
elif 1:
    df1 = pd.DataFrame({
        'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']
    })
    df2 = pd.DataFrame({
        'name': ['Jake', 'Lisa', 'Sue', 'Bob'],
        'salary': [70000, 80000, 120000, 90000]
    })

if 0:
    df3 = pd.merge(df1, df2)
elif 0:
    df3 = pd.merge(df1, df2, on='city') # how='inner'
elif 0:
    #df3 = pd.merge(df1, df2, on='city', how='inner') # Only include observations found in both A and B
    df3 = pd.merge(df1, df2, on='city', how='outer') # Include observations found in either A or B
    #df3 = pd.merge(df1, df2, on='city', how='left') # Include all observations found in A
    #df3 = pd.merge(df1, df2, on='city', how='right') # Include all observations found in B
elif 0:
    # indicator=True: 데이타가 양 쪽에서 왔는지, 왼쪽에서만 왔는지, 아니면 오른쪽에서만 왔는지 표시 
    #df3 = pd.merge(df1, df2, on='city', how='inner', indicator=True) 
    df3 = pd.merge(df1, df2, on='city', how='outer', indicator=True) 
    #df3 = pd.merge(df1, df2, on='city', how='left', indicator=True) 
    #df3 = pd.merge(df1, df2, on='city', how='right', indicator=True) 
elif 0:
    # Because the output would have two conflicting column names, 
    # the merge function automatically appends a suffix _x or _y to make the output columns unique. 
    # If these defaults are inappropriate, 
    # it is possible to specify a custom suffix using the suffixes keyword:
    #df3 = pd.merge(df1, df2, on='city', how='inner', suffixes=['_left','_right']) 
    df3 = pd.merge(df1, df2, on='city', how='outer', suffixes=['_left','_right']) 
    #df3 = pd.merge(df1, df2, on='city', how='left', suffixes=['_left','_right']) 
    #df3 = pd.merge(df1, df2, on='city', how='right', suffixes=['_left','_right']) 
elif 0:
    df3 = pd.merge(df1, df2, left_on='employee', right_on='name').drop('name', axis=1)
elif 1:
    # 인덱스를 이용 데이타를 통합할 때 join method를 사용하면 편한데, 
    # 굳이 pd.merge를 이용하여 작업을 하겠다면 할 수는 있다. 
    # left_index=True라고 하면 왼쪽에서 index를 사용하겠다는 것이고, 
    # right_index=True라고 하면 오른쪽에서 index를 사용하겠다는 것이다.
    df3 = pd.merge(df1, df2, left_index=True, right_index=True)

def main():
    print(f"{df1 = }")
    print(f"{df2 = }")
    print(f"{df3 = }")

if __name__ == "__main__":
    main()