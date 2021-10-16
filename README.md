# Image Quality Assesment

This repo contains implementation of image quality assesment (IQA) model. It's a part of pipeline of self-checkout model (Model that get the video stream from supermarket checkout as input, and gives receipt for )

To make IQA regressor firstly I have generated the dataset by the next way: I take initial images from production and apply to them different distortions (gaussian, horizontal, vertical blur). The more information in [database_description.md](https://github.com/fedor28/Image_Quality_Assesment/blob/main/regression_task/database%20description.md)

I mapped label for each image linearly to the degree of distortion.

Then I used [BRISQUE](https://github.com/fedor28/Image_Quality_Assesment/blob/main/BRISQUE%20theory/am_asilomar_2011.pdf) algorithm for extracting necessary statistics from image and based on this features I trained regressors.

For evaluating model quality I used images from another production.

Metrics of models on test set:

|         | SVR   | Bagging of  decision trees | Random Forest |  Gradient Boosting | 
| ------- | ----------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------- |
| MAPE    | 113   | 17                         | 20            |   47               | 
| MSE     | 753   | 78                         | 107           |   287              |

Also I analyzed predictions on test set of best estimator (Bagging of decision trees). 
Nothing in common of outliers have been detected.

### Usage

1.	Clone this repo
2.	Download [train data](https://drive.google.com/drive/folders/170FK3Ji1fy0TvJZreAKzGL0Y91fjUxa7?usp=sharing), [test data]() and put in local repo with appropriate relative paths 

	Path to train images "/regression_task/data"

	Path to test images "/data/test_images"
3. Everything is ready for your experiments. Run [train_reg.ipynb](https://colab.research.google.com/drive/1uv_JGRfxSgXrA6wVf4NKszkhTbK5tw3O) to train models and see the results.	


You can use [creating_database.ipynb](https://github.com/fedor28/Image_Quality_Assesment/blob/main/regression_task/creating_database.ipynb) for creating your self-made dataset.

For example if you want apply other distortions, you can download the initial images here, add your changes in creating_database.ipynb and run it.
