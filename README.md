# Student Summaries Analysis with MongoDB

## Overview

This project focuses on using MongoDB to analyze a dataset of student summaries. The dataset comprises approximately 24,000 summaries written by students in grades 3-12, covering various topics and genres. The goal of this project is to predict content and wording scores for these summaries on previously unseen topics.

## Dataset

The dataset consists of several CSV files:

- `summaries_train.csv`: Contains student summaries with fields such as student_id, prompt_id, text, content score, and wording score.
- `summaries_test.csv`: Similar to `summaries_train.csv`, but without content and wording scores for the test set.
- `prompts_train.csv`: Includes the prompts given to students, with fields like prompt_id, prompt_question, prompt_title, and prompt_text.
- `prompts_test.csv`: Contains test set prompts with the same structure as `prompts_train.csv`.
- `sample_submission.csv`: A sample submission file to help with the correct format for predictions.

## Goals

The primary objectives of this project are as follows:

1. **Data Cleaning**: Clean the dataset, such as removing the null, correcting punctuation, special character, etc.
2. **Data Exploration**: Explore the dataset to gain insights into student summaries and prompts.
3. **Content and Wording Score Analysis**: Use MongoDB to analyse content and wording scores for student summaries.
4. **Prompt Analysis**: Understand the impact of different prompts on student performance.


## Sub-tasks 
`Executed`

**Data Cleaning:**

1. Remove rows with missing values in the dataset to ensure data completeness.
2. Correct punctuation and special characters in the text of student summaries.
3. Standardize the format of dates or other structured data if present in the dataset.

**Data Exploration:**

4. Calculate and visualize summary statistics for content and wording scores to understand their distribution.
5. Create a word cloud based on the text of student summaries to identify common keywords.
6. Generate descriptive statistics for student summary lengths to understand the range and distribution.

**Content and Wording Score Analysis:**

7. Use MongoDB's aggregation framework to group summaries by content scores and calculate average wording scores within each group.
8. Identify summaries with the highest content and wording scores to showcase exemplary student work.
9. Compute correlations or perform regression analysis between content and wording scores to explore their relationship.

**Prompt Analysis:**

`In Progress`

10. Determine the most frequently used prompts by counting occurrences and analyzing their impact on the distribution of content and wording scores.

## Advanced Querying Techniques 


Utilising  MongoDB's advanced querying techniques for your student summaries dataset, consider the following objectives:

1. **Text Search**: Implement full-text search to find summaries containing specific keywords or phrases, helping you identify common themes or topics.

2. **Geospatial Queries**: If applicable (e.g., if summaries are related to specific locations), perform geospatial queries to identify summaries written in particular regions or areas.

3. **Regular Expressions**: Use regular expressions to extract and analyze specific patterns within the summary text, such as identifying references to dates or important terms.

4. **Aggregation Pipeline**: Create a complex aggregation pipeline to calculate summary statistics, such as the average content and wording scores for different age groups or grades.

5. **Sorting and Pagination**: Implement sorting and pagination to retrieve summaries based on their content or wording scores, allowing you to focus on high-scoring or low-scoring summaries.

6. **Date Ranges**: Query summaries based on date ranges to analyze how student performance has changed over time or in different academic terms.

7. **Array Manipulation**: Utilize MongoDB's array manipulation operators to work with arrays of data within your documents, such as extracting a list of keywords from each summary.

8. **Text Indexing**: Create text indexes on summary text fields to improve text search performance and allow for more advanced querying capabilities.

9. **Graph Queries**: If your data has relationships between documents (e.g., students and their summaries), use graph queries to explore connections and dependencies within the dataset.

10. **Faceted Search**: Implement faceted search to allow users to filter and explore summaries based on multiple criteria, providing a user-friendly interface for exploring the dataset.
