# saucam/Arithmo-Wizard-2-7B results

## nous results 

 |Benchmark|                                 Model                                  |agieval|gpt4all|bigbench|truthfulqa|Average|
|---------|------------------------------------------------------------------------|------:|------:|-------:|---------:|------:|
|nous     |[Arithmo-Wizard-2-7B](https://huggingface.co/saucam/Arithmo-Wizard-2-7B)|  31.58|   70.2|   37.44|     45.91|  46.28|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |27.95|±  |  2.82|
|                              |       |acc_norm|27.56|±  |  2.81|
|agieval_logiqa_en             |      0|acc     |28.73|±  |  1.77|
|                              |       |acc_norm|32.72|±  |  1.84|
|agieval_lsat_ar               |      0|acc     |22.17|±  |  2.75|
|                              |       |acc_norm|18.26|±  |  2.55|
|agieval_lsat_lr               |      0|acc     |36.86|±  |  2.14|
|                              |       |acc_norm|31.76|±  |  2.06|
|agieval_lsat_rc               |      0|acc     |42.38|±  |  3.02|
|                              |       |acc_norm|34.20|±  |  2.90|
|agieval_sat_en                |      0|acc     |60.19|±  |  3.42|
|                              |       |acc_norm|50.00|±  |  3.49|
|agieval_sat_en_without_passage|      0|acc     |37.38|±  |  3.38|
|                              |       |acc_norm|27.67|±  |  3.12|
|agieval_sat_math              |      0|acc     |33.18|±  |  3.18|
|                              |       |acc_norm|30.45|±  |  3.11|

Average: 31.58%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |46.25|±  |  1.46|
|             |       |acc_norm|49.49|±  |  1.46|
|arc_easy     |      0|acc     |77.78|±  |  0.85|
|             |       |acc_norm|76.73|±  |  0.87|
|boolq        |      1|acc     |85.14|±  |  0.62|
|hellaswag    |      0|acc     |62.08|±  |  0.48|
|             |       |acc_norm|80.93|±  |  0.39|
|openbookqa   |      0|acc     |32.60|±  |  2.10|
|             |       |acc_norm|43.60|±  |  2.22|
|piqa         |      0|acc     |80.30|±  |  0.93|
|             |       |acc_norm|81.61|±  |  0.90|
|winogrande   |      0|acc     |73.88|±  |  1.23|

Average: 70.2%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|50.53|±  |  3.64|
|bigbench_date_understanding                     |      0|multiple_choice_grade|63.69|±  |  2.51|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|41.47|±  |  3.07|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|11.98|±  |  1.72|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|31.00|±  |  2.07|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|21.86|±  |  1.56|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|52.00|±  |  2.89|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|31.80|±  |  2.08|
|bigbench_navigate                               |      0|multiple_choice_grade|50.00|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|54.55|±  |  1.11|
|bigbench_ruin_names                             |      0|multiple_choice_grade|35.04|±  |  2.26|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|13.23|±  |  1.07|
|bigbench_snarks                                 |      0|multiple_choice_grade|49.72|±  |  3.73|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|49.80|±  |  1.59|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|27.40|±  |  1.41|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|21.20|±  |  1.16|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|16.63|±  |  0.89|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|52.00|±  |  2.89|

Average: 37.44%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |31.21|±  |  1.62|
|             |       |mc2   |45.91|±  |  1.51|

Average: 45.91%

Average score: 46.28%

Metadata: {'elapsed_time': '01:30:31', 'gpu': 'NVIDIA RTX 6000 Ada Generation'}

## openllm results 

 |Benchmark|                                 Model                                  |winogrande| arc |gsm8k|mmlu |truthfulqa|hellaswag|Average|
|---------|------------------------------------------------------------------------|---------:|----:|----:|----:|---------:|--------:|------:|
|openllm  |[Arithmo-Wizard-2-7B](https://huggingface.co/saucam/Arithmo-Wizard-2-7B)|     77.51|62.88|61.26|60.61|      45.9|    83.15|  65.22|

### winogrande
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.78|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 77.51%

### arc
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.58|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.63|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 62.88%

### gsm8k
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.61|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.65|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 61.26%

### mmlu
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                   0.61|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.29                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.61                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.58                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.66                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.43                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.31                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.35                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.43                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.51                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.34                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.43                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.26                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.47                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.63                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.61                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.33                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.30                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.54                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.88                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.69                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.41                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.69                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.70                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.45                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.45                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.69                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.49                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.87                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 60.61%

### truthfulqa
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |rouge2_acc,none        |             0.42|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_max,none        |            41.54|   |      |
|              |       |rouge2_max_stderr,none |             1.05|   |      |
|              |       |rouge1_max,none        |            55.34|   |      |
|              |       |rouge1_max_stderr,none |             0.89|   |      |
|              |       |rouge1_diff,none       |             2.92|   |      |
|              |       |rouge1_diff_stderr,none|             1.25|   |      |
|              |       |rougeL_diff,none       |             2.41|   |      |
|              |       |rougeL_diff_stderr,none|             1.27|   |      |
|              |       |bleu_acc,none          |             0.45|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |rouge1_acc,none        |             0.46|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_max,none        |            52.36|   |      |
|              |       |rougeL_max_stderr,none |             0.91|   |      |
|              |       |rougeL_acc,none        |             0.44|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |bleu_diff,none         |             2.01|   |      |
|              |       |bleu_diff_stderr,none  |             0.96|   |      |
|              |       |acc,none               |             0.39|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |rouge2_diff,none       |             2.52|   |      |
|              |       |rouge2_diff_stderr,none|             1.36|   |      |
|              |       |bleu_max,none          |            29.57|   |      |
|              |       |bleu_max_stderr,none   |             0.83|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            29.57|   |      |
|              |       |bleu_max_stderr,none   |             0.83|   |      |
|              |       |bleu_acc,none          |             0.45|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |             2.01|   |      |
|              |       |bleu_diff_stderr,none  |             0.96|   |      |
|              |       |rouge1_max,none        |            55.34|   |      |
|              |       |rouge1_max_stderr,none |             0.89|   |      |
|              |       |rouge1_acc,none        |             0.46|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |             2.92|   |      |
|              |       |rouge1_diff_stderr,none|             1.25|   |      |
|              |       |rouge2_max,none        |            41.54|   |      |
|              |       |rouge2_max_stderr,none |             1.05|   |      |
|              |       |rouge2_acc,none        |             0.42|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |             2.52|   |      |
|              |       |rouge2_diff_stderr,none|             1.36|   |      |
|              |       |rougeL_max,none        |            52.36|   |      |
|              |       |rougeL_max_stderr,none |             0.91|   |      |
|              |       |rougeL_acc,none        |             0.44|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |             2.41|   |      |
|              |       |rougeL_diff_stderr,none|             1.27|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.31|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.46|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 45.9%

### hellaswag
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.64|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.83|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 83.15%

Average score: 65.22%

Metadata: {'elapsed_time': '02:39:53', 'gpu': 'NVIDIA A100 80GB PCIe'}

