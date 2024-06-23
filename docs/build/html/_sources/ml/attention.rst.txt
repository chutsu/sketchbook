Attention is a cognitive and behavioural function that enables us to focus on a
subset of the incoming data or information. This function allows us to ignore
irrelevant perceptible information and allows us to concentrate on high-value
information.

Attention mechanisms can be categorized into two classes:

- Bottom-up unconscious attention: Saliency-based attention are stimulated by
  external factors. As an example, louder voices are heard more easily compared
  to quieter ones. (Max-pooling and gating mechanisms)

- Top-Down conscious attention: Focused attention has a predetermined goal and
  follows specific tasks.


One way to visualize implicit attention is by looking at the partial derivatives
with respect to the input (a.k.a. the Jacobian matrix).

We may have reasons to explicitly enforce implicit attention, we can achieve
this by placing more weight on sensitive parts of the model.

Hard Soft Attention
===================

Hard / Soft attention: Hard attention means the function are described by
discrete variables, while soft attention is described by continuous variables.
This distinction is important because the derivatives of these functions are
either step or smooth. Hard attention is non-diffrential, therefore we cannot
use gradient descent techniques to train. This is is why Reinforcement Learning
(RL) techniques such as policy gradients and REINFORCE algorithm is commonly
used.

