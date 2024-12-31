#вывод даты в определённом формате

from greetings import created_date, issue_date

temp_issue_date = issue_date[0:5]
temp_created_date = created_date[0:5]

print(f"Дата создания заметки: {temp_created_date}\n"
      f"Дата истечения заметки: {temp_issue_date}")
