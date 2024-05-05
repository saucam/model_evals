# saucam/Orpomis-Prime-7B results

## nous results 

 |Benchmark|                              Model                               |agieval|bigbench|gpt4all|truthfulqa|Average|
|---------|------------------------------------------------------------------|------:|-------:|------:|---------:|------:|
|nous     |[Orpomis-Prime-7B](https://huggingface.co/saucam/Orpomis-Prime-7B)|   36.4|    37.5|  72.18|     41.02|  46.78|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |23.62|±  |  2.67|
|                              |       |acc_norm|22.83|±  |  2.64|
|agieval_logiqa_en             |      0|acc     |30.11|±  |  1.80|
|                              |       |acc_norm|33.95|±  |  1.86|
|agieval_lsat_ar               |      0|acc     |17.83|±  |  2.53|
|                              |       |acc_norm|18.26|±  |  2.55|
|agieval_lsat_lr               |      0|acc     |39.22|±  |  2.16|
|                              |       |acc_norm|41.18|±  |  2.18|
|agieval_lsat_rc               |      0|acc     |44.61|±  |  3.04|
|                              |       |acc_norm|46.10|±  |  3.04|
|agieval_sat_en                |      0|acc     |55.34|±  |  3.47|
|                              |       |acc_norm|52.91|±  |  3.49|
|agieval_sat_en_without_passage|      0|acc     |46.60|±  |  3.48|
|                              |       |acc_norm|43.69|±  |  3.46|
|agieval_sat_math              |      0|acc     |32.73|±  |  3.17|
|                              |       |acc_norm|32.27|±  |  3.16|

Average: 36.4%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|53.68|±  |  3.63|
|bigbench_date_understanding                     |      0|multiple_choice_grade|67.75|±  |  2.44|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|37.21|±  |  3.02|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|20.89|±  |  2.15|
|                                                |       |exact_str_match      | 9.75|±  |  1.57|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|22.20|±  |  1.86|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|14.71|±  |  1.34|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|37.67|±  |  2.80|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|34.00|±  |  2.12|
|bigbench_navigate                               |      0|multiple_choice_grade|50.80|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|55.00|±  |  1.11|
|bigbench_ruin_names                             |      0|multiple_choice_grade|32.59|±  |  2.22|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|22.34|±  |  1.32|
|bigbench_snarks                                 |      0|multiple_choice_grade|56.91|±  |  3.69|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|50.20|±  |  1.59|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|44.00|±  |  1.57|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|23.04|±  |  1.19|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|14.34|±  |  0.84|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|37.67|±  |  2.80|

Average: 37.5%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |54.44|±  |  1.46|
|             |       |acc_norm|58.02|±  |  1.44|
|arc_easy     |      0|acc     |82.24|±  |  0.78|
|             |       |acc_norm|82.32|±  |  0.78|
|boolq        |      1|acc     |83.76|±  |  0.65|
|hellaswag    |      0|acc     |61.26|±  |  0.49|
|             |       |acc_norm|80.84|±  |  0.39|
|openbookqa   |      0|acc     |33.20|±  |  2.11|
|             |       |acc_norm|44.40|±  |  2.22|
|piqa         |      0|acc     |81.83|±  |  0.90|
|             |       |acc_norm|83.62|±  |  0.86|
|winogrande   |      0|acc     |72.30|±  |  1.26|

Average: 72.18%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |27.78|±  |  1.57|
|             |       |mc2   |41.02|±  |  1.45|

Average: 41.02%

Average score: 46.78%

Metadata: {'elapsed_time': '01:45:01', 'gpu': 'NVIDIA RTX 6000 Ada Generation'}

## openllm results 

 |Benchmark|                              Model                               |gsm8k| arc |hellaswag|mmlu |truthfulqa|winogrande|Average|
|---------|------------------------------------------------------------------|----:|----:|--------:|----:|---------:|---------:|------:|
|openllm  |[Orpomis-Prime-7B](https://huggingface.co/saucam/Orpomis-Prime-7B)|24.41|60.67|    79.12|52.43|     41.02|     73.95|  55.27|

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.24|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.24|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 24.41%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.55|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.61|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 60.67%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.58|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.79|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 79.12%

### mmlu
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                   0.52|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.59                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.41                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.37                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.34                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.58                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.48                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.42                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.42                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.39                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.36                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.42                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.56                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.81                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.53                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.32                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.53                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.27                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.38                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.60                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.51                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.59                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.61                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.55                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.63                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.40                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.38                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.51                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.55                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.43                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 52.43%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rouge2_max,none        |            30.11|   |      |
|              |       |rouge2_max_stderr,none |             1.03|   |      |
|              |       |rouge2_diff,none       |            -8.36|   |      |
|              |       |rouge2_diff_stderr,none|             1.05|   |      |
|              |       |rougeL_max,none        |            44.03|   |      |
|              |       |rougeL_max_stderr,none |             0.93|   |      |
|              |       |rouge1_acc,none        |             0.35|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |bleu_acc,none          |             0.40|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |rougeL_acc,none        |             0.34|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |acc,none               |             0.34|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |bleu_diff,none         |            -4.83|   |      |
|              |       |bleu_diff_stderr,none  |             0.78|   |      |
|              |       |rouge1_max,none        |            46.48|   |      |
|              |       |rouge1_max_stderr,none |             0.94|   |      |
|              |       |bleu_max,none          |            24.05|   |      |
|              |       |bleu_max_stderr,none   |             0.75|   |      |
|              |       |rougeL_diff,none       |            -7.79|   |      |
|              |       |rougeL_diff_stderr,none|             0.93|   |      |
|              |       |rouge2_acc,none        |             0.26|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |            -7.81|   |      |
|              |       |rouge1_diff_stderr,none|             0.93|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            24.05|   |      |
|              |       |bleu_max_stderr,none   |             0.75|   |      |
|              |       |bleu_acc,none          |             0.40|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |            -4.83|   |      |
|              |       |bleu_diff_stderr,none  |             0.78|   |      |
|              |       |rouge1_max,none        |            46.48|   |      |
|              |       |rouge1_max_stderr,none |             0.94|   |      |
|              |       |rouge1_acc,none        |             0.35|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |            -7.81|   |      |
|              |       |rouge1_diff_stderr,none|             0.93|   |      |
|              |       |rouge2_max,none        |            30.11|   |      |
|              |       |rouge2_max_stderr,none |             1.03|   |      |
|              |       |rouge2_acc,none        |             0.26|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |            -8.36|   |      |
|              |       |rouge2_diff_stderr,none|             1.05|   |      |
|              |       |rougeL_max,none        |            44.03|   |      |
|              |       |rougeL_max_stderr,none |             0.93|   |      |
|              |       |rougeL_acc,none        |             0.34|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |            -7.79|   |      |
|              |       |rougeL_diff_stderr,none|             0.93|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.28|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.41|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 41.02%

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.74|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 73.95%

Average score: 55.27%

Metadata: {'elapsed_time': '02:37:38', 'gpu': 'NVIDIA A100 80GB PCIe'}

