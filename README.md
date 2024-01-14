# uProc-ObjectDet by Gherman Ovidiu
- To run this project: (If you don't have a camera connected you will not be able to turn on LIVE Detection)
  * Run init/init.bat
  * Open CMD in the dataSetHandler directory
  * Run the following command: python.exe dataSetImage_downloader.py --download_folder testPictures listOfImages
  * Wait for pictures to be downloaded
  * Now go in the parent directory and run the following command: python.exe main.py
- How to use the scripts (for the data set downloader):
  * First you have to run dataSetHandler/imageList_creator.py (modify tempIDs depending on what pictures section you want on Open Image DataSet v7)
  * Then run dataSetHandler/dataSetImage_downloader.py (args: --download_folder destination listOfImages)
  * Then run dataSetHandler/dataSet_creator.py (this will download copy the images and from OData the labes for the network) 
