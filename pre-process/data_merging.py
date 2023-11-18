import pandas as pd
 # CREATING DATAFRAMES FROM THE DATASETS
df1 = pd.read_excel(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\originals\Bangla-Abusive-Comment-Dataset-master\Bangla-Abusive-Comment-Dataset-master\train_data.xlsx')
df2 = pd.read_csv(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\originals\Bangla-Abusive-Comment-Dataset-master\Kingshuk\BD SHS\test.csv')
df3 = pd.read_csv(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\originals\Bangla-Abusive-Comment-Dataset-master\Kingshuk\BD SHS\train.csv')
df4 = pd.read_csv(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\originals\Bangla-Abusive-Comment-Dataset-master\Kingshuk\BD SHS\val.csv')
df5 = pd.read_csv(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\originals\archive\Bengali hate speech .csv')


## WORKING WITH DF1
df1['target'] = df1['toxic'] | df1['threat'] | df1['obscene'] | df1['insult'] | df1['racism']
# REMOVING THE UNWANTED COLUMNS FROM DF1
columns_to_remove_df1 = ['id', 'toxic', 'threat', 'obscene', 'insult', 'racism', 'Unnamed: 7']
df1 = df1.drop(columns=columns_to_remove_df1)
# RENAMING COMMENT_TEXT COLUMN TO TEXT
df1 = df1.rename(columns={'comment_text': 'text'})

# WORKING WITH DF2
columns_to_remove_df2 = ['target', 'type']
df2 = df2.drop(columns=columns_to_remove_df2)
df2 = df2.rename(columns={'hate speech':'target', 'sentence': 'text'})


# WORKING WITH DF3
columns_to_remove_df3 = ['target', 'type']
df3 = df3.drop(columns=columns_to_remove_df3)
df3 = df3.rename(columns={'hate speech':'target', 'sentence': 'text'})
# print(df3)

# WORKING WITH DF4
columns_to_remove_df4 = ['target', 'type']
df4 = df4.drop(columns=columns_to_remove_df4)
df4 = df4.rename(columns={'sentence': 'text', 'hate speech': 'target'})
# print(df4)

# WORKING WITH DF5
columns_to_remove_df5 = ['category']
df5 = df5.drop(columns=columns_to_remove_df5)
df5 = df5.rename(columns={'sentence':'text', 'hate':'target'})
# print(df5)

# MERGING ALL THE DATAFRAMES INTO ONE DATAFRAME
merged_df = pd.concat([df1, df2, df3, df4, df5], axis=0)
# merged_df = pd.merge(merged_df, df3, on='text')
# merged_df = pd.merge(merged_df, df4, on='text', suffixes=('_left', '_right'))
# merged_df = pd.merge(merged_df, df5, on='text')

# print(merged_df)

#CONVERTING THE FINAL DATAFRAME INTO CSV FILE
merged_df.to_csv(r'C:\Users\arnab\Coding_Stuff\python\TwitterBanglaDatabase\dataset\Current_Merge.csv', index=False)

# print("\nData Frame 1:", df1)
# print("\nData Frame 2:", df2)
# print("\nData Frame 3:", df3)
# print("\nData Frame 4:", df4)
# print("\nMerged Dataframe:", merged_df)
print(merged_df['text'].value_counts())
print(merged_df['target'].value_counts())
# print(merged_df['text'].map(len).max())
# print(merged_df['text'].map(len).min())


