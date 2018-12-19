import json
from datetime import datetime
from pprint import pprint

with open('229344.json') as f:
    data = json.load(f)

results = {}
for user_id, user_info in data['members'].items():
    user_solutions = {}
    for problem_id, problem_info in user_info['completion_day_level'].items():
        problem_id = int(problem_id)
        user_solutions[problem_id] = {}
        for problem_part, time_completed in problem_info.items():
            problem_part = int(problem_part)
            user_solutions[problem_id][problem_part] = datetime.fromtimestamp(int(time_completed['get_star_ts'])).strftime("%Y-%m-%d_%H:%M")
        results[user_info['name']] = user_solutions

pprint(results)
