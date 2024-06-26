# saucam/llama-airo-3 results

## nous results 

 |Benchmark|                          Model                           |agieval|bigbench|gpt4all|truthfulqa|Average|
|---------|----------------------------------------------------------|------:|-------:|------:|---------:|------:|
|nous     |[llama-airo-3](https://huggingface.co/saucam/llama-airo-3)|  36.59|   39.26|  72.24|      56.3|   51.1|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |24.80|±  |  2.72|
|                              |       |acc_norm|25.98|±  |  2.76|
|agieval_logiqa_en             |      0|acc     |31.03|±  |  1.81|
|                              |       |acc_norm|33.64|±  |  1.85|
|agieval_lsat_ar               |      0|acc     |18.26|±  |  2.55|
|                              |       |acc_norm|16.96|±  |  2.48|
|agieval_lsat_lr               |      0|acc     |36.27|±  |  2.13|
|                              |       |acc_norm|35.29|±  |  2.12|
|agieval_lsat_rc               |      0|acc     |51.67|±  |  3.05|
|                              |       |acc_norm|47.58|±  |  3.05|
|agieval_sat_en                |      0|acc     |67.48|±  |  3.27|
|                              |       |acc_norm|58.25|±  |  3.44|
|agieval_sat_en_without_passage|      0|acc     |41.75|±  |  3.44|
|                              |       |acc_norm|35.92|±  |  3.35|
|agieval_sat_math              |      0|acc     |44.55|±  |  3.36|
|                              |       |acc_norm|39.09|±  |  3.30|

Average: 36.59%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|55.26|±  |  3.62|
|bigbench_date_understanding                     |      0|multiple_choice_grade|66.94|±  |  2.45|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|34.50|±  |  2.97|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|23.96|±  |  2.26|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|31.20|±  |  2.07|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|22.71|±  |  1.58|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|47.00|±  |  2.89|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|30.40|±  |  2.06|
|bigbench_navigate                               |      0|multiple_choice_grade|49.40|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|63.85|±  |  1.07|
|bigbench_ruin_names                             |      0|multiple_choice_grade|31.92|±  |  2.20|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|23.65|±  |  1.35|
|bigbench_snarks                                 |      0|multiple_choice_grade|59.67|±  |  3.66|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|54.97|±  |  1.59|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|25.90|±  |  1.39|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|22.08|±  |  1.17|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|16.29|±  |  0.88|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|47.00|±  |  2.89|

Average: 39.26%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |54.69|±  |  1.45|
|             |       |acc_norm|57.59|±  |  1.44|
|arc_easy     |      0|acc     |83.71|±  |  0.76|
|             |       |acc_norm|81.86|±  |  0.79|
|boolq        |      1|acc     |84.50|±  |  0.63|
|hellaswag    |      0|acc     |61.49|±  |  0.49|
|             |       |acc_norm|80.57|±  |  0.39|
|openbookqa   |      0|acc     |35.00|±  |  2.14|
|             |       |acc_norm|46.00|±  |  2.23|
|piqa         |      0|acc     |80.14|±  |  0.93|
|             |       |acc_norm|81.01|±  |  0.92|
|winogrande   |      0|acc     |74.11|±  |  1.23|

Average: 72.24%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |39.78|±  |  1.71|
|             |       |mc2   |56.30|±  |  1.52|

Average: 56.3%

Average score: 51.1%

Metadata: {'elapsed_time': '11:34:38', 'gpu': 'NVIDIA A100 80GB PCIe'}

## openllm results 

 |Benchmark|                          Model                           |gsm8k| arc |hellaswag|mmlu |truthfulqa|winogrande|Average|
|---------|----------------------------------------------------------|----:|----:|--------:|----:|---------:|---------:|------:|
|openllm  |[llama-airo-3](https://huggingface.co/saucam/llama-airo-3)|56.33|61.01|    82.42|64.79|     56.35|     78.22|  66.52|

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.56|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.57|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 56.33%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.58|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.61|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 61.01%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.62|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.82|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 82.42%

### mmlu
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                   0.65|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.28                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.56                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.35                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.39                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.61                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.40                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.51                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.34                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.51                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.88                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.34                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.45                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.60                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.90                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.81                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.41                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.55                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 64.79%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rouge2_max,none        |            30.31|   |      |
|              |       |rouge2_max_stderr,none |             0.88|   |      |
|              |       |bleu_diff,none         |            -1.26|   |      |
|              |       |bleu_diff_stderr,none  |             0.55|   |      |
|              |       |rouge1_max,none        |            45.97|   |      |
|              |       |rouge1_max_stderr,none |             0.77|   |      |
|              |       |acc,none               |             0.48|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |rougeL_acc,none        |             0.48|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_acc,none        |             0.39|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |            -1.43|   |      |
|              |       |rougeL_diff_stderr,none|             0.72|   |      |
|              |       |rougeL_max,none        |            42.50|   |      |
|              |       |rougeL_max_stderr,none |             0.78|   |      |
|              |       |rouge1_diff,none       |            -1.35|   |      |
|              |       |rouge1_diff_stderr,none|             0.71|   |      |
|              |       |bleu_acc,none          |             0.43|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_max,none          |            19.13|   |      |
|              |       |bleu_max_stderr,none   |             0.67|   |      |
|              |       |rouge2_diff,none       |            -2.60|   |      |
|              |       |rouge2_diff_stderr,none|             0.84|   |      |
|              |       |rouge1_acc,none        |             0.47|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            19.13|   |      |
|              |       |bleu_max_stderr,none   |             0.67|   |      |
|              |       |bleu_acc,none          |             0.43|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |            -1.26|   |      |
|              |       |bleu_diff_stderr,none  |             0.55|   |      |
|              |       |rouge1_max,none        |            45.97|   |      |
|              |       |rouge1_max_stderr,none |             0.77|   |      |
|              |       |rouge1_acc,none        |             0.47|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |            -1.35|   |      |
|              |       |rouge1_diff_stderr,none|             0.71|   |      |
|              |       |rouge2_max,none        |            30.31|   |      |
|              |       |rouge2_max_stderr,none |             0.88|   |      |
|              |       |rouge2_acc,none        |             0.39|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |            -2.60|   |      |
|              |       |rouge2_diff_stderr,none|             0.84|   |      |
|              |       |rougeL_max,none        |            42.50|   |      |
|              |       |rougeL_max_stderr,none |             0.78|   |      |
|              |       |rougeL_acc,none        |             0.48|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |            -1.43|   |      |
|              |       |rougeL_diff_stderr,none|             0.72|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.40|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.56|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 56.35%

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.78|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 78.22%

Average score: 66.52%

Metadata: {'elapsed_time': '03:41:18', 'gpu': 'NVIDIA A100 80GB PCIe'}

