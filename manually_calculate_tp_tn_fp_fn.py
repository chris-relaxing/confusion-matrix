
def manually_calculate_tp_tn_fp_fn(test_y, test_predictions):
    """Manually create confusion matrix by comparing predictions with answers."""
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    x = 0
    while x < len(test_y):
        if test_y[x] == 0 and test_predictions[x] == 0:
            TN += 1
        if test_y[x] == 0 and test_predictions[x] == 1:
            FP += 1
        if test_y[x] == 1 and test_predictions[x] == 1:
            TP += 1
        if test_y[x] == 1 and test_predictions[x] == 0:
            FN += 1
        x += 1

    cm = [[TN, FP],[FN, TP]]
    return cm

