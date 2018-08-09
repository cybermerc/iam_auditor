import json
import numpy as np

iam_calls = []

with open ('temp.logs', 'r') as f:
    logstore = json.load(f)

for items in logstore:
    details = items["protoPayload"]["authorizationInfo"]

    for calls in details:
        iam_calls.append(calls["permission"])

x = np.array(iam_calls)
unique, counts = np.unique(x, return_counts=True)
r = np.asarray((unique, counts)).T

for k, v in r:
    print k, v
