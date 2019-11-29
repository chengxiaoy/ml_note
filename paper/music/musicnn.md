### A Comparison of Music Input Domains for Self-Supervised Feature Learning

a direct comparision of input representations better suited for feature learning   
compare the symbolic and audio domains
![image](https://user-images.githubusercontent.com/19379550/69517076-9b177580-0f8e-11ea-9ccd-a72b871ea3b5.png)

the highlight of this paper is:
- use self-supervised learning, the neighboring clips are similar, siamese network
- use MIDI files to obtain a symbolic representation as well as to synthesize audio using fluidsynth


### TRANSFER LEARNING FOR MUSIC CLASSIFICATION AND REGRESSION TASKS

music tagging as a source task because large training data is availabel and rich label set 
covers various aspects of music, e.g., genre, mood, era, and instrumentations.

![image](https://user-images.githubusercontent.com/19379550/69526097-63b3c380-0fa4-11ea-8669-144ca0390368.png)

A common motivation for transfer learning is the lack of sufficient training data in the target task, 
When using a neural network, by transferring pre- trained weights, the number of trainable parameters in the 
target-task model can be significantly reduced, enabling effective learning with a smaller dataset.


the presentation transfer features are applied to the target task, as below:
![image](https://user-images.githubusercontent.com/19379550/69527712-d2dee700-0fa7-11ea-9067-9b4b5c74ee84.png)


### MAIN MELODY EXTRACTION WITH SOURCE-FILTER NMF AND CRNN

the model consists of three parts
- SF-NMF to get HF0
- HF0 as the input to the crnn 
- classification

![image](https://user-images.githubusercontent.com/19379550/69858933-0bdfca00-12ce-11ea-91e0-85ceaac3e768.png)

the dataset is MedleyDB
the github code is https://github.com/dogacbasaran/ismir2018_dominant_melody_estimation    



