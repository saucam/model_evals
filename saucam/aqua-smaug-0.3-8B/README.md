# saucam/aqua-smaug-0.3-8B results

## openllm results 

 |Benchmark|                               Model                                |winogrande| arc |gsm8k|mmlu|truthfulqa|hellaswag|Average|
|---------|--------------------------------------------------------------------|---------:|----:|----:|---:|---------:|--------:|------:|
|openllm  |[aqua-smaug-0.3-8B](https://huggingface.co/saucam/aqua-smaug-0.3-8B)|     77.11|62.37|76.19|  66|      53.7|    83.02|  69.73|

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.77|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 77.11%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.59|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.62|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 62.37%

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.76|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.76|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 76.19%

### mmlu
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                   0.66|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.33                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.61                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.38                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.60                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.44                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.40                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.91                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.39                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.41                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.87                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.60                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.81                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.92                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.42                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.48                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.69                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.87                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.56                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 66.0%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rougeL_acc,none        |             0.49|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_acc,none        |             0.51|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |bleu_acc,none          |             0.49|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_max,none          |            26.70|   |      |
|              |       |bleu_max_stderr,none   |             0.81|   |      |
|              |       |rougeL_diff,none       |             2.40|   |      |
|              |       |rougeL_diff_stderr,none|             1.04|   |      |
|              |       |rouge1_diff,none       |             2.47|   |      |
|              |       |rouge1_diff_stderr,none|             1.03|   |      |
|              |       |rouge2_acc,none        |             0.42|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |acc,none               |             0.46|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |rouge2_max,none        |            36.75|   |      |
|              |       |rouge2_max_stderr,none |             1.04|   |      |
|              |       |rouge2_diff,none       |             1.52|   |      |
|              |       |rouge2_diff_stderr,none|             1.16|   |      |
|              |       |rougeL_max,none        |            49.63|   |      |
|              |       |rougeL_max_stderr,none |             0.88|   |      |
|              |       |bleu_diff,none         |             1.78|   |      |
|              |       |bleu_diff_stderr,none  |             0.80|   |      |
|              |       |rouge1_max,none        |            52.58|   |      |
|              |       |rouge1_max_stderr,none |             0.85|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            26.70|   |      |
|              |       |bleu_max_stderr,none   |             0.81|   |      |
|              |       |bleu_acc,none          |             0.49|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |             1.78|   |      |
|              |       |bleu_diff_stderr,none  |             0.80|   |      |
|              |       |rouge1_max,none        |            52.58|   |      |
|              |       |rouge1_max_stderr,none |             0.85|   |      |
|              |       |rouge1_acc,none        |             0.51|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |             2.47|   |      |
|              |       |rouge1_diff_stderr,none|             1.03|   |      |
|              |       |rouge2_max,none        |            36.75|   |      |
|              |       |rouge2_max_stderr,none |             1.04|   |      |
|              |       |rouge2_acc,none        |             0.42|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |             1.52|   |      |
|              |       |rouge2_diff_stderr,none|             1.16|   |      |
|              |       |rougeL_max,none        |            49.63|   |      |
|              |       |rougeL_max_stderr,none |             0.88|   |      |
|              |       |rougeL_acc,none        |             0.49|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |             2.40|   |      |
|              |       |rougeL_diff_stderr,none|             1.04|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.38|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.54|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 53.7%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.64|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.83|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 83.02%

Average score: 69.73%

Metadata: {'elapsed_time': '02:22:58', 'gpu': 'NVIDIA A100 80GB PCIe'}

