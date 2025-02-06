from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session
from datetime import datetime

import enum


class Grades(enum.Enum):
    # The higher number equal higher Grade
    Grade1 = 1
    Grade2 = 2
    Grade3 = 3
    Grade4 = 4
    Grade5 = 5
    Grade6 = 6
    Grade7 = 7
    Grade8 = 8


class Employee(SQLModel, table=True):
    __tablename__ = "Employees"
    id: int = Field(default=None, primary_key=True)
    Name: str
    Employee_number: str
    PhoneNumber: str
    Department_id:int=Field(default=None, foreign_key="Departments.id")   
    Address: str
    PostalCode: str
    Grade: Grades 
    Email: str
    IsAuditor: bool=Field(default=False)
    IBAN: str
    Bank: str
    

class Given_status(enum.Enum):
    undamaged = 1
    fully_damag = 2
    low_damge = 3
    high_damge = 4

class Returned_status(enum.Enum):
    undamaged = 1
    fully_damag = 2
    low_damge = 3
    high_damge = 4



class Assets_Allocation(SQLModel, table=True):
    __tablename__ = "Assets_Allocations"
    id: int = Field(default=None, primary_key=True)
    Asset_id:int=Field(default=None, foreign_key="Asset_Inventory.id")
    Employee_id: int=Field(default=None, foreign_key="Employees.id")
    Auditor_id: int=Field(default=None, foreign_key="Auditors_user.id")
    Department_id:Optional[int]=Field(default=None, foreign_key="Departments.id")   
    Quantity: int
    Unrecived_Quantity: int
    Allocation_Date: datetime =Field(default_factory=datetime.now)
    IsReturned: bool=Field(default=False)
    Return_Date:Optional[str] = Field(default_factory=None)
    Note: Optional[str] 
    Suggested_ReturnDate: str
    Given_status: Given_status
    Returned_status: Optional[Returned_status]

class LoanType(enum.Enum):
    Work=1
    Personal=2

class TypeOfDeposit(enum.Enum):
    Cash = 1
    BankTransfer=2

    
class Currency(enum.Enum):
    SaudiRiyal = 1
    Dollar = 2
    Euro = 3


class FinancialLoan(SQLModel, table=True):
    __tablename__ = "financial_loans"
    id: int = Field(default=None, primary_key=True)
    Employee_id: int=Field(default=None, foreign_key="Employees.id")
    Auditor_id: int=Field(default=None, foreign_key="Auditors_user.id")
    Amount: int
    Currency: Currency
    Timestamp: datetime =Field(default_factory=datetime.now)
    Loan_type: LoanType
    Type_of_deposit: TypeOfDeposit
    Paidinfull: bool=Field(default=False)
    

class Payment_method(enum.Enum):
    Catch_Receipt=1
    Cash=2
    Bills= 3
    BankTransfer= 4

class Loan_payment(SQLModel, table=True):
    __tablename__ = "Loan payments"
    id: int = Field(default=None, primary_key=True)
    Employee_id: int=Field(default=None, foreign_key="Employees.id")
    Loan_id: int=Field(default=None, foreign_key="financial_loans.id")
    Auditor_id: int=Field(default=None, foreign_key="Auditors_user.id")
    Amount: int
    Time_stamp: datetime = Field(default_factory=datetime.now)
    Payment_method: Payment_method
    Note:Optional[str]



class Auditors_user(SQLModel, table=True):
    __tablename__ = "Auditors_user"
    id: int = Field(default=None, primary_key=True)
    Employee_id: int=Field(default=None, foreign_key="Employees.id",unique=True)
    User_name: str
    Enc_password: str
    Login_status: bool=Field(default=False)
    Admin_check: bool=Field(default=False)

class Department(SQLModel,table=True):
    __tablename__ = "Departments"
    id: int = Field(default=None, primary_key=True)
    Name:str
    Manager_id:Optional[int]=Field(default=None, foreign_key="Employees.id")

class Asset_Inventory(SQLModel,table=True):
    __tablename__ = "Asset_Inventory"
    id:int = Field(default=None, primary_key=True)
    Name:str
    Description:str
    Serial_number:str
    Money_value:int
    Quantity:int
    Location:str


engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)
