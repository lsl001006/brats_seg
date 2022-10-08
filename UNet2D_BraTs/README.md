# UNet2D_BraTs
To get started, you could using the command below:

- for training:
`python train.py --arch="Unet" --dataset=“AnyName”`
- for testing:
  - generate test images to output/GT and output/Pred
`python test.py --name="AnyName_Unet_woDS" --mode="GetPicture"`
  - evaluate:
  `python test.py --name="AnyName_Unet_woDS" --mode="Calculate"`  
- to compare the GT with the segmentation result one by one:
   - first, make sure you have finished training and testing procedure above
   - second, modify the paths in `concateImage.py` and run `python concateImage.py`