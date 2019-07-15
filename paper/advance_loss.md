### center loss(A Discriminative Feature Learning Approach for Deep Face Recognition)

this paper proposed center loss, the center loss simultaneously learns a center for deep features of each class and 
penalizes the distances between the deep features and their corresponding class centers. the softmax loss forces the 
deep features of different classes staying apart. The center loss efficiently pulls the deep features of the same class to their centers

------
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
