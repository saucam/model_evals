# saucam/Orpomis-Prime-7B-dare results

## nous results 

 |Benchmark|                                   Model                                    |agieval|bigbench|gpt4all|truthfulqa|Average|
|---------|----------------------------------------------------------------------------|------:|-------:|------:|---------:|------:|
|nous     |[Orpomis-Prime-7B-dare](https://huggingface.co/saucam/Orpomis-Prime-7B-dare)|  42.71|   39.82|  73.42|     53.72|  52.42|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |22.44|±  |  2.62|
|                              |       |acc_norm|22.83|±  |  2.64|
|agieval_logiqa_en             |      0|acc     |36.10|±  |  1.88|
|                              |       |acc_norm|37.33|±  |  1.90|
|agieval_lsat_ar               |      0|acc     |22.61|±  |  2.76|
|                              |       |acc_norm|23.04|±  |  2.78|
|agieval_lsat_lr               |      0|acc     |47.65|±  |  2.21|
|                              |       |acc_norm|48.63|±  |  2.22|
|agieval_lsat_rc               |      0|acc     |57.99|±  |  3.01|
|                              |       |acc_norm|55.02|±  |  3.04|
|agieval_sat_en                |      0|acc     |71.84|±  |  3.14|
|                              |       |acc_norm|70.87|±  |  3.17|
|agieval_sat_en_without_passage|      0|acc     |49.03|±  |  3.49|
|                              |       |acc_norm|47.57|±  |  3.49|
|agieval_sat_math              |      0|acc     |37.73|±  |  3.28|
|                              |       |acc_norm|36.36|±  |  3.25|

Average: 42.71%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|55.79|±  |  3.61|
|bigbench_date_understanding                     |      0|multiple_choice_grade|67.48|±  |  2.44|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|42.25|±  |  3.08|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|20.61|±  |  2.14|
|                                                |       |exact_str_match      | 0.28|±  |  0.28|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|26.20|±  |  1.97|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|19.29|±  |  1.49|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|44.33|±  |  2.87|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|32.60|±  |  2.10|
|bigbench_navigate                               |      0|multiple_choice_grade|50.10|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|60.60|±  |  1.09|
|bigbench_ruin_names                             |      0|multiple_choice_grade|40.85|±  |  2.32|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|17.84|±  |  1.21|
|bigbench_snarks                                 |      0|multiple_choice_grade|71.27|±  |  3.37|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|57.40|±  |  1.58|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|28.00|±  |  1.42|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|21.76|±  |  1.17|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|16.06|±  |  0.88|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|44.33|±  |  2.87|

Average: 39.82%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |57.08|±  |  1.45|
|             |       |acc_norm|60.15|±  |  1.43|
|arc_easy     |      0|acc     |83.08|±  |  0.77|
|             |       |acc_norm|82.66|±  |  0.78|
|boolq        |      1|acc     |86.91|±  |  0.59|
|hellaswag    |      0|acc     |63.94|±  |  0.48|
|             |       |acc_norm|82.83|±  |  0.38|
|openbookqa   |      0|acc     |33.00|±  |  2.10|
|             |       |acc_norm|43.40|±  |  2.22|
|piqa         |      0|acc     |81.50|±  |  0.91|
|             |       |acc_norm|83.19|±  |  0.87|
|winogrande   |      0|acc     |74.82|±  |  1.22|

Average: 73.42%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |36.72|±  |  1.69|
|             |       |mc2   |53.72|±  |  1.52|

Average: 53.72%

Average score: 52.42%

Metadata: {'elapsed_time': '01:51:18', 'gpu': 'NVIDIA RTX 6000 Ada Generation'}

## openllm results 

 |Benchmark|                                   Model                                    |gsm8k| arc |hellaswag|mmlu |truthfulqa|winogrande|Average|
|---------|----------------------------------------------------------------------------|----:|----:|--------:|----:|---------:|---------:|------:|
|openllm  |[Orpomis-Prime-7B-dare](https://huggingface.co/saucam/Orpomis-Prime-7B-dare)|59.74|64.68|    85.12|62.21|     53.72|     78.77|  67.37|

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.60|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.60|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 59.74%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.61|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.65|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 64.68%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.66|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.85|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 85.12%

### mmlu
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                   0.62|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.30                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.59                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.48                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.30                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.38                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.41                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.46                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.35                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.88                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.36                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.56                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.46                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.88                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.24                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.46                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.55                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 62.21%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rougeL_diff,none       |             9.45|   |      |
|              |       |rougeL_diff_stderr,none|             1.36|   |      |
|              |       |rouge2_acc,none        |             0.48|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_max,none        |            60.08|   |      |
|              |       |rouge1_max_stderr,none |             0.88|   |      |
|              |       |bleu_diff,none         |             6.84|   |      |
|              |       |bleu_diff_stderr,none  |             1.02|   |      |
|              |       |rouge2_max,none        |            46.72|   |      |
|              |       |rouge2_max_stderr,none |             1.08|   |      |
|              |       |rouge1_acc,none        |             0.52|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_max,none        |            57.11|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rouge2_diff,none       |             9.46|   |      |
|              |       |rouge2_diff_stderr,none|             1.47|   |      |
|              |       |acc,none               |             0.45|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |bleu_acc,none          |             0.51|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |rouge1_diff,none       |             9.88|   |      |
|              |       |rouge1_diff_stderr,none|             1.34|   |      |
|              |       |rougeL_acc,none        |             0.51|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |bleu_max,none          |            33.30|   |      |
|              |       |bleu_max_stderr,none   |             0.87|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            33.30|   |      |
|              |       |bleu_max_stderr,none   |             0.87|   |      |
|              |       |bleu_acc,none          |             0.51|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |             6.84|   |      |
|              |       |bleu_diff_stderr,none  |             1.02|   |      |
|              |       |rouge1_max,none        |            60.08|   |      |
|              |       |rouge1_max_stderr,none |             0.88|   |      |
|              |       |rouge1_acc,none        |             0.52|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |             9.88|   |      |
|              |       |rouge1_diff_stderr,none|             1.34|   |      |
|              |       |rouge2_max,none        |            46.72|   |      |
|              |       |rouge2_max_stderr,none |             1.08|   |      |
|              |       |rouge2_acc,none        |             0.48|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |             9.46|   |      |
|              |       |rouge2_diff_stderr,none|             1.47|   |      |
|              |       |rougeL_max,none        |            57.11|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rougeL_acc,none        |             0.51|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |             9.45|   |      |
|              |       |rougeL_diff_stderr,none|             1.36|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.37|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.54|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 53.72%

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.79|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 78.77%

Average score: 67.37%

Metadata: {'elapsed_time': '02:51:10', 'gpu': 'NVIDIA A100 80GB PCIe'}

