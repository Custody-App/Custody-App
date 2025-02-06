from sqlmodel import Session
from datetime import datetime 
from sqlalchemy import or_

from Data_modeling import *

from encpass import hashpassword


class AssetsOfAllocations:
    @staticmethod
    def add( employee_id:int ,auditor_id: int,assest_id:int,quantity:int,note:str, given_status: Given_status,suggestedReturnDate:str,department_id:int):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        Assests = Assets_Allocation(Department_id=department_id ,Employee_id=employee_id, Auditor_id=auditor_id,Asset_id=assest_id, Quantity=quantity, Allocation_Date=timestamp,  Note=note,Given_status=given_status,Suggested_ReturnDate=suggestedReturnDate,Unrecived_Quantity=quantity)
        
        with Session(engine) as session:
            session.add(Assests)
            asset_inventory = session.query(Asset_Inventory).filter(Asset_Inventory.id == assest_id).first()
            if asset_inventory:
                new_quantity = asset_inventory.Quantity - quantity
                asset_inventory.Quantity = new_quantity
                session.commit()
                return True, Assests
            else:
                error_message = "Asset inventory is not found"
                return False, error_message
            
    @staticmethod
    def edit(id: int, data: dict):
        with Session(engine) as session:
            Assest = session.query(Assets_Allocation).filter(Assets_Allocation.id == id).first()
        
            for key, value in data.items():
                if key == 'IsReturned' and value:
                    setattr(Assest, 'Return_Date', datetime.now())
                if hasattr(Assest, key):  
                    setattr(Assest, key, value) 
                else:
                    raise ValueError(f"Assest object has no field '{key}'")

            session.commit()
    @staticmethod
    def search(search_query: str):
        with Session(engine) as session:
            Assets = session.query(Assets_Allocation).join(Employee, Assets_Allocation.Employee_id == Employee.id).join(Department, Assets_Allocation.Department_id == Department.id, isouter=True).join(Asset_Inventory, Assets_Allocation.Asset_id == Asset_Inventory.id).filter(
                or_(
                    Assets_Allocation.Quantity.like(f"%{search_query}%"),
                    Assets_Allocation.Given_status.like(f"%{search_query}%"),
                    Assets_Allocation.Returned_status.like(f"%{search_query}%"),
                    Assets_Allocation.Allocation_Date.like(f"%{search_query}%"),
                    Assets_Allocation.Suggested_ReturnDate.like(f"%{search_query}%"),
                    Assets_Allocation.Note.like(f"%{search_query}%"),
                    Assets_Allocation.Return_Date.like(f"%{search_query}%"),
                    Employee.Name.like(f"%{search_query}%"),  
                    Employee.Employee_number.like(f"%{search_query}%"),
                    Department.Name.like(f"%{search_query}%"),  
                    Asset_Inventory.Name.like(f"%{search_query}%")  
                )
            ).all()

            filtered_Assets = []
            for asset in Assets :
                employee_id = asset.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                department = session.query(Department).filter(Department.id == asset.Department_id).first()                 
                assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()

                if department :
                    department_name=department.Name 
                else:
                    department_name = "No Department"  
                filtered_Assets.append([asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status])
            return filtered_Assets

class AssetInventory:
    @staticmethod
    def add(name: str, description: str, serial_number: str, money_value: int, quantity: int, location: str):

        Asset_INV = Asset_Inventory(Name=name , Description=description,Serial_number=serial_number,Money_value=money_value,Quantity=quantity,Location=location)
        with Session(engine) as session:
            session.add(Asset_INV)
            session.commit()

    @staticmethod
    def edit(id: int, data: dict):
        with Session(engine) as session:
            Asset_INV = session.query(Asset_Inventory).filter(Asset_Inventory.id == id).first()

            for key, value in data.items():
                if hasattr(Asset_INV, key):
                    setattr(Asset_INV, key, value)

                else:
                    raise ValueError(f"AssetInventory object has no field '{key}'")

            session.commit()

    @staticmethod
    def search(search_query: str):
        with Session(engine) as session:
            inventorys = session.query(Asset_Inventory).filter(
                or_(
                    Asset_Inventory.Name.like(f"%{search_query}%"),
                    Asset_Inventory.Description.like(f"%{search_query}%"),
                    Asset_Inventory.Serial_number.like(f"%{search_query}%"),
                    Asset_Inventory.Money_value.like(f"%{search_query}%"),
                    Asset_Inventory.Quantity.like(f"%{search_query}%"),
                    Asset_Inventory.Location.like(f"%{search_query}%"),

                )
            ).all()

            filtered_inventroy = []
            for inventory in inventorys:
                filtered_inventroy.append([inventory.id,inventory.Name,inventory.Description,inventory.Serial_number,inventory.Quantity,inventory.Money_value,inventory.Location])
            return filtered_inventroy            


