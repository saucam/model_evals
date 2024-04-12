# saucam/Orpomis-Prime-7B-it results

## nous results 

 |Benchmark|                                 Model                                  |agieval|gpt4all|bigbench|truthfulqa|Average|
|---------|------------------------------------------------------------------------|------:|------:|-------:|---------:|------:|
|nous     |[Orpomis-Prime-7B-it](https://huggingface.co/saucam/Orpomis-Prime-7B-it)|  37.23|  72.28|   38.72|     43.68|  47.98|

### agieval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |22.05|±  |  2.61|
|                              |       |acc_norm|23.23|±  |  2.65|
|agieval_logiqa_en             |      0|acc     |31.80|±  |  1.83|
|                              |       |acc_norm|34.25|±  |  1.86|
|agieval_lsat_ar               |      0|acc     |17.39|±  |  2.50|
|                              |       |acc_norm|17.83|±  |  2.53|
|agieval_lsat_lr               |      0|acc     |40.20|±  |  2.17|
|                              |       |acc_norm|39.80|±  |  2.17|
|agieval_lsat_rc               |      0|acc     |44.61|±  |  3.04|
|                              |       |acc_norm|45.35|±  |  3.04|
|agieval_sat_en                |      0|acc     |58.25|±  |  3.44|
|                              |       |acc_norm|56.31|±  |  3.46|
|agieval_sat_en_without_passage|      0|acc     |45.63|±  |  3.48|
|                              |       |acc_norm|45.15|±  |  3.48|
|agieval_sat_math              |      0|acc     |36.36|±  |  3.25|
|                              |       |acc_norm|35.91|±  |  3.24|

Average: 37.23%

### gpt4all
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |55.89|±  |  1.45|
|             |       |acc_norm|58.53|±  |  1.44|
|arc_easy     |      0|acc     |82.53|±  |  0.78|
|             |       |acc_norm|82.87|±  |  0.77|
|boolq        |      1|acc     |83.76|±  |  0.65|
|hellaswag    |      0|acc     |62.06|±  |  0.48|
|             |       |acc_norm|81.38|±  |  0.39|
|openbookqa   |      0|acc     |33.60|±  |  2.11|
|             |       |acc_norm|43.80|±  |  2.22|
|piqa         |      0|acc     |81.77|±  |  0.90|
|             |       |acc_norm|83.30|±  |  0.87|
|winogrande   |      0|acc     |72.30|±  |  1.26|

Average: 72.28%

### bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|54.74|±  |  3.62|
|bigbench_date_understanding                     |      0|multiple_choice_grade|67.48|±  |  2.44|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|41.86|±  |  3.08|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|22.28|±  |  2.20|
|                                                |       |exact_str_match      | 9.75|±  |  1.57|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|22.60|±  |  1.87|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|15.43|±  |  1.37|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|37.00|±  |  2.79|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|34.40|±  |  2.13|
|bigbench_navigate                               |      0|multiple_choice_grade|50.00|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|56.60|±  |  1.11|
|bigbench_ruin_names                             |      0|multiple_choice_grade|34.15|±  |  2.24|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|23.15|±  |  1.34|
|bigbench_snarks                                 |      0|multiple_choice_grade|62.43|±  |  3.61|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|55.27|±  |  1.58|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|45.20|±  |  1.57|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|22.88|±  |  1.19|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|14.51|±  |  0.84|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|37.00|±  |  2.79|

Average: 38.72%

### truthfulqa
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |29.62|±  |  1.60|
|             |       |mc2   |43.68|±  |  1.49|

Average: 43.68%

Average score: 47.98%

Metadata: {'elapsed_time': '01:33:39', 'gpu': 'NVIDIA RTX 6000 Ada Generation'}

