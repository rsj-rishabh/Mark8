VOLCANOES ON VENUS

Description: This dataset contains images collected by the Magellan expedition to Venus. Venus is the most similar planet to the Earth in size, and therefore researchers want to learn about its geology. Venus' surface is scattered with volcanos, and the aim of this dataset was to develop a program that can automatically identify volcanoes (from training data that have been labeled by human experts between 1-with 98% probability a volcano- and 4-with 50% probability). A tool called JARtool was developed to do this. The makers of this tool made the data publicly available to allow more research and establish a benchmark in this field. They provide in total 134 images of 1024*1024 8-bit pixels (out of the 30000 images of the original project). The dataset you will use is a preprocessed version of these images: possibly interesting 15*15 pixel frames ('chips') were taken from the images by the image recognition program of JARtool, and each was labeled between 0 (not labeled by the human experts, so definitely not a volcano), 1 (98% certain a volcano) and 4 (50% certainty according to the human experts). More information can be found in the data documentation.

Size: The image chips are spread over groups, according to experiments carried out for the JARtool software. The training and test sets for experiments C1 and D4 together cover all chips (see the experiments table):

Records: 37280 image chips, divided as follows: C1_trn: 12018 / C1_tst: 16608 / D4_trn: 6398 / D4_tst: 2256

Features: 15 * 15 pixels
8.4 MB

References:
These data were used for the development of JARtool, a software system that learns to recognize volcanoes in images from Venus. The technical details about this tool are described in the paper Learning to Recognize Volcanoes on Venus (1998) by M. C. Burl, L. Asker, P. Smyth, U. Fayyad, P. Perona, L. Crumpler and J. Aubele. This paper should give you a good example of how data mining can be performed on this dataset (you can ignore the part about Focus of Attention, because that has already been done for you).

Task: Perform Exploratory data analysis. Prepare the data for data mining. Feature space reduction will be necessary, because the number of features is very high compared to the number of positive volcano examples. Then build at least two classifiers to detect volcanoes: implement the basic classifier from Burl et Al.'s paper, and at least one other. You can follow Burl et Al.'s paper, where classes 1 up to 4 are considered positive examples. As an extra, you can try to perform clustering to find the different types of volcanoes as mentioned in Burl et Al.'s paper.

Challenges: It will be necessary to normalise the pixel frames, as there is a difference in brightness between the different images and even between different parts of the same image. Also, feature extraction will be necessary, because there are quite a lot of pixels per frame. This is especially a problem because the dataset is highly unbalanced: the number of positive examples is very low. Finally, there is the fact that the volcanos are of different kinds, and it is difficult to build one classifier for all of them together.

Site: http://www.inf.ed.ac.uk/teaching/courses/dme/html/datasets0405.html
