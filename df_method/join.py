import pandas as pd

if 0:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando"],
        "temperature": [21, 14, 35]
    }).set_index('city')
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "orlando"],
        "humidity": [65, 68, 75]
    }).set_index('city')
elif 0:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando", "baltimore"],
        "temperature": [21, 14, 35, 38]
    }).set_index('city')
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "san diego"],
        "humidity": [65, 68, 71]
    }).set_index('city')
elif 1:
    df1 = pd.DataFrame({
        "city": ["new york", "chicago", "orlando", "baltimore"],
        "temperature": [21, 14, 35, 38],
        "humidity": [65, 68, 71, 75]}).set_index('city')
    df2 = pd.DataFrame({
        "city": ["chicago", "new york", "san diego"],
        "temperature": [21, 21, 35]
    }).set_index('city')
elif 1:
    df1 = pd.DataFrame({
        'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']
    }).set_index('employee')
    df2 = pd.DataFrame({
        'name': ['Jake', 'Lisa', 'Sue', 'Bob'],
        'salary': [70000, 80000, 120000, 90000]
    }).set_index('name')

if 0:
    df3 = df1.join(df2)
elif 0:
    #df3 = df1.join(df2, how='inner')
    df3 = df1.join(df2, how='outer')
    #df3 = df1.join(df2, how='left') # default
    #df3 = df1.join(df2, how='right')
elif 1:
    #df3 = df1.join(df2, how='inner')
    df3 = df1.join(df2, how='outer',  lsuffix='_left', rsuffix='_right')
    #df3 = df1.join(df2, how='left') # default
    #df3 = df1.join(df2, how='right')

def main():
    print(f"{df1 = }")
    print(f"{df2 = }")
    print(f"{df3 = }")

if __name__ == "__main__":
    main()