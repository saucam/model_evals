# saucam/mistral-orpo-beta-NeuralBeagle14-7B-dare-ties results

## openllm results 

 |Benchmark|                                                           Model                                                            |winogrande| arc |gsm8k|truthfulqa|hellaswag|Average|
|---------|----------------------------------------------------------------------------------------------------------------------------|---------:|----:|----:|---------:|--------:|------:|
|openllm  |[mistral-orpo-beta-NeuralBeagle14-7B-dare-ties](https://huggingface.co/saucam/mistral-orpo-beta-NeuralBeagle14-7B-dare-ties)|     81.14|67.32|61.79|     54.17|    85.89|  70.06|

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.81|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 81.14%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.63|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.67|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 67.32%

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.62|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.62|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 61.79%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rouge1_diff,none       |            13.01|   |      |
|              |       |rouge1_diff_stderr,none|             1.41|   |      |
|              |       |rougeL_diff,none       |            12.57|   |      |
|              |       |rougeL_diff_stderr,none|             1.43|   |      |
|              |       |bleu_max,none          |            34.91|   |      |
|              |       |bleu_max_stderr,none   |             0.87|   |      |
|              |       |rouge2_max,none        |            49.18|   |      |
|              |       |rouge2_max_stderr,none |             1.08|   |      |
|              |       |rouge2_diff,none       |            12.96|   |      |
|              |       |rouge2_diff_stderr,none|             1.54|   |      |
|              |       |acc,none               |             0.45|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |rougeL_acc,none        |             0.52|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |bleu_acc,none          |             0.52|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |rouge2_acc,none        |             0.49|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_acc,none        |             0.54|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |bleu_diff,none         |             9.25|   |      |
|              |       |bleu_diff_stderr,none  |             1.06|   |      |
|              |       |rougeL_max,none        |            59.19|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rouge1_max,none        |            61.89|   |      |
|              |       |rouge1_max_stderr,none |             0.88|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            34.91|   |      |
|              |       |bleu_max_stderr,none   |             0.87|   |      |
|              |       |bleu_acc,none          |             0.52|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |             9.25|   |      |
|              |       |bleu_diff_stderr,none  |             1.06|   |      |
|              |       |rouge1_max,none        |            61.89|   |      |
|              |       |rouge1_max_stderr,none |             0.88|   |      |
|              |       |rouge1_acc,none        |             0.54|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |            13.01|   |      |
|              |       |rouge1_diff_stderr,none|             1.41|   |      |
|              |       |rouge2_max,none        |            49.18|   |      |
|              |       |rouge2_max_stderr,none |             1.08|   |      |
|              |       |rouge2_acc,none        |             0.49|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |            12.96|   |      |
|              |       |rouge2_diff_stderr,none|             1.54|   |      |
|              |       |rougeL_max,none        |            59.19|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rougeL_acc,none        |             0.52|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |            12.57|   |      |
|              |       |rougeL_diff_stderr,none|             1.43|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.37|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.54|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 54.17%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.67|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.86|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 85.89%

Average score: 70.06%

Metadata: {}

