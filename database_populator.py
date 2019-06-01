import json
from problems.models import Problem

with open('problems.json') as f:
	problems_json = json.load(f)

for problem in problems_json:
	problem = Problem(oj_name=problem['oj_name'], prob_id=problem['prob_id'], name=problem['name'], category=problem['category'], link=problem['link'])


for problem in problems_json:
	problem = Problem(oj_name=problem['oj_name'], prob_id=problem['prob_id'], name=problem['name'], category=problem['category'], link=problem['link'])
	problem.save()