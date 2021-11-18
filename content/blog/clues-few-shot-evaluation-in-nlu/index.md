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

## Dataset examples

![Examples](images/clues_examples.png)

## Unified metric

$$
\text{S1}(\mathbf{p}, \mathbf{a}) = \begin{cases}
    \frac{2.0}{\frac{1}{\text{p}(\mathbf{p}, \mathbf{a})} + \frac{1}{\text{r}(\mathbf{p}, \mathbf{a})}} &\text{if } \mathbf{a} \not = \emptyset, \mathbf{p} \not = \emptyset, \text{p}(\mathbf{p}, \mathbf{a}) \cdot \text{r}(\mathbf{p}, \mathbf{a}) \not = 0 \newline
    1.0 &\text{if } a = \emptyset, p = \emptyset \newline
    0.0 &\text{otherwise}
\end{cases}
$$

## Baseline results

![classification](images/classification_results.png)

![mrc](images/mrc_results.png)