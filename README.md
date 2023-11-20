# detect-abusive-comment

This academic work explores the problem of detecting toxic comments in Bengali social media text, which is unstructured and inflectional. Manual filtering is hard and inefficient, so we use deep learning models that can extract features automatically. We compare them with statistical models that need feature engineering and show that deep learning models perform better, as in English text analysis.

We study the problem of detecting toxic comments in Bengali social media text, which is unstructured and has misspelled vulgar words. We use machine learning models that can classify such comments automatically. We compare four supervised models with our [BanglaBERT](https://github.com/csebuetnlp/banglabert) and LSTM models, which is better than statistical models for Bengali text.

# Dataset
We have merged three datasets to create a new dataset. The datasets are:
* [BD-SHS](http://arxiv.org/abs/2206.00372)
* [Bangla-Abusive-Comment-Dataset](https://github.com/aimansnigdha/Bangla-Abusive-Comment-Dataset)
* [Multi_labeled_toxic_comments](https://github.com/deepu099cse/Multi-Labeled-Bengali-Toxic-Comments-Classification)

The merged dataset is available in the [*data*](https://github.com/abirmondal/detect-abusive-comment/blob/main/data) folder. The latest merge is present in the folder *m_dataset_21_9*.

# Preprocessing

We have used the following preprocessing steps:
* Remove comments with stars ```*```, i.e. comments that are censored
* Remove special words, such as HTML tags
* Remove Links and Emojis using [normalizer](https://github.com/csebuetnlp/normalizer)
* Remove single letter words
* Translate English words to Bengali using Google Translator with the help of the library [translators](https://pypi.org/project/translators/)
* Strip Comments to remove extra space

# Dataset Division

We have divided the dataset into three parts:
| Train Set | Test Set | Validation Set |
| :-: | :-: | :-: |
| 63241 (70%) | 18069 (20%) | 9035 (10%) |

We have used sklearn's ```train_test_split``` function to divide the dataset.

# Models
We have used four statistical models and one deep learning model.

The statistical models are:
* [Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
* [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* [Support Vector Machine](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

The deep learning model is made using [BanglaBERT](https://github.com/csebuetnlp/banglabert) and LSTM.

# Results

| Model | Accuracy | Weighted Average Precision | Weighted Average Recall | Weighted Average F1-Score |
| --- | :-: | :-: | :-: | :-: |
| BanglaBERT + LSTM | 76.89 | 76.76 | 71.07 | 73.81 |
| Random Forest | 77.65 | 75.16 | 70.66 | 72.84 |
| Support Vector Machine | 72.47 | 73.39 | 55.03 | 62.89 |
| Logistic Regression | 72.37 | 72.20 | 56.67 | 63.50 |
| Naive Bayes | 71.64 | 74.87 | 49.88 | 59.87 |

We have achieved almost the best accuracy using **BanglaBERT + LSTM** model. As we wanted to focus on detecting abusive comments, we have focused on the *recall* and *f1-score* which is better than the other models.

# Testing

* To test BanglaBERT + LSTM model on the *testing set* execute all the cells of the notebook [*banglabert_test_17_11_abir_.ipynb*](https://github.com/abirmondal/detect-abusive-comment/blob/e46dcd6c4bac364ea340f84ab8cff9d1f7880529/test/banglabert_test_17_11_abir_.ipynb) in the [*test*](https://github.com/abirmondal/detect-abusive-comment/blob/6fa8e139f8867cb9717b5113bf4c53127e732cc1/test) folder.
* To test the baseline models on the *testing set* execute all the cells of the notebook [*loaded_baselines__19_11_kingshuk.ipynb*](https://github.com/abirmondal/detect-abusive-comment/blob/6fa8e139f8867cb9717b5113bf4c53127e732cc1/test/loaded_baselines__19_11_kingshuk.ipynb) in the [*test*](https://github.com/abirmondal/detect-abusive-comment/blob/6fa8e139f8867cb9717b5113bf4c53127e732cc1/test) folder.

> Note: The models are already trained and saved in the [*models*](https://github.com/abirmondal/detect-abusive-comment/blob/9b95e5b7b5cb38424ee00b2b843bcc2d9cd82f4d/src/models) folder. You can also run the notebooks in [Google Colab](https://colab.research.google.com/).