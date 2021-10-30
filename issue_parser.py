import pandas as pd
import json
import requests


response = requests.get('https://api.github.com/repos/UCSD-CSE-210-2021/cse-210-team-project-fam/issues')
issues = response.json()

issue_dataframe = pd.DataFrame(columns = {
    "Number", "Title", "Body", "Comments", "State", "Updated_at", "URL", "user",
    "Milestone", "Node_id", "Labels", "Updated_at"
    })

for issue in issues:
    issue_dataframe = issue_dataframe.append(
        {
            "Number" : issue['number'],
            "Title"  : issue['title'],
            "Body"   : issue['body'],
            "Comments" : issue['comments'],
            "State"    : issue['state'],
            "Updated_at" : issue['updated_at'],
            "URL"        : issue['url'],
            "user"       : issue['user'],
            "Milestone"  : issue['milestone'],
            "Node_id"    : issue['node_id'],
            "Labels"     : issue['labels']
        },
        ignore_index = True
    )
    

issue_dataframe[[
        "Number",
        "Title",
        "Body",
        "Comments",
        "State",
        "Updated_at",
        "URL",
        "Node_id"
    ]].to_excel("./FAM_issue_list.xlsx")
