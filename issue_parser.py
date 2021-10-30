import pandas as pd
import json
import requests


response = requests.get('https://api.github.com/repos/UCSD-CSE-210-2021/cse-210-team-project-fam/issues?per_page=100')
issues = response.json()

issue_dataframe = pd.DataFrame(columns = {
    "Number", "Title", "Body", "Comments", "State", "Updated_at", "URL", "user",
    "Milestone", "Node_id", "Labels", "Updated_at", "Type", "In_story"
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
    issue_dataframe.set_index(issue_dataframe.Number, inplace = True)
    try:
        issue_dataframe.at[issue['number'], 'Type'] = issue['labels'][0]['name']
    except:
        pass
    
    body = issue['body']
    
    try:
        if "TYPE:TASK" in body:
            issue_dataframe.at[issue['number'], 'Type'] = 'Task'
            issue_dataframe.at[issue['number'], 'In_story'] = (
                body[body.find("EPIC:'") + 6 : body.find("'", body.find("EPIC:'") + 7)]
            )
        elif "TYPE:TEST" in body:
            issue_dataframe.at[issue['number'], 'Type'] = 'Test'
            issue_dataframe.at[issue['number'], 'In_story'] = (
                body[body.find("EPIC:'") + 6 : body.find("'", body.find("EPIC:'") + 7)]
            )
    except:
        pass


issue_dataframe[[
        "Number",
        "Title",
        "Body",
        "Type",
        "In_story",
        "Comments",
        "State",
        "Updated_at",
        "URL",
        "Node_id"
    ]].to_excel("./FAM_issue_list.xlsx")

