# mrm8488/bert-tiny-finetuned-sms-spam-detection results

## nous results 

 |Benchmark|                                                     Model                                                     |agieval|bigbench|gpt4all|truthfulqa|Average|
|---------|---------------------------------------------------------------------------------------------------------------|------:|-------:|------:|---------:|------:|
|nous     |[bert-tiny-finetuned-sms-spam-detection](https://huggingface.co/mrm8488/bert-tiny-finetuned-sms-spam-detection)|  22.95|   28.75|  36.07|     48.09|  33.97|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |20.87|±  |  2.55|
|                              |       |acc_norm|21.26|±  |  2.57|
|agieval_logiqa_en             |      0|acc     |22.43|±  |  1.64|
|                              |       |acc_norm|26.88|±  |  1.74|
|agieval_lsat_ar               |      0|acc     |19.13|±  |  2.60|
|                              |       |acc_norm|20.87|±  |  2.69|
|agieval_lsat_lr               |      0|acc     |14.90|±  |  1.58|
|                              |       |acc_norm|21.57|±  |  1.82|
|agieval_lsat_rc               |      0|acc     |21.19|±  |  2.50|
|                              |       |acc_norm|15.61|±  |  2.22|
|agieval_sat_en                |      0|acc     |26.70|±  |  3.09|
|                              |       |acc_norm|26.21|±  |  3.07|
|agieval_sat_en_without_passage|      0|acc     |25.24|±  |  3.03|
|                              |       |acc_norm|25.73|±  |  3.05|
|agieval_sat_math              |      0|acc     |24.09|±  |  2.89|
|                              |       |acc_norm|25.45|±  |  2.94|

Average: 22.95%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|47.89|±  |  3.63|
|bigbench_date_understanding                     |      0|multiple_choice_grade| 9.49|±  |  1.53|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|30.23|±  |  2.86|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|10.03|±  |  1.59|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|19.60|±  |  1.78|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|14.57|±  |  1.33|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|33.67|±  |  2.73|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|27.80|±  |  2.01|
|bigbench_navigate                               |      0|multiple_choice_grade|48.90|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|13.45|±  |  0.76|
|bigbench_ruin_names                             |      0|multiple_choice_grade|54.24|±  |  2.36|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|16.83|±  |  1.18|
|bigbench_snarks                                 |      0|multiple_choice_grade|45.86|±  |  3.71|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|49.70|±  |  1.59|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|27.10|±  |  1.41|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|20.16|±  |  1.14|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|14.29|±  |  0.84|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|33.67|±  |  2.73|

Average: 28.75%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |22.18|±  |  1.21|
|             |       |acc_norm|25.85|±  |  1.28|
|arc_easy     |      0|acc     |25.08|±  |  0.89|
|             |       |acc_norm|24.03|±  |  0.88|
|boolq        |      1|acc     |47.86|±  |  0.87|
|hellaswag    |      0|acc     |25.69|±  |  0.44|
|             |       |acc_norm|26.31|±  |  0.44|
|openbookqa   |      0|acc     |17.40|±  |  1.70|
|             |       |acc_norm|29.60|±  |  2.04|
|piqa         |      0|acc     |52.12|±  |  1.17|
|             |       |acc_norm|49.40|±  |  1.17|
|winogrande   |      0|acc     |49.41|±  |  1.41|

Average: 36.07%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |22.52|±  |  1.46|
|             |       |mc2   |48.09|±  |  1.59|

Average: 48.09%

Average score: 33.97%

Metadata: {'elapsed_time': '02:32:24', 'gpu': 'NVIDIA GeForce RTX 4090'}

