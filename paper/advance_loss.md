### center loss(A Discriminative Feature Learning Approach for Deep Face Recognition)

this paper proposed center loss, the center loss simultaneously learns a center for deep features of each class and 
penalizes the distances between the deep features and their corresponding class centers. the softmax loss forces the 
deep features of different classes staying apart. The center loss efficiently pulls the deep features of the same class to their centers


the center loss formulation:

![center_loss](https://user-images.githubusercontent.com/19379550/61193263-f6864c80-a6ec-11e9-9a09-7ba6f820030a.jpg)

The c<sub>yi</sub> ∈ R<sup>d</sup> denotes the <sub>yi</sub>th class center of deep features. The formulation effectively characterizes the intra-class variations. 
Ideally, the c<sub>yi</sub> should be updated as the deep features changed. In other words, we need to take the entire training set into account and average 
the features of every class in each iteration, which is inefficient even impractical. 

to address this problem, two modify are used:
1. instead of updating the centers with respect to the entire training set,perform the update based on the mini-batch
2. to avoid large perturbations, use scalar alpha to control the learning rate of the centers


The gradients of _L<sub>C</sub>_ with respect to x<sub>i</sub> and update equation of _c<sub>yi</sub>_ are computed as:

![test](https://user-images.githubusercontent.com/19379550/61193635-482fd680-a6ef-11e9-9afb-0f0f8ba035b7.jpg)


adopt the joint supervision of softmax loss and center loss to train the CNNs for discriminative feature learning.


tips:
the disadvantage of contrastive loss and triplet loss is the number of training pairs or triplets dramatically grows.
--------
### A-softmax(SphereFace: Deep Hypersphere Embedding for Face Recognition)


this paper addresses discriminative features, idea features are expected to have smaller maximal intra-class
distance than minimal inter-class distance under a suitably chosen metric space


the softmax loss:   
![softmax-loss](https://user-images.githubusercontent.com/19379550/62436191-7c883700-b771-11e9-920d-d67c7749f019.jpg)

softmax loss only learns separable features that are not discriminative enough.

center loss only explicitly encourages intra-class compact- ness. Both contrastive loss and triplet loss 
can not constrain on each individual sample, and thus require carefully designed pair/triplet mining procedure, 
which is both time-consuming and performance-sensitive.

above method are Euclidean margin based loss, However, as can be observed from below pic, the features learned by 
softmax loss have intrinsic angular distribution
![softmax](https://user-images.githubusercontent.com/19379550/62436619-c9b8d880-b772-11e9-9e08-8a75db43544e.jpg)
if normalize ||W<sub>j</sub>|| we can get modified softmax loss

the A-Softmax Loss:   
![A-softmax](https://user-images.githubusercontent.com/19379550/62436914-b8240080-b773-11e9-963f-ed1ccb492d10.jpg)
--------

### NormFace
apply both feature normalization and weight normalization 


------

### AM-Softmax(Additive Margin Softmax for Face Verification)

margin is a scalar subtracted from cosθ, we call our loss function Additive Margin Softmax (AM-Softmax).    

a-softmax formulation making ||Wi|| to be 1:   

![A-softmax](https://user-images.githubusercontent.com/19379550/62438996-9418ed00-b77c-11e9-8859-2d0e9e7ecd74.jpg)

and the phi(theta):   
![phi](https://user-images.githubusercontent.com/19379550/62439173-8021bb00-b77d-11e9-857b-df1dccc708ae.jpg)


the new specific phi:   
![new_phi](https://user-images.githubusercontent.com/19379550/62439389-2968b100-b77e-11e9-9aba-d7520346f1ec.jpg)

apply both feature normalization and weight normalization to the inner product layer in order to build a cosine layer.

the loss function becomes:
![AM-softmax](https://user-images.githubusercontent.com/19379550/62439441-67fe6b80-b77e-11e9-8d58-4d8348206b4c.jpg)


-------

### LMCL(CosFace:Large Margin Cosine Loss for Deep Face Recognition) 

this paper is similar to am-softmax one 
In this paper, reformulate the softmax loss as a cosine loss by L2 normalizing both features and weight vectors to 
remove radial variations, based on which a cosine margin term m is introduced to further maximize the decision margin 
in the angular space.    
![different-loss](https://user-images.githubusercontent.com/19379550/62443377-4ce72800-b78d-11e9-91cf-7c59b822f468.jpg)
------

### ArcFace/InsightFace (ArcFace: Additive Angular Margin Loss for Deep Face Recognition)
