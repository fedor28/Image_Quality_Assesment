# Image Quality Assesment

This repo contains implementation of image quality assesment (IQA) model. It's a part of pipeline of self-checkout model.

To make IQA regressor firstly I have generated the dataset by the next way: I take initial images from production and apply to them different distortions (gaussian, horizontal, vertical blur). The more information in [database_description.md](https://github.com/fedor28/Image_Quality_Assesment/blob/main/regression_task/database%20description.md)

I mapped label for each image linearly to the degree of distortion.

Then I used BRISQUE algorithm for extracting necessary statistics from image and based on this features I trained regressors.

For evauating model quality I used images from another production.

Results of models in the table:
|         | SVR   | Bagging of  decision trees | |  Random Forest | 
| ------- | ----------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------- |
| MAPE    | 113   | 17                         | |  20            | 
| MSE     | 753   | 78                         | |  107           |

### Working with repo

1.	Clone this repo
2.	Download [train data](https://drive.google.com/drive/folders/170FK3Ji1fy0TvJZreAKzGL0Y91fjUxa7?usp=sharing), [test data]() and put in local repo with appropriate relative paths 

	Path to train images "/regression_task/data"

	Path to test images "/data/test_images"
3. Everything is ready for your experiments. Run train_reg.ipynb, train models and see the results.	
Path to train data "/regression_task/data"
Path to initial images "/data/initial_images"
Path to test images "/data/test_images"


If you want to make self-made train dataset, you can download the initial images here

and add your changes in creating_database.ipynb

### Data


If you want to make self-made train dataset, you can download the initial images here

and run creating_database.ipynb

** link