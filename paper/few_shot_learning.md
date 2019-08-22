### Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks

in MAML method, the parameters of the model are explicitly trained such that a small number of gradient 
steps with a small amount of training data from a new task will produce good generalization performance on that task

The intuition behind this approach is that some internal representations are more transferrable than others,
so find model parameters that are sensitive to changes in the task

the mechanism for learning to learn(meta-learning) should be general to the task
the common MAML
![image](https://user-images.githubusercontent.com/19379550/63484059-0144b600-c4d1-11e9-919d-315acc61ef86.png)

for shot learning:


### A CLOSER LOOK AT FEW-SHOT CLASSIFICATION

three contributions this paper:
1. several different few-shot classification algorithms for a fair comparison,Increasing the model capacity of the feature backbone reduces the performance gap between different methods when domain differences are limited
2. a distance-based (cosine) classifier surprisingly achieves competitive performance with the state-of-the art meta-learning.
3. current few-shot classification algorithms fail to address such do- main shifts and are inferior even to the baseline method


baseline method and baseline++ method:
![image](https://user-images.githubusercontent.com/19379550/63494363-1a109400-c4f0-11e9-8636-b47394cb1fed.png)

meta-learning method:
![image](https://user-images.githubusercontent.com/19379550/63494476-4af0c900-c4f0-11e9-9e4d-700dd0b72b55.png)

experiment:
![image](https://user-images.githubusercontent.com/19379550/63494546-7d9ac180-c4f0-11e9-8eb5-f563a0a0c044.png)





