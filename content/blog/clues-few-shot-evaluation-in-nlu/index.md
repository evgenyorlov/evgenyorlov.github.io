---
author: "Evgeny Orlov"
title: "Paper Summary: CLUES Few-Shot Learning Evaluation in Natural Language Understanding"
date: "2021-11-18"
categories: ["paper_summary"]
tags: ["few_shot", "nlp", "nlu", "dataset"]
draft: true
math: true
---

[Paper URL](https://arxiv.org/abs/2111.02570) | [Code and dataset URL](https://github.com/microsoft/CLUES)

What did authors try to accomplish?

What were the key elements of the approach?

$$
 \varphi = 1+\frac{1} {1+\frac{1} {1+\frac{1} {1+\cdots} } }
$$

Some text in between
, p(p, a)r(p, a) \not = 0

$$
\text{S1}(\mathbf{p}, \mathbf{a}) = \begin{cases}
   a &\text{if } \mathbf{a} \not = \emptyset, \mathbf{p} \not = \emptyset \\
   1.0 &\text{if } a = \emptyset, p = \emptyset \\
   0.0 &\text{otherwise}
\end{cases}
$$

$$
x = \begin{cases}
   a &\text{if } b \\

   c &\text{if } d
\end{cases}
$$

$$
x = \begin{cases}
   a &\text{if } b
   c &\text{if } d
\end{cases}
$$


![Examples](images/clues_examples.png)