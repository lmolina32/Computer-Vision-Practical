# Task 1
- Items brought to class: scissors, headphones, and umbrella 
- Question: All the items brought to class where correctly classified, I had the hardest time detecting the umbrella. 
## Confusion Matrix For training 
![img](/practical4/imgs/confusion_matrix_task1_training.png)
## Confusion Matrix For validation  
![img](/practical4/imgs/confusion_matrix_task1_validation.png)
## Accuracies 
![img](/practical4/imgs/task1_accuracies.png)
## Notes
The Linear SVM correctly classified all features in the traning, but was misclassifying scissors with headphones in the validation dataset. 

# Task 2 
The classes choosen are: 
```python
my_object_list = ['umbrella','headphone','scissors', "Leopards", "Motorbikes", "airplanes", "bonsai", "crayfish",  "dollar_bill", "kangaroo"]
```
## Confusion Matrix For training 
![img](/practical4/imgs/confusion_matrix_task2_training.png)
## Confusion Matrix For validation  
![img](/practical4/imgs/confusion_matrix_task2_valdiation.png)
## accuracies 
![img](/practical4/imgs/task2_accuracies.png)
## Notes:
For fc2 and linear kernel on the 10 classes my results were 100% for both the testing and the training data. I think this is a sign of overfitting of our model. This was supported by presenting my items to the camera. The model couldn't accurately detect the umbrella object and kept misclassifying the object as an ariplane or bonsai. 

# Task 3 

## Linear + fc1 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc1_linear.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc1_linear.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc1_linear.png)
## RBF + fc1 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc1_rbf.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc1_rbf.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc1_rbf.png)

## Poly + fc1 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc1_poly.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc1_poly.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc1_poly.png)


## Linear + fc2 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc2_linear.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc2_linear.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc2_linear.png)

## RBF + fc2 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc2_rbf.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc2_rbf.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc2_rbf.png)


## Poly + fc2 
### Confusion matrix for training
![img](/practical4/imgs/confusion_matrix_task3_training_fc2_poly.png)
### Confusion matrix for validatiaon 
![img](/practical4/imgs/confusion_matrix_task3_validation_fc2_poly.png)
### Accuracies 
![img](/practical4/imgs/task3_accuracies_fc2_poly.png)

## Notes
- The models with 100% accuracy in training and testing where Linear + fc2 and RBF + fc2. Like I said in task2 these two models likely overfitted the data, but if we are going based on accuracy these two models would be the ones we selected. The next runner ups are both at 99.7817% and both misclassified headphones, but they missclassified them as different things, the two models are linear + fc1 and rbf + fc1. The next highest accuracy is at 97.8166% which misclassified 6 out of the 10 classes all above 80%. The model is Poly + fc2. The last model had an accuracy of 95.1965% which was poly + fc1. Thus based on my reasoning of overfitting but picking the highest accuracy to have robustness when generalizing to unseen data, linear/RBF + FC1 will be the best models. This is because they represent the best bias/variance trade off, with high accuracy without the 100% perfection found in fc2-based models that likely overfit to VGG's own learned feature compression. 