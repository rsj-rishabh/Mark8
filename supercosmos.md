THE SUPERCOSMOS SKY SURVEY OBJECTS CATALOGUE
Description: The SuperCOSMOS Sky Survey programme is carried out at the University of Edinburgh.
             The project used the SuperCOSMOS machine, a high-precision plate scanning facility, to scan in the Schmidt photographic atlas material. 
             This has produced a digitised survey of the entire sky in three colours (B, R and I), with one colour (R) at two epochs. 
             From these digital images, objects have been extracted, and an objects catalogue has been composed. 
             For each object, useful astronomical characteristics have been registered, such as the size, the brightness, the position, etc. 
             A project was then caried out to classify the objects as stars or galaxies. 
             External labeling to evaluate the classification algorithm was obtained from the more precise data of the Sloan Digital Sky Survey.

Size:
There are 4 object sets, one for B and I, and two for R (one set from pictures taken in the 50's and one set more recent). 
Each of these is divided in a set of paired objects (for which a corresponding SDSS object was found) and a set of unpaired ones:
B-paired: 34663 / B-unpaired: 68987
R-paired (recent): 26791 / R-unpaired: 54920
I-paired: 15645 / I-unpaired: 41596
R-paired (50's): 15834 / R-unpaired: 34426
Paired datasets have 40 attributes (including some from SDSS), unpaired 34.
The size of the datasets is as follows:
B-paired: 16.4MB / B-unpaired: 23.5MB
R-paired (recent): 12.6MB / R-unpaired: 18.7MB
I-paired: 14MB / I-unpaired: 7.3MB
R-paired (50's): 7.4MB / R-unpaired: 11.7MB

References:
The SuperCOSMOS Sky Survey. Paper I: 
        Introduction and description (2001) by N. Hambly, H. MacGillivray, M. Read, S. Tritton, E. Thomson, D. Kelly, D. Morgan, R. Smith, S. Driver, J. Williamson, Q. Parker, M. Hawkins, P. Williams and A. Lawrence: 
        This paper is an introduction to the SSS project.
The SuperCOSMOS Sky Survey. Paper II: Image detection, parameterisation, classification and photometry (2001) by N. Hambly, M. Irwin and H. MacGillivray: 
        A description of the methods for image detection, parameterisation, classification and photometry. 
        A useful paper for you to read, as it gives explanations about how the data were obtained and what they mean, and about the object classification efforts by the SSS people.
The SuperCOSMOS Sky Survey. Paper III: Astrometry (2001) by N. Hambly, A. Davenhall, M. Irwin and H. MacGillivray: 
        An overview of how the astrometric parameters of the data were derived. Probably less interesting for you.
Automated Star/Galaxy Classification for Digitized POSS-II (1995) by N. Weir, U. M. Fayyad and S. Djorgovski: 
        This paper uses a similar astronomical dataset. It is quite interesting, as it is much more understandable than paper II above. 
        It uses a similar two-step classification method and should therefore give you some insight in what is happening in paper II.

Task: First read the information in the README file, and in paper II (and the paper by Weir) referenced above. 
      Then perform exploratory data analysis and prepare the data for data mining. You can concentrate on one of the paired datasets. 
      Classify sky objects as stars or galaxies (use the SDSS classification as label). 
      Compare at least two different classification algorithms. 
      Try the effect of excluding/including fields 19 and 31, the classification efforts of the SSS team. 
      Also, do a performance evaluation with respect to the magnitude as was done in paper II.

Challenges: These are astronomical data, and all the documentation is written in 'astronomical language', so it is quite difficult to understand what the data are all about and how the previous research has been caried out. 
            Furthermore, the dataset is quite big, so case reduction might be necessary.
