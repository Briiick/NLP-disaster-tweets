import pandas as pd

def kaggle_submit(predictions, submission_str):
    """
    input predictions and string label
    output to submissions
    """
    submission = pd.read_csv("../data/submissions/submission.csv")
    submission["target"] = predictions
    submission.to_csv('../data/submissions/'+submission_str, index=False)