---
author: "Evgeny Orlov"
title: "Paper Summary: CLUES Few-Shot Learning Evaluation in Natural Language Understanding"
description: "New dataset for NLU evaluation in the few-shot setting by Microsoft Research"
date: "2021-11-18"
categories: ["paper_summary"]
tags: ["few_shot", "nlp", "nlu", "dataset"]
draft: true
math: true
cover.image: 'clues_examples.png'
cover.hiddenInList: false
cover.hiddenInSingle: false
cover.hidden: false
cover.responsiveImages: false
---

[Paper URL](https://arxiv.org/abs/2111.02570) | [Code and dataset URL](https://github.com/microsoft/CLUES)

What did authors try to accomplish?

$$
 \varphi = 1+\frac{1} {2}
$$

What were the key elements of the approach?

$$
 \varphi = 1+\frac{1} {1+\frac{1} {1+\frac{1} {1+\cdots} } }
$$

Some text in between
, p(p, a)r(p, a) \not = 0

$$
S1(p, a) = \begin{cases}
   a &\text{if a \not = \emptyset, p \not = \emptyset} \\
   1.0 &\text{if a = \emptyset, p = \emptyset} \\
   0.0 &\text{otherwise}
\end{cases}
$$

$$
x = \begin{cases}
   a &\text{if } b \\
   c &\text{if } d
\end{cases}
$$


![Examples](images/clues_examples.png)