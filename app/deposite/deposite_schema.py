from pydantic import BaseModel, Field, validator
from datetime import datetime


class DepositeSchema(BaseModel):
    date: str = Field(..., description="Дата заявки")
    periods: int = Field(..., ge=1, le=60, description="Количество месяцев по вкладу")
    amount: int = Field(..., ge=10000, le=3000000, description="Сумма вклада")
    rate: float = Field(..., ge=1, le=8, description="Процент по вкладу")

    # @validator("date")
    # def validate_date_range(cls, date):
    #     if not validate_date(date):
    #         raise ValueError("error: Date must be in the format dd.mm.YYYY")
    #     return date

    class Config:
        from_attributes = True
