from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class Task(BaseModel):
    id: int = Field(default_factory=lambda: int(datetime.now().timestamp()))
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    due_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def complete(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now()

    def is_overdue(self) -> bool:
        if not self.due_date or self.status == TaskStatus.COMPLETED:
            return False
        return datetime.now() > self.due_date 