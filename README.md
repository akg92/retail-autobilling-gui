# UI Developement git
The neural network implementation can be found in https://github.com/akg92/retail-product-auto-billing repo.


## How to Test

### Approach 1
* The model is trained on the checkout data set.
* This can be considered as a backup approach. 
* Requires the annotated checkout dataset for training. 
* Due to above reason this way of modeling is not an realistic one. But tried to avoid the risk of total failure.
##### How to run??
python gui_retail.py multi

### Approach 2: An realistic approach to retail billing.
* Generated checkout data from individual product for training.
* The realistic approach. 
* As of now, the C-GAN is not used to reduce the gap between the actual dataset and generated.
#### How to run??
python gui_retail.py multi


## Demo data.
Some of sample data is included in the image folder of this repo. For more data please download from following link https://drive.google.com/open?id=1dTemCJvQ6-smURj69cs46Zo3QER4_22X . Total 6000 images are added in this zip.