class Financial_Loan:
    @staticmethod
    def add(employee_id: int, auditor_id: int, amount: int, currency: Currency, loan_type: LoanType, type_of_deposit: TypeOfDeposit, paid_in_full: bool):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        financial = FinancialLoan(Employee_id=employee_id, Auditor_id=auditor_id, Amount=amount, Currency=currency, Timestamp=timestamp, Loan_type=loan_type, Type_of_deposit=type_of_deposit, Paidinfull=paid_in_full)
        with Session(engine) as session:
            session.add(financial)
            session.commit()


    @staticmethod
    def edit(id: int, data: dict):
        with Session(engine) as session:
            loan = session.query(FinancialLoan).filter(FinancialLoan.id == id).first()

            for key, value in data.items():
                if hasattr(loan, key):
                    setattr(loan, key, value)

                else:
                    raise ValueError(f"FinancialLoan object has no field '{key}'")

            session.commit()
    @staticmethod
    def search(search_query: str):
        with Session(engine) as session:
            loans = session.query(FinancialLoan).join(Employee, FinancialLoan.Employee_id == Employee.id).filter(
                or_(
                    FinancialLoan.Employee_id.like(f"%{search_query}%"),
                    FinancialLoan.Amount.like(f"%{search_query}%"),
                    FinancialLoan.Auditor_id.like(f"%{search_query}%"),
                    FinancialLoan.Currency.like(f"%{search_query}%"),
                    FinancialLoan.Loan_type.like(f"%{search_query}%"),
                    FinancialLoan.Type_of_deposit.like(f"%{search_query}%"),
                    Employee.Name.like(f"%{search_query}%"),  
                    Employee.Employee_number.like(f"%{search_query}%")  
                )
            ).all()

            filtered_loans = []
            for loan in loans:
                employee_id = loan.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()
            
                filtered_loans.append([loan.id ,employee.Name, employee.Employee_number, loan.Amount, loan.Currency, loan.Timestamp, loan.Loan_type, loan.Type_of_deposit, loan.Paidinfull])       
            return filtered_loans



class Auditor:
    @staticmethod
    def add(employee_id: int,user_name: str,enc_password: str,admin_check: bool):
        hashed_password = hashpassword(enc_password)

        auditor= Auditors_user(Employee_id=employee_id,User_name=user_name,Enc_password=hashed_password,Admin_check=admin_check)

        with Session(engine) as session:
            session.query(Employee).filter(Employee.id == employee_id).update({"IsAuditor": True})
            session.add(auditor)
            session.commit()
   
   
    @staticmethod
    def login(user_name: str, password: str):
        with Session(engine) as session:
            auditors_user = session.query(Auditors_user).filter(Auditors_user.User_name == user_name).first()

        if auditors_user:
            stored_password = auditors_user.Enc_password
            hashed_password = hashpassword(password)

            if stored_password and hashed_password == stored_password:
                auditor_employee = session.query(Employee).filter(Employee.id == auditors_user.Employee_id, Employee.IsAuditor == True).first()
                auditors_user.Login_status = True
                session.add(auditors_user)
                session.commit()

                if auditor_employee:
                    welcome_message = f"Welcome {auditor_employee.Name} Employee number: {auditor_employee.Employee_number}"
                    return welcome_message, auditors_user

        return False, None

    @staticmethod
    def logout(user_name: str):
        with Session(engine) as session:
            auditors_user = session.query(Auditors_user).filter(Auditors_user.User_name == user_name).first()

            if auditors_user:
                auditors_user.Login_status = False
                session.add(auditors_user)
                session.commit()
                return True

        return False
    
    def edit(id: int, data: dict):
        with Session(engine) as session:
            auditor = session.query(Auditors_user).filter(Auditors_user.id == id).first()
            
            if auditor:
                for key, value in data.items():
                    if hasattr(auditor, key): 
                        setattr(auditor, key, value)
                    else:
                        raise ValueError(f"Auditor object has no field '{key}'")

                session.commit()



