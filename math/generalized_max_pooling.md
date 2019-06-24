### Generalized Max Pooling

&emsp;&emsp;the paper introduce a method for feature representations involve a pooling
operation that aggregates statistics computed from local descriptors.

standard pooling operation include sum- and max-pooing
the sum-pooling with weakly influenced by rare yet potentially highly-informative local feature.

like the pic below:

![GMP](https://user-images.githubusercontent.com/19379550/60000027-f5d23b80-9695-11e9-9591-f21ba3c798eb.jpg)

the inference as below:

enforce the dot-product similarity between each patch encoding φn and the GMP representation φgmp to be a constant c   
- ![1](https://user-images.githubusercontent.com/19379550/60000334-8f99e880-9696-11e9-898e-864f29187890.jpg)

arbitrarily set the constant c =1,Let Φ de- note the D × N matrix that contains the patch encodings: Φ = [φ1 , ..., φN ]. In matrix form, (1) can be rewritten as:
- ![2](https://user-images.githubusercontent.com/19379550/60000361-a0e2f500-9696-11e9-89b8-f2f173d18f79.jpg)


if D>N we might have an infinite number of solutions   
else N>D the system might not have a solution   
Therefore, we turn (2) into a least-squares regression problem and seek:
- ![3](https://user-images.githubusercontent.com/19379550/60000727-5ada6100-9697-11e9-9cce-826d47a30fcf.jpg)

closed-form solution:
- ![4](https://user-images.githubusercontent.com/19379550/60000862-a260ed00-9697-11e9-9bc9-9d98447bddc1.jpg)

where + denotes the pseudo-inverse and the second equality stems from the property A+ = (AT A)+AT . We note that Φ1N = 􏰀Nn=1 φ(xn) = φsum is the sum-pooled represen- tation. Hence, the proposed GMP involves projecting the φsum on (ΦΦT )+.

since the pseudo-inverse is not a continuous operation it
is beneficial to add a regularization term to obtain a stable
solution:
- ![5](https://user-images.githubusercontent.com/19379550/60001122-55c9e180-9698-11e9-9524-2fbbcc078c8e.jpg)

in practice The choice of λ (the regular- ization parameter of the GMP) has a significant
 impact on the final performance and was chosen by cross-validation from 
 the set {101, 102, 103, 104, 105}.

