|                                                     Model                                                     |agieval|gpt4all|bigbench|truthfulqa|Average|
|---------------------------------------------------------------------------------------------------------------|------:|------:|-------:|---------:|------:|
|[bert-tiny-finetuned-sms-spam-detection](https://huggingface.co/mrm8488/bert-tiny-finetuned-sms-spam-detection)|  22.29|  34.67|   29.11|     48.11|  33.55|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |18.90|±  |  2.46|
|                              |       |acc_norm|18.50|±  |  2.44|
|agieval_logiqa_en             |      0|acc     |21.97|±  |  1.62|
|                              |       |acc_norm|25.50|±  |  1.71|
|agieval_lsat_ar               |      0|acc     |20.87|±  |  2.69|
|                              |       |acc_norm|20.87|±  |  2.69|
|agieval_lsat_lr               |      0|acc     |14.71|±  |  1.57|
|                              |       |acc_norm|20.59|±  |  1.79|
|agieval_lsat_rc               |      0|acc     |22.30|±  |  2.54|
|                              |       |acc_norm|17.84|±  |  2.34|
|agieval_sat_en                |      0|acc     |27.67|±  |  3.12|
|                              |       |acc_norm|25.24|±  |  3.03|
|agieval_sat_en_without_passage|      0|acc     |26.21|±  |  3.07|
|                              |       |acc_norm|25.24|±  |  3.03|
|agieval_sat_math              |      0|acc     |24.09|±  |  2.89|
|                              |       |acc_norm|24.55|±  |  2.91|

Average: 22.29%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |22.53|±  |  1.22|
|             |       |acc_norm|26.11|±  |  1.28|
|arc_easy     |      0|acc     |24.92|±  |  0.89|
|             |       |acc_norm|24.58|±  |  0.88|
|boolq        |      1|acc     |37.65|±  |  0.85|
|hellaswag    |      0|acc     |25.84|±  |  0.44|
|             |       |acc_norm|26.34|±  |  0.44|
|openbookqa   |      0|acc     |16.40|±  |  1.66|
|             |       |acc_norm|29.20|±  |  2.04|
|piqa         |      0|acc     |51.20|±  |  1.17|
|             |       |acc_norm|49.51|±  |  1.17|
|winogrande   |      0|acc     |49.33|±  |  1.41|

Average: 34.67%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|49.47|±  |  3.64|
|bigbench_date_understanding                     |      0|multiple_choice_grade| 9.76|±  |  1.55|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|30.23|±  |  2.86|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|10.03|±  |  1.59|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|19.40|±  |  1.77|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|14.43|±  |  1.33|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|34.33|±  |  2.75|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|25.60|±  |  1.95|
|bigbench_navigate                               |      0|multiple_choice_grade|52.30|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|11.10|±  |  0.70|
|bigbench_ruin_names                             |      0|multiple_choice_grade|55.36|±  |  2.35|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|16.83|±  |  1.18|
|bigbench_snarks                                 |      0|multiple_choice_grade|52.49|±  |  3.72|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|49.70|±  |  1.59|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|24.10|±  |  1.35|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|20.08|±  |  1.13|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|14.51|±  |  0.84|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|34.33|±  |  2.75|

Average: 29.11%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |22.52|±  |  1.46|
|             |       |mc2   |48.11|±  |  1.59|

Average: 48.11%

Average score: 33.55%

Metadata: {'elapsed_time': '00:29:33'}