class Employees:
    @staticmethod
    def add(name: str, employee_number: str, phoneNumber: str, department_id:int, address: str, postalCode: str, Grade: Grades, email: str,iBAN: str, bank: str, isAduitor: bool):
        employee = Employee(Name=name,Employee_number=employee_number,PhoneNumber=phoneNumber,Department_id=department_id,Address=address,PostalCode=postalCode,Grade=Grade,Email=email,IBAN=iBAN,Bank=bank,IsAuditor=isAduitor)

        with Session(engine) as session:
            session.add(employee)
            session.commit()

    @staticmethod
    def edit(id: int, data: dict):
        with Session(engine) as session:
            employee = session.query(Employee).filter(Employee.id == id).first()
            
            if employee:
                for key, value in data.items():
                    if hasattr(employee, key): 
                        setattr(employee, key, value)
                    else:
                        raise ValueError(f"Employee object has no field '{key}'")

                session.commit()
            else:
                raise ValueError(f"Employee with ID '{id}' not found")

    @staticmethod
    def search(search_query: str):
        with Session(engine) as session:
            employees = session.query(Employee).join(Department, Employee.Department_id == Department.id).filter(
                or_(
                    Employee.Employee_number.like(f"%{search_query}%"),
                    Employee.Name.like(f"%{search_query}%"),
                    Employee.PhoneNumber.like(f"%{search_query}%"),
                    Employee.Address.like(f"%{search_query}%"),
                    Employee.PostalCode.like(f"%{search_query}%"),
                    Employee.Grade.like(f"%{search_query}%"),
                    Employee.Email.like(f"%{search_query}%"),
                    Employee.IBAN.like(f"%{search_query}%"),
                    Employee.Bank.like(f"%{search_query}%"),
                    Department.Name.like(f"%{search_query}%")

                )
            ).all()

            filtered_employees = []
            for employee in employees:
                department_id = employee.Department_id
                department = session.query(Department).filter(Department.id == department_id).first() 

                filtered_employees.append([employee.id, employee.Name, employee.Employee_number, employee.PhoneNumber,department.Name, employee.Address, employee.PostalCode, employee.Grade,employee.Email, employee.IsAuditor, employee.IBAN, employee.Bank])
               
            return filtered_employees

    @staticmethod
    def delete( id: int):
        with Session(engine) as session:

            employee = session.get(Employee, id)
            if employee:
                session.delete(employee)
                session.commit()
            else:
                raise ValueError(f"Employee with ID '{id}' not found")


class Departments:
    @staticmethod
    def add(name: str,manager_id: int):

        department = Department(Name=name, Manager_id=manager_id)
        with Session(engine) as session:
            session.add(department)
            session.commit()
            


class Payment:

    @staticmethod
    def add(employee_id: int, loan_id: int, auditor_id: int, amount: int, PaymentMethod: Payment_method,note:str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Payed = Loan_payment(Employee_id=employee_id,Loan_id=loan_id,Auditor_id=auditor_id,Amount=amount,Time_stamp=timestamp,Payment_method=PaymentMethod,Note=note)
        with Session(engine) as session:
            session.add(Payed)

            loan = session.query(FinancialLoan).filter(FinancialLoan.id == loan_id).first()
            if loan:
                new_amount = loan.Amount - int(amount)
                if new_amount < 0:
                 error_message = "Payment amount exceeds the loan amount"
                 return False, error_message
                elif new_amount == 0:
                    loan.Paidinfull = True
                loan.Amount = new_amount
                session.commit()
                return True, None
            else:
                    error_message = "Financial loan is not found"
                    return False, error_message

    @staticmethod
    def search(search_query: str):
        with Session(engine) as session:
            loan_payments = session.query(Loan_payment).join(Employee, Employee.id == Loan_payment.Employee_id).filter(
                or_(
                    Loan_payment.Time_stamp.like(f"%{search_query}%"),
                    Loan_payment.Amount.like(f"%{search_query}%"),
                    Loan_payment.Payment_method.like(f"%{search_query}%"),
                    Loan_payment.Note.like(f"%{search_query}%"),
                    Employee.Name.like(f"%{search_query}%"),  
                    Employee.Employee_number.like(f"%{search_query}%")  
                )
            ).all()

            filtered_payments = []
            for payment in loan_payments:
                employee_id = payment.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()                
                filtered_payments.append([payment.id, employee.Name, employee.Employee_number, payment.Amount, payment.Time_stamp, payment.Payment_method, payment.Note])
            return filtered_payments
