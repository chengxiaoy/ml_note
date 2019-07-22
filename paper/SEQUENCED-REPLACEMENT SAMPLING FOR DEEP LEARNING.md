### SEQUENCED-REPLACEMENT SAMPLING FOR DEEP LEARNING
-----------

this paper propose sequenced-replacement sampling for training deep neural networks

some view metioned in this paper:
1. although smaller mini-batch means a larger variance, the smaller mini-batch(above some threshold) actually outperform 
a larger one, the reason behinds this counter-intuitive phenomenon is that a relatively smaller mini-batch induces more 
stochasticity and hence exploration during the training process
2. non-replacement sampling has been shown to lead to faster convergence than replacement sampling
3. replacement sampling lead more accessible configurations of mini-batch and hence more exploration-induction during 
the training precess
4. the drawback of the replacement sampling is that there is no guarantee that all the samples in the dataset would been 
utilized with sufficient frequency even after a large number of training steps.

to tackle this drawback, sequenced-replacement sampling is proposed