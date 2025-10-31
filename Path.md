## Questions to Ask to Understand the Data

1. **What’s the size of the data?**  
   → Use: `df.shape`

2. **How does the data look?**  
   → Use: `df.sample(n)` or `df.head()`

3. **What are the datatypes of the columns?**  
   → Use: `df.info()`

4. **Are there any missing values?**  
   → Use: `df.isnull().sum()`

5. **How does the data look mathematically?**  
   → Use: `df.describe()`

6. **Are there any duplicated values?**  
   → Use: `df.duplicated().sum()`

7. **What’s the correlation between columns?**  
   → Use: `df.corr()`
