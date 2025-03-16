import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from .models import Task

class StorageManager:
    def __init__(self, storage_file: Optional[str] = None):
        if storage_file is None:
            config_dir = os.path.join(str(Path.home()), ".terminal_task_manager")
            os.makedirs(config_dir, exist_ok=True)
            storage_file = os.path.join(config_dir, "tasks.json")
        self.storage_file = storage_file
        self._ensure_storage_file()

    def _ensure_storage_file(self) -> None:
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, "w") as f:
                json.dump([], f)

    def _serialize_datetime(self, obj: datetime) -> str:
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    def _deserialize_task(self, task_dict: Dict) -> Task:
        if task_dict.get("due_date"):
            task_dict["due_date"] = datetime.fromisoformat(task_dict["due_date"])
        if task_dict.get("created_at"):
            task_dict["created_at"] = datetime.fromisoformat(task_dict["created_at"])
        if task_dict.get("completed_at"):
            task_dict["completed_at"] = datetime.fromisoformat(task_dict["completed_at"])
        return Task(**task_dict)

    def save_tasks(self, tasks: List[Task]) -> None:
        with open(self.storage_file, "w") as f:
            json.dump(
                [task.model_dump() for task in tasks],
                f,
                default=self._serialize_datetime,
                indent=2
            )

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.storage_file, "r") as f:
                tasks_data = json.load(f)
                return [self._deserialize_task(task_dict) for task_dict in tasks_data]
        except json.JSONDecodeError:
            return []

    def add_task(self, task: Task) -> None:
        tasks = self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)

    def update_task(self, task: Task) -> bool:
        tasks = self.load_tasks()
        for i, t in enumerate(tasks):
            if t.id == task.id:
                tasks[i] = task
                self.save_tasks(tasks)
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        tasks = self.load_tasks()
        initial_length = len(tasks)
        tasks = [t for t in tasks if t.id != task_id]
        if len(tasks) != initial_length:
            self.save_tasks(tasks)
            return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        tasks = self.load_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        return None 