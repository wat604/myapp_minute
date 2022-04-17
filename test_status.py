from re import S
import sqlite3
from models.status import StatusModel

### find_by_id
# status = StatusModel.find_by_id(1)
# print(status)

### save: insert
# status = StatusModel(None, "2022-04-18", "project3", "new project")
# status.save()

### save: update
# status = StatusModel.find_by_id(1)
# status.description = "description changed"
# status.save()

### delete
status = StatusModel.find_by_id(1)
status.delete()