from PyQt5 import QtCore, QtGui, QtWidgets
from sqlmodel import Session

from LoginPage import LoginPage
from ProgramMainWindow import ProgramMainWindow
from data_opersion import *
from Data_modeling import *
from datetime import datetime 
from RuternPage import RuternPage
from Localization import TranslationData, Translateion

import codecs
import sys
import resources

class MyApp:
    def __init__(self):
        self.qapp =QtWidgets.QApplication(sys.argv)
        self.login_window = LoginPage()
        self.main_window = ProgramMainWindow()
        self.inventroy_page=RuternPage()
        self.current_language = 0
        self.Int_type=QtGui.QIntValidator()
        self.apply_dark_mode()
        self.populate_combo_boxes()
        self.setup_connections()
        self.validate_data()
        self.load_data()
        self.qapp_icon =QtGui.QIcon(":/icon.png") 
        self.main_window.setWindowTitle("Custody App")
        self.main_window.setWindowIcon(self.qapp_icon)
        self.login_window.setWindowTitle("Custody App")
        self.login_window.setWindowIcon(self.qapp_icon)
        self.inventroy_page.setWindowTitle("Custody App")
        self.inventroy_page.setWindowIcon(self.qapp_icon)
        self.trayIcon =QtWidgets.QSystemTrayIcon(self.qapp_icon)
        self.trayIcon.setToolTip('Exit')
        self.trayIcon.show()
        self.menu =QtWidgets.QMenu()
        self.exitAction = self.menu.addAction('Exit')
        self.exitAction.triggered.connect(self.qapp.quit)
        self.trayIcon.setContextMenu(self.menu)
        
    def handleLanguageChange(self, state):
            if state == QtCore.Qt.Checked:
                lang = 1
            else:
                lang = 0
            self.current_language=lang
            self.translate_ui(lang)
            self.populate_combo_boxes(lang)


    def translate_ui(self, lang):
        
        self.main_window.label_4.setText(Translateion('Adding Auditor', lang))
        self.main_window.Edit_Auditor_manging_.setText(Translateion('Save', lang))
        self.main_window.Return_EditAuditor_Mange_.setText(Translateion('Return', lang))
        self.main_window.AuditorManginigPageEdit_EncPassword_TXT_.setPlaceholderText(Translateion('Password', lang))
        self.main_window.Admin_checkEdit_Checkbox_.setText(Translateion('Admin Check', lang))
        self.main_window.Auditor_Edit_butt.setText(Translateion('Edit', lang))
        self.inventroy_page.label_inventory_quantity.setText(Translateion('Quantity', lang))
        self.inventroy_page.label_Inventory_returnstate.setText(Translateion('Return State', lang))
        self.inventroy_page.Inventory_page_ReturnItem.setText(Translateion('Return Item', lang))
        self.inventroy_page.Inventory_page_cancelbutt.setText(Translateion('Cancel', lang))
        self.main_window.label_10.setText(Translateion('Notes', lang))
        self.main_window.label_11.setText(Translateion('Notes', lang))
        self.main_window.EmployeeUsersnButton.setText(Translateion('Users', lang))
        self.main_window.RESET_butt.setText(Translateion('Reset', lang))
        self.main_window.RESET_butt.setToolTip(Translateion('By pressing this button, all recordes will be reset.', lang))
        self.main_window.EmployeeMainPage_Department_butt.setText(Translateion('Department', lang))
        self.main_window.EmployeeMainPage_edit_butt.setText(Translateion('Edit', lang))
        self.main_window.EmployeeMainPage_remove_butt.setText(Translateion('Remove', lang))
        self.main_window.Employee_recodes.setText(Translateion('Employees Records', lang))
        self.main_window.EmployeeMainPage_add_butt.setText(Translateion('Add', lang))
        self.main_window.AddEmployeePage_Add_butt.setText(Translateion('Add', lang))
        self.main_window.label_3.setText(Translateion('Department', lang))
        self.main_window.Employee_recodes_2.setText(Translateion('Department Record',lang))
        self.main_window.label_5.setText(Translateion('Grade', lang))
        self.main_window.AddEmployeePage_Return_butt.setText(Translateion('Return', lang))
        self.main_window.EditEmployeePage_Save_butt_.setText(Translateion('Save', lang))
        self.main_window.Edit_ReturnEmployee_.setText(Translateion('Return', lang))
        self.main_window.label_8.setText(Translateion('Department', lang))
        self.main_window.label_7.setText(Translateion('Grade', lang))
        self.main_window.AuditorPage_add_butt.setText(Translateion('Add', lang))
        self.main_window.Auditor_Return_butt.setText(Translateion('Return', lang))
        self.main_window.Admin_check_Checkbox.setText(Translateion('Admin Check', lang))
        self.main_window.Add_Auditor_manging.setText(Translateion('Add', lang))
        self.main_window.Return_Auditor_Mange.setText(Translateion('Return', lang))
        self.main_window.Logout.setText(Translateion('Logout', lang))
        self.main_window.AssetsRecordsPage_add_butt.setText(Translateion('Add', lang))
        self.main_window.AssetsRecordsPage_edit_butt.setText(Translateion('Edit', lang))
        self.main_window.AssetsRecordsPage_IsReturn_butt_.setText(Translateion('Return Item', lang))
        self.main_window.AssetsAddingPage_add_butt_.setText(Translateion('Add', lang))
        self.main_window.AssetsAddingPage_return_butt_.setText(Translateion('Return', lang))
        self.main_window.AssetsEditPage_save_butt_.setText(Translateion('Save', lang))
        self.main_window.AssetsEditPage_return_butt_.setText(Translateion('Return', lang))
        self.main_window.PaymentAddingPage_pay_butt.setText(Translateion('Pay', lang))
        self.main_window.LoansRecordsPage_Pay_butt_.setText(Translateion('AddingPayment', lang))
        self.main_window.PaymentAddingPage_Return_butt.setText(Translateion('Return', lang))
        self.main_window.label_25.setText(Translateion('Given State', lang))
        self.main_window.label_27.setText(Translateion('Given State', lang))
        self.main_window.label_26.setText(Translateion('Object Name', lang))
        self.main_window.label_22.setText(Translateion('Quantity', lang))
        self.main_window.label_23.setText(Translateion('Suggested Return date', lang))
        self.main_window.label_24.setText(Translateion('Suggested Return date', lang))
        self.main_window.label_17.setText(Translateion('Loan Type', lang))
        self.main_window.label_2.setText(Translateion('Payment Method', lang))
        self.main_window.label_16.setText(Translateion('Currency', lang))
        self.main_window.label_6.setText(Translateion('Amount', lang))
        self.main_window.LoansRecordsPage_Add_butt_.setText(Translateion('Add', lang))
        self.main_window.LoansRecordsPage_edit_butt.setText(Translateion('Edit', lang))
        self.main_window.label_12.setText(Translateion('Currency', lang))
        self.main_window.label_13.setText(Translateion('Loan Type', lang))
        self.main_window.label.setText(Translateion('Type of deposit', lang))
        self.main_window.LoansAddingTab_add_butt.setText(Translateion('Add', lang))
        self.main_window.LoansAddingTab_Return_butt.setText(Translateion('Return', lang))
        self.main_window.label_18.setText(Translateion('Type of deposit', lang))
        self.main_window.label_19.setText(Translateion('Amount', lang))
        self.main_window.label_16.setText(Translateion('Currency', lang))
        self.main_window.label_17.setText(Translateion('Loan Type', lang))
        self.main_window.LoanseditTab_save_butt_.setText(Translateion('Save', lang))
        self.main_window.Loans_editTab_Return_butt_.setText(Translateion('Return', lang))
        self.main_window.EmployeeMainPage_search_txt.setPlaceholderText(Translateion('Employee Information', lang))
        self.main_window.PaymentRecordsPage_search_txt.setPlaceholderText(Translateion('Payment Information', lang))
        self.main_window.AssetsRecordsPage_search_txt.setPlaceholderText(Translateion('Objects Information', lang))
        self.main_window.LoansRecordsPage_search_txt.setPlaceholderText(Translateion('Loan Information', lang))
        self.main_window.AddEmployeePage_Name_txt.setPlaceholderText(Translateion('Name', lang))
        self.main_window.AddEmployeePage_Employeenumber_txt.setPlaceholderText(Translateion('Employee Number', lang))
        self.main_window.AddEmployeePage_Postalcode_txt.setPlaceholderText(Translateion('Postal Code', lang))
        self.main_window.AddEmployeePage_Address_txt.setPlaceholderText(Translateion('Address', lang))
        self.main_window.AddEmployeePage_Phone_txt.setPlaceholderText(Translateion('Phone', lang))
        self.main_window.AddEmployeePage_IBAN_txt.setPlaceholderText(Translateion('IBAN', lang))
        self.main_window.AddEmployeePage_Bank_txt.setPlaceholderText(Translateion('Bank', lang))
        self.main_window.AddEmployeePage_Email_txt.setPlaceholderText(Translateion('Email', lang))
        self.main_window.Edit_EmployeePage_Name_txt_.setPlaceholderText(Translateion('Name', lang))
        self.main_window.EditEmployeePage_Employeenumber_txt_.setPlaceholderText(Translateion('Employee Number', lang))
        self.main_window.EditEmployeePage_Postalcode_txt_.setPlaceholderText(Translateion('Postal Code', lang))
        self.main_window.Edit_EmployeePage_Address_txt_.setPlaceholderText(Translateion('Address', lang))
        self.main_window.EditEmployeePage_Phone_txt_.setPlaceholderText(Translateion('Phone', lang))
        self.main_window.EditEmployeePage_IBAN_txt_.setPlaceholderText(Translateion('IBAN', lang))
        self.main_window.EditEmployeePage_Bank_txt_.setPlaceholderText(Translateion('Bank', lang))
        self.main_window.EditEmployeePage_Email_txt.setPlaceholderText(Translateion('Email', lang))
        self.main_window.AuditorManginigPage_EmployeeNumber_TXT.setPlaceholderText(Translateion('EmployeeID', lang))
        self.main_window.AuditorManginigPage_USERNAME_TXT.setPlaceholderText(Translateion('Username', lang))
        self.main_window.AuditorManginigPage_EncPassword_TXT.setPlaceholderText(Translateion('EncPassword', lang))
        self.main_window.PaymentAddingPage_Amount_txt.setPlaceholderText(Translateion('Amount', lang))
        self.login_window.Login_butt_login.setText(Translateion('Login', lang))
        self.login_window.Pass_txt_login.setPlaceholderText(Translateion('Password', lang))
        self.login_window.label_2023.setText(Translateion('Login', lang))
        self.login_window.checkBox_Arabic.setText(Translateion('Arabic', lang))
        self.login_window.User_txt_login.setPlaceholderText(Translateion('Username', lang))
        self.main_window.Inventory_AddingTable_Add_butt_.setText(Translateion('Add', lang))
        self.main_window.Inventory_AddingTable_Edit_butt_.setText(Translateion('Edit', lang))
        self.main_window.DepartemntTable_Add_butt.setText(Translateion('Add', lang))
        self.main_window.DepartemntTable_Return_butt.setText(Translateion('Return', lang))
        self.main_window.label_21.setText(Translateion('Quantity', lang))
        self.main_window.label_36.setText(Translateion('Quantity', lang))
        self.main_window.Depatrment_add_butt_.setText(Translateion('Add', lang))
        self.main_window.Departemnt_return_butt_.setText(Translateion('Return', lang))
        self.main_window.Inventory_Edit__Save_butt_.setText(Translateion('Save', lang))
        self.main_window.Inventory_Edit__Return_butt_.setText(Translateion('Return', lang))
        self.main_window.InventoryEdit_ObjectName_Assets_.setPlaceholderText(Translateion('Name', lang))
        self.main_window.InventoryEditDescription_Assets_.setPlaceholderText(Translateion('Description', lang))
        self.main_window.InventoryEditSerialNumber_Assets_.setPlaceholderText(Translateion('Serial Number', lang))
        self.main_window.InventoryEditLocation_Assets_.setPlaceholderText(Translateion('Location', lang))
        self.main_window.InventoryEditMoneyValue_Assets_.setPlaceholderText(Translateion('MoneyValue', lang))
        self.main_window.InventoryAddingMoneyValue_Assets_.setPlaceholderText(Translateion('MoneyValue', lang))
        self.main_window.InventoryAdding_ObjectName_Assets_.setPlaceholderText(Translateion('Name', lang))
        self.main_window.InventoryAddingLocation_Assets_.setPlaceholderText(Translateion('Location', lang))
        self.main_window.InventoryAddingDescription_Assets_.setPlaceholderText(Translateion('Description', lang))
        self.main_window.InventoryAddingSerialNumber_Assets_.setPlaceholderText(Translateion('Serial Number', lang))
        self.main_window.Inventory_Add_butt_.setText(Translateion('Add', lang))
        self.main_window.Inventory_Return_butt_.setText(Translateion('Return', lang))
        self.main_window.EmployeeMainPage_search_txt.setPlaceholderText(Translateion('Employee Information', lang))
        self.main_window.DepartmentName_txt_.setPlaceholderText(Translateion('Department', lang))
        self.main_window.label_9.setText(Translateion('Department', lang))
        self.main_window.MangerIDDepartment_txt_3.setPlaceholderText(Translateion('Manger', lang))
        self.main_window.AuditorManginigPageEdit_USERNAME_TXT_.setPlaceholderText(Translateion('Return', lang))
        self.main_window.LoansRecordsPage_search_txt.setPlaceholderText(Translateion('Loans Information', lang))
        self.main_window.PaymentAddingPage_Note_txt.setPlaceholderText(Translateion('Notes', lang))
        self.main_window.AssetInventory_search_txt.setPlaceholderText(Translateion('Inventory Information', lang))
        self.main_window.AssetInventory_search_txt.setPlaceholderText(Translateion('Inventory information', lang))



        self.main_window.AssetsAndLoansMainTabs.setTabText(0, Translateion('Assets', lang))
        self.main_window.AssetsAndLoansMainTabs.setTabText(1, Translateion('Loans', lang))

        self.main_window.tabWidget.setTabText(1, Translateion('Assest Allocation', lang))
        self.main_window.tabWidget.setTabText(0, Translateion('Assest Inventory', lang))

        self.main_window.LoansAndPaymentSecondTabWidget.setTabText(0, Translateion('Loans Record', lang))
        self.main_window.LoansAndPaymentSecondTabWidget.setTabText(1, Translateion('Paymenet', lang))

        self.main_window.InventoryTablePage_Assets.setColumnHidden(0, True) 
        self.main_window.InventoryTablePage_Assets.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Description', lang),
            Translateion('SerialNumber', lang),
            Translateion('Quantity', lang),
            Translateion('MoneyValue', lang),
            Translateion('Location', lang),
        ])
        self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnHidden(0, True) 
        self.main_window.AssetsRecordsPage_AssetsDataTable_.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Employee Number', lang),
            Translateion('Object Name', lang),
            Translateion('Department', lang),
            Translateion('Quantity', lang),
            Translateion('Unrecived Quantity', lang),
            Translateion('Allocation Date', lang),
            Translateion('Is Returned', lang),
            Translateion('Return Date', lang),
            Translateion('Notes', lang),
            Translateion('Suggestes Return Date', lang),
            Translateion('Given State', lang),
            Translateion('Return State', lang),
        ])

        self.main_window.AuditorTabel.setColumnHidden(0, True)
        self.main_window.AuditorTabel.setColumnHidden(4, True)

        self.main_window.AuditorTabel.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Employee Number', lang),
            Translateion('Username', lang),
            'EncPassword',
            Translateion('LoginStatus', lang),
            Translateion('AdminCheck', lang),
        ])




        self.main_window.EmployeeMainPage_EmployeeDataTable.setColumnHidden(0, True)
        self.main_window.EmployeeMainPage_EmployeeDataTable.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Employee Number', lang),
            Translateion('Phone', lang),
            Translateion('Department', lang),
            Translateion('Address', lang),
            Translateion('Postal Code', lang),
            Translateion('Grade', lang),
            Translateion('Email', lang),
            Translateion('Is Auditor', lang),
            Translateion('IBAN', lang),
            Translateion('Bank', lang),  
        ])
        
        self.main_window.DepartemntTable.setColumnHidden(0, True)  
        self.main_window.DepartemntTable.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Manager_ID', lang),  
        ])
        self.main_window.LoansRecordsPage_LoansDataTable.setColumnHidden(0, True)
        self.main_window.LoansRecordsPage_LoansDataTable.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Employee Number', lang),
            Translateion('Amount', lang),
            Translateion('Currency', lang),
            Translateion('TimeStamp', lang),
            Translateion('Loan Type', lang),
            Translateion('Deposit Type', lang),
            Translateion('Paid In Full', lang)
            
        ])
        
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.setColumnHidden(0, True)
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.setHorizontalHeaderLabels([
            'ID',
            Translateion('Name', lang),
            Translateion('Employee Number', lang),
            Translateion('Amount', lang),
            Translateion('TimeStamp', lang),
            Translateion('Payment Method', lang),
            Translateion('Notes', lang),     
        ])


    def setup_connections(self):
        self.login_window.Login_butt_login.clicked.connect(self.check_credentials)
        self.login_window.Pass_txt_login.returnPressed.connect(self.check_credentials)
        self.login_window.User_txt_login.returnPressed.connect(self.move_focus_to_password)
        self.main_window.AddEmployeePage_Add_butt.clicked.connect(self.add_employee)
        self.main_window.EmployeeMainPage_search_txt.textChanged.connect(self.filter_employee_table)
        self.main_window.AssetsRecordsPage_search_txt.textChanged.connect(self.filter_Assest_table)
        self.main_window.EmployeeMainPage_add_butt.clicked.connect(self.go_to_add_employee)
        self.main_window.LoanseditTab_save_butt_.clicked.connect(self.edit_Loans)
        self.main_window.Loans_editTab_Return_butt_.clicked.connect(self.go_to_loans_main_page)
        self.main_window.LoansRecordsPage_edit_butt.clicked.connect(self.go_to_edit_loanrecordes)
        self.main_window.EmployeeMainPage_remove_butt.clicked.connect(self.remove_employee)
        self.main_window.EmployeeMainPage_edit_butt.clicked.connect(self.go_to_Edit_employee)
        self.main_window.AddEmployeePage_Return_butt.clicked.connect(self.go_to_employee_main_page)
        self.main_window.AuditorPage_add_butt.clicked.connect(self.go_to_Add_Auditor) 
        self.main_window.EmployeeUsersnButton.clicked.connect(self.user_button)
        self.main_window.Edit_ReturnEmployee_.clicked.connect(self.go_to_employee_main_page)
        self.main_window.Auditor_Return_butt.clicked.connect(self.go_to_employee_main_page)
        self.main_window.Return_Auditor_Mange.clicked.connect(self.user_button)
        self.main_window.Add_Auditor_manging.clicked.connect(self.add_auditor)
        self.main_window.EmployeeMainPage_EmployeeDataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.InventoryTablePage_Assets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.DepartemntTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.AuditorTabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.EditEmployeePage_Save_butt_.clicked.connect(self.edit_employee)
        self.main_window.Logout.clicked.connect(self.logout)
        self.main_window.AssetsEditPage_return_butt_.clicked.connect(self.go_to_assets_main_page)
        self.main_window.AssetsEditPage_save_butt_.clicked.connect(self.edit_asset_allocation)
        self.main_window.AssetsRecordsPage_edit_butt.clicked.connect(self.go_to_assets_edit_page)
        self.main_window.AssetsAddingPage_return_butt_.clicked.connect(self.go_to_assets_main_page)
        self.main_window.AssetsAddingPage_add_butt_.clicked.connect(self.add_assets)
        self.main_window.AssetsRecordsPage_add_butt.clicked.connect(self.go_to_add_assets)
        self.main_window.AssetsRecordsPage_AssetsDataTable_.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.LoansAddingTab_Return_butt.clicked.connect(self.go_to_loans_main_page)
        self.main_window.LoansRecordsPage_Add_butt_.clicked.connect(self.go_to_add_loan)
        self.main_window.LoansRecordsPage_Pay_butt_.clicked.connect(self.go_to_pay_loan)
        self.main_window.PaymentAddingPage_pay_butt.clicked.connect(self.add_payment)
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.PaymentRecordsPage_search_txt.textChanged.connect(self.filter_payment_table)
        self.main_window.LoansRecordsPage_search_txt.textChanged.connect(self.filter_loan_table)
        self.main_window.EmployeeMainPage_EmployeeDataTable.itemSelectionChanged.connect(self.filter_by_employee)
        self.main_window.RESET_butt.clicked.connect(self.load_data)
        self.main_window.EmployeeMainPage_Department_butt.clicked.connect(self.go_to_debartment)
        self.main_window.Departemnt_return_butt_.clicked.connect(self.go_to_debartment)
        self.main_window.LoansAddingTab_add_butt.clicked.connect(self.add_Loans)
        self.main_window.LoansRecordsPage_LoansDataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.Depatrment_add_butt_.clicked.connect(self.add_department)
        self.main_window.Inventory_AddingTable_Add_butt_.clicked.connect(self.go_to_assest_inventroy_add)
        self.main_window.Inventory_Add_butt_.clicked.connect(self.add_assest_inventory)
        self.main_window.Inventory_Return_butt_.clicked.connect(self.go_to_assest_inventroy_table)
        self.main_window.Auditor_Edit_butt.clicked.connect(self.go_to_edit_auditor)
        self.main_window.Edit_Auditor_manging_.clicked.connect(self.edit_auditor)
        self.main_window.Return_EditAuditor_Mange_.clicked.connect(self.go_to_Auditor_record)
        self.main_window.Inventory_Edit__Return_butt_.clicked.connect(self.go_to_assest_inventroy_table)
        self.main_window.AssetInventory_search_txt.textChanged.connect(self.filter_assest_invitory_table)            
        self.main_window.Inventory_Return_butt_.clicked.connect(self.go_to_assest_inventroy_table)
        self.main_window.Inventory_AddingTable_Edit_butt_.clicked.connect(self.go_to_assest_inventroy_edit)
        self.main_window.Inventory_Edit__Save_butt_.clicked.connect(self.edit_assest_inventory)
        self.main_window.Inventory_Edit__Return_butt_.clicked.connect(self.go_to_assest_inventroy_table)
        self.main_window.AssetsRecordsPage_IsReturn_butt_.clicked.connect(self.go_to_return_asset)
        self.inventroy_page.Inventory_page_ReturnItem.clicked.connect(self.return_asset)
        self.inventroy_page.Inventory_page_cancelbutt.clicked.connect(self.inventroy_page.close)
        self.main_window.DepartemntTable_Add_butt.clicked.connect(self.go_to_add_department)
        self.main_window.DepartemntTable_Return_butt.clicked.connect(self.go_to_employee_main_page)
        self.login_window.checkBox_Arabic.stateChanged.connect(self.handleLanguageChange)
        self.main_window.DepartemntTable.itemSelectionChanged.connect(self.filter_by_department)
        self.login_window.Dark_mode_checkBox.stateChanged.connect(self.apply_dark_mode)
        self.main_window.PaymentAddingPage_Return_butt.clicked.connect(self.go_to_loans_main_page)
        self.qapp.aboutToQuit.connect(self.logout)
        self.main_window.EmployeeMainPage_EmployeeDataTable.horizontalHeader().sectionClicked.connect(self.sort_table_emplyee)
        self.main_window.DepartemntTable.horizontalHeader().sectionClicked.connect(self.sort_table_department)
        self.main_window.AuditorTabel.horizontalHeader().sectionClicked.connect(self.sort_table_auditor)
        self.main_window.InventoryTablePage_Assets.horizontalHeader().sectionClicked.connect(self.sort_table_asset_inventory)
        self.main_window.AssetsRecordsPage_AssetsDataTable_.horizontalHeader().sectionClicked.connect(self.sort_table_Asset)
        self.main_window.LoansRecordsPage_LoansDataTable.horizontalHeader().sectionClicked.connect(self.sort_table_loan)
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.horizontalHeader().sectionClicked.connect(self.sort_table_payment)


    def validate_data(self):
        self.main_window.PaymentAddingPage_Amount_txt.setValidator(self.Int_type)
        self.main_window.AddEmployeePage_Employeenumber_txt.setValidator(self.Int_type)
        self.main_window.AddEmployeePage_Phone_txt.setValidator(self.Int_type)
        self.main_window.EditEmployeePage_Employeenumber_txt_.setValidator(self.Int_type)
        self.main_window.EditEmployeePage_Phone_txt_.setValidator(self.Int_type)
        self.main_window.LoansAddingTab_amount_txt.setValidator(self.Int_type)
        self.main_window.LoansEditTab_amount_txt_.setValidator(self.Int_type)
        self.main_window.InventoryAddingMoneyValue_Assets_.setValidator(self.Int_type)
        self.main_window.InventoryEditMoneyValue_Assets_.setValidator(self.Int_type)
        self.main_window.MangerIDDepartment_txt_3.setValidator(self.Int_type)
        self.main_window.AuditorManginigPage_EmployeeNumber_TXT.setValidator(self.Int_type)
           
    def load_data(self):

        self.original_employee_data = []
        self.original_auditor_data = []
        self.original_payment_data=[]
        self.original_financialLoan_data=[]
        self.original_assets_data=[]
        self.original_department_data=[]
        self.original_assest_invontary_data=[]
        
        with Session(engine) as session:
            departments = session.query(Department).all()
            
            for department in departments:
                employee_id = department.Manager_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                if employee :
                    employee_name = employee.Name
                else:
                    employee_name = None

                department_data = [department.id, department.Name,employee_name]
                self.original_department_data.append(department_data)
           
            self.update_department_table(self.original_department_data)
        
        with Session(engine) as session:
            assets = session.query(Assets_Allocation).all()
            
            with Session(engine) as session:
                assets = session.query(Assets_Allocation).all()
                
                for asset in assets:
                    employee_id = asset.Employee_id
                    employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                    assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()
                    department = session.query(Department).filter(Department.id == asset.Department_id).first()                 

                    if department :
                        department_name=department.Name 
                    else:
                        department_name =  "No Department" 

                    asset_data = [asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status]
                    self.original_assets_data.append(asset_data)
            self.update_assets_table(self.original_assets_data)
        
        with Session(engine) as session:
            employees = session.query(Employee).all()
      
            
            for employee in employees:
                department_id = employee.Department_id
                department = session.query(Department).filter(Department.id == department_id).first() 

                employee_data = [employee.id, employee.Name, employee.Employee_number, employee.PhoneNumber,department.Name, employee.Address, employee.PostalCode, employee.Grade,employee.Email, employee.IsAuditor, employee.IBAN, employee.Bank]
                self.original_employee_data.append(employee_data)
           
            self.update_employee_table(self.original_employee_data)



        with Session(engine) as session:
            auditors = session.query(Auditors_user).all()
           
            for auditor in auditors:
                employee_id = auditor.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()  
                auditor_data = [auditor.id ,employee.Name,employee.Employee_number , auditor.User_name,auditor.Enc_password,auditor.Login_status,auditor.Admin_check]
                self.original_auditor_data.append(auditor_data)
        self.update_auditor_table(self.original_auditor_data)  
        with Session(engine) as session:
            payments= session.query(Loan_payment).all()
            
            for payment in payments:
                employee_id = payment.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()                
                payment_data=[payment.id,employee.Name,employee.Employee_number, payment.Amount,payment.Time_stamp,payment.Payment_method,payment.Note]
                self.original_payment_data.append(payment_data)
        self.update_payment_table(self.original_payment_data)
           

        with Session(engine) as session:
            financialLoans = session.query(FinancialLoan).all()              
            for financialLoan in financialLoans:           
                employee_id = financialLoan.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()
            
                financialLoan_data = [financialLoan.id ,employee.Name, employee.Employee_number, financialLoan.Amount, financialLoan.Currency, financialLoan.Timestamp, financialLoan.Loan_type, financialLoan.Type_of_deposit, financialLoan.Paidinfull]                 
                self.original_financialLoan_data.append(financialLoan_data)      
       
       
        self.update_LoansRecords(self.original_financialLoan_data)
        self.main_window.LoansRecordsPage_LoansDataTable.setColumnHidden(0, True)

        with Session(engine) as session:
            inventorys = session.query(Asset_Inventory).all()
           
            for inventory in inventorys:
                asses_inventory = [inventory.id ,inventory.Name,inventory.Description, inventory.Serial_number,inventory.Quantity,inventory.Money_value,inventory.Location]
                self.original_assest_invontary_data.append(asses_inventory)
        self.update_assest_inventory_table(self.original_assest_invontary_data) 

    def check_credentials(self):
        username = self.login_window.User_txt_login.text()
        password = self.login_window.Pass_txt_login.text()
        welcome_message, auditors_user = Auditor.login(username, password)
        if auditors_user:
            self.login_window.close()
            self.main_window.show()
            self.auditor_id = auditors_user.Employee_id  
            self.check_admin_visibility()
            self.show_message_box("Success", welcome_message,self.current_language)
            self.load_data()
        else:
            self.show_message_box("Error", "Invalid username or password.")  
 
    def update_department_table(self, Departments):
        self.main_window.DepartemntTable.setRowCount(0)
        self.main_window.DepartemntTable.setColumnHidden(0, True)

        for row, Department in enumerate(Departments):
            self.main_window.DepartemntTable.insertRow(row)

            for col, value in enumerate(Department):
                item = QtWidgets.QTableWidgetItem(str(value))

                self.main_window.DepartemntTable.setItem(row, col, item)
                
    def update_employee_table(self, employees):
        self.main_window.EmployeeMainPage_EmployeeDataTable.setRowCount(0)
        self.main_window.EmployeeMainPage_EmployeeDataTable.setColumnHidden(0, True)
        for row, employee in enumerate(employees):
            self.main_window.EmployeeMainPage_EmployeeDataTable.insertRow(row)

            for col, value in enumerate(employee):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.main_window.EmployeeMainPage_EmployeeDataTable.setItem(row, col, item)
                if col == 7:
                    item.setText(str(value).split(".")[-1])
            is_auditor = employee[9]
            item = self.main_window.EmployeeMainPage_EmployeeDataTable.item(row, 9)
            if item:
                if is_auditor==True:
                    item.setBackground(QtGui.QColor("#2FCD00"))
                else:
                    item.setBackground(QtGui.QColor("#E52F2F"))
                
    def update_assets_table(self, assets): 
        self.main_window.AssetsRecordsPage_AssetsDataTable_.setRowCount(0)
        self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnHidden(0, True)

        
        for row, asset in enumerate(assets):
            self.main_window.AssetsRecordsPage_AssetsDataTable_.insertRow(row)
            for col, value in enumerate(asset):
                item = QtWidgets.QTableWidgetItem(str(value))
                if col == 12: 
                    item.setText(str(value).split(".")[-1])
                if col == 13: 
                    item.setText(str(value).split(".")[-1])
                if col == 6:
                    self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnWidth(col, 250)
                if col == 7:
                    self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnWidth(col, 250)
                if col == 9:
                    self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnWidth(col, 250)
                if col ==11:
                    self.main_window.AssetsRecordsPage_AssetsDataTable_.setColumnWidth(col, 250)

                self.main_window.AssetsRecordsPage_AssetsDataTable_.setItem(row, col, item)

            isReturned = asset[8]

            item = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(row, 8)
            if item :
                if isReturned==True:
                    item.setBackground(QtGui.QColor("#2FCD00"))
                else:
                    item.setBackground(QtGui.QColor("#E52F2F"))


    def update_payment_table(self,payments):
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.setRowCount(0)
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.setColumnHidden(0, True)

        for row,payment in enumerate(payments):
            self.main_window.PaymentRecordsPage_LoanPaymantTableData.insertRow(row)
            
            for col,value in enumerate(payment):
                item = QtWidgets.QTableWidgetItem(str(value))
                if col==5:
                    item.setText(str(value).split(".")[1])
                self.main_window.PaymentRecordsPage_LoanPaymantTableData.setItem(row, col, item)
                if col == 4:  
                     self.main_window.PaymentRecordsPage_LoanPaymantTableData.setColumnWidth(col, 250)  
            


    def update_assest_inventory_table(self, assest_inventory):
        
        
        self.main_window.InventoryTablePage_Assets.setColumnHidden(0, True)
        self.main_window.InventoryTablePage_Assets.setRowCount(0)
        for row, assest_inventory in enumerate(assest_inventory):
            self.main_window.InventoryTablePage_Assets.insertRow(row)

            for col, value in enumerate(assest_inventory):
                item = QtWidgets.QTableWidgetItem(str(value))

                self.main_window.InventoryTablePage_Assets.setItem(row, col, item)

        

    def update_auditor_table(self, auditors):
        self.main_window.AuditorTabel.setColumnHidden(0, True)
        self.main_window.AuditorTabel.setColumnHidden(4, True)

        self.main_window.AuditorTabel.setRowCount(0)
        for row, auditor in enumerate(auditors):
            self.main_window.AuditorTabel.insertRow(row)

            for col, value in enumerate(auditor):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.main_window.AuditorTabel.setItem(row, col, item)

            login_statues= auditor[5]
            item = self.main_window.AuditorTabel.item(row, 5)
            
            if item :
                if login_statues==True:
                        item.setBackground(QtGui.QColor("#2FCD00"))
                else:
                        item.setBackground(QtGui.QColor("#E52F2F"))
            admin_check= auditor[6]
            item = self.main_window.AuditorTabel.item(row, 6)
            if item :
                if admin_check==True:
                        item.setBackground(QtGui.QColor("#2FCD00"))
                else:
                        item.setBackground(QtGui.QColor("#E52F2F"))

            
    def update_LoansRecords(self, loans):
        self.main_window.LoansRecordsPage_LoansDataTable.setRowCount(0)
        for row, loan in enumerate(loans):
            self.main_window.LoansRecordsPage_LoansDataTable.insertRow(row)
            for col, value in enumerate(loan):
                item = QtWidgets.QTableWidgetItem(str(value))
                if col == 4:
                     item.setText(str(value).split(".")[-1])

                if col == 6:
                    item.setText(str(value).split(".")[-1])

                if col==7: 
                    item.setText(str(value).split(".")[-1])

                if col == 5:
                    self.main_window.LoansRecordsPage_LoansDataTable.setColumnWidth(col, 250)
                self.main_window.LoansRecordsPage_LoansDataTable.setItem(row, col, item) 
            
            paidinful = loan[8]

            item = self.main_window.LoansRecordsPage_LoansDataTable.item(row, 8)
            if item is not None:
                if paidinful:
                    item.setBackground(QtGui.QColor("#2FCD00"))
                else:
                    item.setBackground(QtGui.QColor("#E52F2F"))


    def show_message_box(self, title, message, lang=None):

        lang = self.current_language

        translated_title = Translateion(title, lang)
        translated_message = message

        translations = {
            'Welcome': TranslationData["Welcome"][lang],
            'Employee number': TranslationData["Employee number"][lang],
            'has a Quantity of': TranslationData["has a Quantity of"][lang],
            'The Asset Inventory record with the Object Name': TranslationData["The Asset Inventory record with the Object Name"][lang]
        }
        for key, translation in translations.items():
            translated_message = translated_message.replace(key, translation)

        if translated_message == message:
            translated_message = Translateion(message, lang)

        if translated_message == message:
            translated_message = message

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(translated_title)
        msg_box.setText(translated_message)
        msg_box.exec()



    
    def clear_auditor_adding_fields(self):
        self.main_window.AuditorManginigPage_EmployeeNumber_TXT.clear()
        self.main_window.AuditorManginigPage_USERNAME_TXT.clear()
        self.main_window.AuditorManginigPage_EncPassword_TXT.clear()
        self.main_window.Admin_check_Checkbox.setChecked(False)  

    def clear_pay_loan_fields(self):
        self.main_window.PaymentAddingPage_Amount_txt.clear()
        self.main_window.PaymentAddingPage_payMethod_enum.setCurrentIndex(0)
        self.main_window.PaymentAddingPage_Note_txt.clear()

    def clear_loans_adding_fields(self):
        self.main_window.LoansAddingTab_amount_txt.clear()
        self.main_window.LoansAddingTab_currency_enum.setCurrentIndex(0)
        self.main_window.LoansAddingTab_loantype_enum.setCurrentIndex(0)
        self.main_window.LoansAddingTab_TypeOfDeposit_enum.setCurrentIndex(0)
        
    def clear_employee_adding_fields(self):
        self.main_window.AddEmployeePage_Name_txt.clear()
        self.main_window.AddEmployeePage_Employeenumber_txt.clear()
        self.main_window.AddEmployeePage_Phone_txt.clear()
        self.main_window.AddEmployeePage_Department_enum.setCurrentIndex(0)
        self.main_window.AddEmployeePage_Address_txt.clear()
        self.main_window.AddEmployeePage_Postalcode_txt.clear()
        self.main_window.AddEmployeePage_Grade_enum.setCurrentIndex(0)
        self.main_window.AddEmployeePage_IBAN_txt.clear()
        self.main_window.AddEmployeePage_Bank_txt.clear()
        self.main_window.AddEmployeePage_Email_txt.clear()

    def clear_add_assest_inventory(self):

        self.main_window.InventoryAdding_ObjectName_Assets_.clear()
        self.main_window.InventoryAddingDescription_Assets_.clear()
        self.main_window.InventoryAddingQuantity_Assets_.setValue(0)
        self.main_window.InventoryAddingSerialNumber_Assets_.clear()
        self.main_window.InventoryAddingLocation_Assets_.clear()
        self.main_window.InventoryAddingMoneyValue_Assets_.clear()

    def clear_assets_adding_fields(self):

        self.main_window.AssetsAddingPage_quantity_spinbox.setValue(0)
        self.main_window.AssetsAddingPage_note_txt.clear()
        self.main_window.AssetsAddingPage_suggsestedReturnTime_date.setDate(QtCore.QDate.currentDate())
        self.main_window.AssetsAddingPage_GivenState_enum.setCurrentIndex(0)
    
    def clear_return_asset(self):
        self.inventroy_page.Inventory_page_quantity_spinbox.setValue(0)
        self.inventroy_page.Inventory_page_Returnstate_enum.setCurrentIndex(0)


    def clear_adding_department(self):

        self.main_window.DepartmentName_txt_.clear()
        self.main_window.MangerIDDepartment_txt_3.clear()
        
    def add_Loans(self, lang):
        amount = self.main_window.LoansAddingTab_amount_txt.text()
        Currency1 = self.main_window.LoansAddingTab_currency_enum.currentText()
        currency1 = Translateion(Currency1, lang)
        Loan_type1 = self.main_window.LoansAddingTab_loantype_enum.currentText()
        loan_type1 = Translateion(Loan_type1, lang)
        Type_of_deposit1 = self.main_window.LoansAddingTab_TypeOfDeposit_enum.currentText()
        type_of_deposit1 = Translateion(Type_of_deposit1, lang)

        if currency1 not in [currency.name for currency in Currency]:
            self.show_message_box("Error", "Invalid Currency selected.")
            return
        if loan_type1 not in [loan_type.name for loan_type in LoanType]:
            self.show_message_box("Error", "Invalid Loan Type selected.")
            return
        if type_of_deposit1 not in [type_of_deposit.name for type_of_deposit in TypeOfDeposit]:
            self.show_message_box("Error", "Invalid Type Of Deposit selected.")
            return

        currency = Currency[currency1]
        loan_type = LoanType[loan_type1]
        type_of_deposit = TypeOfDeposit[type_of_deposit1]


        if not all([amount, currency, loan_type, type_of_deposit]):
            self.show_message_box("Error", "Please fill in all the fields.")
            return

        if int(amount) <= 0:
            self.show_message_box("Error", "Amount should be a positive number.")
            return


        auditors_user = self.get_logged_in_auditor()
        auditor_id = auditors_user.id

        Financial_Loan.add(employee_id=self.current_employee_id, amount=amount, auditor_id=auditor_id, currency=currency, loan_type=loan_type, type_of_deposit=type_of_deposit, paid_in_full=False)
        self.show_message_box("Success", "loan added successfully.")
        self.clear_loans_adding_fields()

        added_loans = []
        with Session(engine) as session:
            loans = session.query(FinancialLoan).filter(FinancialLoan.Employee_id == self.current_employee_id).all()
            for loan in loans:
                employee_id = loan.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()
            
                added_loans.append([loan.id ,employee.Name, employee.Employee_number, loan.Amount, loan.Currency, loan.Timestamp, loan.Loan_type, loan.Type_of_deposit, loan.Paidinfull])       

        self.update_LoansRecords(added_loans)

        self.go_to_loans_main_page()

    def add_department(self):
        name = self.main_window.DepartmentName_txt_.text()
        maneger_num = self.main_window.MangerIDDepartment_txt_3.text()
        
        if not name :
            self.show_message_box("Error", "Please fill in all the fields.")
            return

        
        with Session(engine) as session:
            existing_Department_name = session.query(Department).filter(Department.Name == name).first()
            if existing_Department_name:
                self.show_message_box("Error", "An Deparment with the same Department Name already exists.")
                return
            maneger_num_is_employee = session.query(Employee).filter(Employee.Employee_number ==maneger_num).first()
            if not maneger_num_is_employee:
                manger_id=maneger_num_is_employee  = None      
            else:
                manger_id = maneger_num_is_employee.id             
       

        Departments.add(name=name,manager_id=manger_id)
        self.show_message_box("Success", "Department added successfully.") 

        self.clear_adding_department()
        
        self.load_data()
        self.go_to_debartment()

 
    def add_employee(self,lang):
        name = self.main_window.AddEmployeePage_Name_txt.text()
        employee_number = self.main_window.AddEmployeePage_Employeenumber_txt.text()
        phone_number = self.main_window.AddEmployeePage_Phone_txt.text()
        department_name  = self.main_window.AddEmployeePage_Department_enum.currentText()
        address = self.main_window.AddEmployeePage_Address_txt.text()
        postal_code = self.main_window.AddEmployeePage_Postalcode_txt.text()
        grade1 = self.main_window.AddEmployeePage_Grade_enum.currentText()
        Grade1 = Translateion(grade1,lang)
        iBAN = self.main_window.AddEmployeePage_IBAN_txt.text()
        bank = self.main_window.AddEmployeePage_Bank_txt.text()
        email= self.main_window.AddEmployeePage_Email_txt.text()

        if Grade1 not in [grade.name for grade in Grades]:
            self.show_message_box("Error", "Invalid Grade selected.")
            return
        
        Grade = Grades[Grade1]

        if not (name and employee_number and phone_number and address and postal_code and Grade1 and email and iBAN and bank):
            self.show_message_box("Error", "Please fill in all the fields.")
            return
        
        if "@" not in email:
                self.show_message_box("Error", "Invalid email address.")
                return
        
        if len(phone_number) != 10 or not phone_number.isdigit():
            self.show_message_box("Error", " phone number 10-digit number.")
            return


        with Session(engine) as session:
            existing_employee = session.query(Employee).filter(Employee.Employee_number == employee_number).first()
            if existing_employee:
                self.show_message_box("Error", "An employee with the same employee number already exists.")
                return
            department = session.query(Department).filter(Department.Name == department_name).first()
            
            if not department:
                self.show_message_box("Error", "Invalid Department selected.")
                return 
            department_id = department.id
   
        Employees.add(name=name, employee_number=employee_number, phoneNumber=phone_number, department_id=department_id,address=address, postalCode=postal_code, Grade=Grade, iBAN=iBAN, bank=bank, isAduitor=False,email=email)
        self.show_message_box("Success", "Employee added successfully.") 
        self.clear_employee_adding_fields()

        
        self.load_data()
        self.go_to_employee_main_page()
    
         
    def add_assets(self,lang):

        department_name  = self.main_window.AssetsAddingPage_Department_enum.currentText()
        assest_inventory_name =self.main_window.AssetsAddingPage_ObjectName_enum_.currentText()
        quantity = self.main_window.AssetsAddingPage_quantity_spinbox.value()
        note = self.main_window.AssetsAddingPage_note_txt.text()
        suggested_return_date = self.main_window.AssetsAddingPage_suggsestedReturnTime_date.date().toString(QtCore.Qt.ISODate)
        Given_status1 = self.main_window.AssetsAddingPage_GivenState_enum.currentText()
        given_status = Translateion(Given_status1,lang)
        
        if not ( quantity  and suggested_return_date and given_status):
            self.show_message_box("Error", "Please fill in all the required fields.")
            return

        if given_status not in [given_status_enum.name for given_status_enum in Given_status]:
            self.show_message_box("Error", "Invalid Given status selected.")
            return
        given_status_enum = Given_status[given_status]
        
        auditor_user = self.get_logged_in_auditor()
        auditor_id = auditor_user.id
        

        with Session(engine) as session:
            department = session.query(Department).filter(Department.Name == department_name).first()
            assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.Name==assest_inventory_name).first()
            if department_name == "" or department :
                if not department:
                    department_id = None
                else:
                    department_id = department.id 
            else :
                self.show_message_box("Error", "Invalid Deparment selected.")
                return
            if not assest_inventory:
                self.show_message_box("Error", "Invalid Object Name selected.")
                return
            if assest_inventory.Quantity < quantity:
                massege_error=f"The Asset Inventory record with the Object Name {assest_inventory.Name } has a Quantity of {assest_inventory.Quantity }"
                self.show_message_box("Error", massege_error)
                return
            assest_id=assest_inventory.id

        AssetsOfAllocations.add(assest_id= assest_id,employee_id=self.current_employee_id,auditor_id=auditor_id,quantity=quantity,department_id=department_id, note=note,suggestedReturnDate=suggested_return_date, given_status=given_status_enum )
        self.show_message_box("Success", "Asset added successfully.") 
        self.clear_assets_adding_fields()

        with Session(engine) as session:
            assests = session.query(Assets_Allocation).filter(Assets_Allocation.Employee_id == self.current_employee_id).all()

            add_Assests =[]
            for asset in assests :
                employee_id = asset.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                department = session.query(Department).filter(Department.id == asset.Department_id).first()                 
                assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()

                if department :
                    department_name=department.Name 
                else:
                    department_name = None  
                add_Assests.append([asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status])
        self.load_data()
        self.update_assets_table(add_Assests)
        self.go_to_assets_main_page()

    def add_auditor(self):
        employee_number = self.main_window.AuditorManginigPage_EmployeeNumber_TXT.text()
        user_name = self.main_window.AuditorManginigPage_USERNAME_TXT.text()
        enc_password = self.main_window.AuditorManginigPage_EncPassword_TXT.text()
        admin_check = self.main_window.Admin_check_Checkbox.isChecked()

        if not (employee_number and user_name and enc_password ):
            self.show_message_box("Error", "Please fill in all the fields.")
            return




        with Session(engine) as session:
            employee = session.query(Employee).filter(Employee.Employee_number == employee_number).first()
            if not employee:
                self.show_message_box("Error", "The employee Number does not exist in the employee records.")
                return
        

            existing_auditor = session.query(Auditors_user).filter(Auditors_user.Employee_id == employee.id).first()
            if existing_auditor:
                self.show_message_box("Error", "An auditor with the same employee Number already exists.")
                return
            Auditor.add(employee_id=employee.id,user_name=user_name,enc_password=enc_password,admin_check=admin_check)
            self.show_message_box("Success", "Auditor added successfully.") 

            self.clear_auditor_adding_fields()

            self.go_to_Auditor_record()
            self.load_data()


        

    def add_payment(self,lang):

        amount = self.main_window.PaymentAddingPage_Amount_txt.text()
        note = self.main_window.PaymentAddingPage_Note_txt.text()
        Payment_method_value1 = self.main_window.PaymentAddingPage_payMethod_enum.currentText()
        Payment_method_value = Translateion(Payment_method_value1,lang)
        
        if Payment_method_value not in [payment_method.name for payment_method in Payment_method]:
            self.show_message_box("Error", "Invalid Payment method selected.")
            return
        payment_method_enum = Payment_method[Payment_method_value]

        if not (   amount and Payment_method_value):
            self.show_message_box("Error", "Please fill in all the fields.")
            return
        if not amount.isdigit() or int(amount) <= 0:
            self.show_message_box("Error", "Amount should be a positive number.")
            return
    
        auditors_user = self.get_logged_in_auditor()
        auditor_id= auditors_user.id


    

        success,error_message = Payment.add(employee_id=self.current_employee_id, loan_id=self.current_loan_id, auditor_id=auditor_id, amount=amount, PaymentMethod=payment_method_enum,note=note)
        self.clear_pay_loan_fields()

        if not success:
            self.show_message_box("Error",error_message)
            return
        self.show_message_box("Success", "Payment added successfully.")
        add_payments = []
        with Session(engine) as session:
            loan_payments = session.query(Loan_payment).filter(Loan_payment.Employee_id == self.current_employee_id).all()

            for payment in loan_payments:
                employee_id = payment.Employee_id
                employee = session.query(Employee).filter(Employee.id == employee_id).first()                
                add_payments.append([payment.id,employee.Name,employee.Employee_number, payment.Amount,payment.Time_stamp,payment.Payment_method,payment.Note])
        self.load_data()    
        self.update_payment_table(add_payments)
        self.go_to_payment_main_Page()

    
    def add_assest_inventory(self):
        name= self.main_window.InventoryAdding_ObjectName_Assets_.text()
        descroption=self.main_window.InventoryAddingDescription_Assets_.text()
        quantity = self.main_window.InventoryAddingQuantity_Assets_.value()
        serial_number= self.main_window.InventoryAddingSerialNumber_Assets_.text()
        location= self.main_window.InventoryAddingLocation_Assets_.text()
        money_value= self.main_window.InventoryAddingMoneyValue_Assets_.text()
        
        if not ( name and descroption and serial_number and location and money_value and quantity):
            self.show_message_box("Error", "Please fill in all the fields.")
            return
        
        with Session(engine) as session:
            existing_inventory_name = session.query(Asset_Inventory).filter(Asset_Inventory.Name == name).first()
            if existing_inventory_name:
                self.show_message_box("Error", "An Asset inventory with the same Object Name already exists.")
                return
                    
        AssetInventory.add(name=name,description=descroption,serial_number=serial_number,money_value=money_value,quantity=quantity,location=location)
        self.show_message_box("Success", "Asset Inventory added successfully.") 
        self.clear_add_assest_inventory()

        self.load_data()
        self.go_to_assest_inventroy_table()



    def populate_combo_boxes(self,lang=0):
        self.inventroy_page.Inventory_page_Returnstate_enum.clear()
        self.main_window.AddEmployeePage_Grade_enum.clear()
        self.main_window.EditEmployeePage_Grade_enum_.clear()
        self.main_window.LoansAddingTab_currency_enum.clear()
        self.main_window.LoansEditTab_currency_enum_.clear()
        self.main_window.LoansAddingTab_loantype_enum.clear()
        self.main_window.LoansEditTab_loantype_enum_.clear()
        self.main_window.LoansAddingTab_TypeOfDeposit_enum.clear()
        self.main_window.LoansEditTab_TypeOfDeposit_enum_.clear()
        self.main_window.AssetsAddingPage_GivenState_enum.clear()
        self.main_window.AssetsEditPage_GivenState_enum_.clear()
        self.main_window.PaymentAddingPage_payMethod_enum.clear()


        returned_status_names = [Translateion(returned_status.name, lang) for returned_status in Returned_status]
        self.inventroy_page.Inventory_page_Returnstate_enum.addItems(returned_status_names)
        
    
        grade_names = [Translateion(grade.name, lang) for grade in Grades]
        self.main_window.AddEmployeePage_Grade_enum.addItems(grade_names)
        self.main_window.EditEmployeePage_Grade_enum_.addItems(grade_names)

        currency_names = [Translateion(currency.name, lang) for currency in Currency]
        self.main_window.LoansAddingTab_currency_enum.addItems(currency_names)
        self.main_window.LoansEditTab_currency_enum_.addItems(currency_names)

        loantype_names = [Translateion(loantype.name, lang) for loantype in LoanType]
        self.main_window.LoansAddingTab_loantype_enum.addItems(loantype_names)
        self.main_window.LoansEditTab_loantype_enum_.addItems(loantype_names)

        type_of_deposit_names = [Translateion(deposit.name, lang) for deposit in TypeOfDeposit]
        self.main_window.LoansAddingTab_TypeOfDeposit_enum.addItems(type_of_deposit_names)
        self.main_window.LoansEditTab_TypeOfDeposit_enum_.addItems(type_of_deposit_names)

        given_status_names = [Translateion(status.name, lang) for status in Given_status]
        self.main_window.AssetsAddingPage_GivenState_enum.addItems(given_status_names)
        self.main_window.AssetsEditPage_GivenState_enum_.addItems(given_status_names)

        payment_method_names = [Translateion(method.name, lang) for method in Payment_method]
        self.main_window.PaymentAddingPage_payMethod_enum.addItems(payment_method_names)
  
    def populate_combo_boxes_object_name(self):
        with Session(engine) as session:
            assest_inventory = session.query(Asset_Inventory).all()

            object_names = [assest_object_name.Name for assest_object_name in assest_inventory]
        
        self.main_window.AssetsAddingPage_ObjectName_enum_.clear()
        self.main_window.AssetsAddingPage_ObjectName_enum_.addItems(object_names)

    def populate_combo_boxes_department(self):
        with Session(engine) as session:
            departments = session.query(Department).all()

            department_names = [department.Name for department in departments]
        
        self.main_window.AddEmployeePage_Department_enum.clear()
        self.main_window.EditEmployeePage_Department_enum_.clear()
        self.main_window.AssetsAddingPage_Department_enum.clear()

        self.main_window.AddEmployeePage_Department_enum.addItems(department_names)
        self.main_window.EditEmployeePage_Department_enum_.addItems(department_names)
        self.main_window.AssetsAddingPage_Department_enum.addItems(department_names)
        self.main_window.AssetsAddingPage_Department_enum.setCurrentIndex(-1)

    
    def filter_by_department(self):
            selected_row = self.main_window.DepartemntTable.currentRow()
            if selected_row >= 0:        
                department_id = self.main_window.DepartemntTable.item(selected_row, 0).text()
                with Session(engine) as session:
                    assests = session.query(Assets_Allocation).filter(Assets_Allocation.Department_id == department_id).all()
                    filtered_Assests =[]
                    for asset in assests :
                        department_id = asset.Department_id
                        employee = session.query(Employee).filter(Employee.id == asset.Employee_id).first() 
                        assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()
                        department = session.query(Department).filter(Department.id == asset.Department_id).first()                 

                        if department :
                            department_name=department.Name 
                        else:
                            department_name = None  

                        filtered_Assests.append([asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status])
                    self.update_assets_table(filtered_Assests)
                        
    def filter_by_employee(self):
            selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
            if selected_row >= 0: 
                employee_id = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()
                with Session(engine) as session:
                    loan_payments = session.query(Loan_payment).filter(Loan_payment.Employee_id == employee_id).all()
                    loans = session.query(FinancialLoan).filter(FinancialLoan.Employee_id == employee_id).all()
                    assests = session.query(Assets_Allocation).filter(Assets_Allocation.Employee_id == employee_id).all()

                    filtered_Assests =[]
                    for asset in assests :
                        employee_id = asset.Employee_id
                        employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                        department = session.query(Department).filter(Department.id == asset.Department_id).first()                 
                        assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()

                        if department :
                            department_name=department.Name 
                        else:
                            department_name = None  
                        filtered_Assests.append([asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status])

                    filtered_payments = []
                    for payment in loan_payments:
                        employee_id = payment.Employee_id
                        employee = session.query(Employee).filter(Employee.id == employee_id).first()                
                        filtered_payments.append([payment.id,employee.Name,employee.Employee_number, payment.Amount,payment.Time_stamp,payment.Payment_method,payment.Note])
                    
                    filtered_loans = []
                    for loan in loans:
                        employee_id = loan.Employee_id
                        employee = session.query(Employee).filter(Employee.id == employee_id).first()
                    
                        filtered_loans.append([loan.id ,employee.Name, employee.Employee_number, loan.Amount, loan.Currency, loan.Timestamp, loan.Loan_type, loan.Type_of_deposit, loan.Paidinfull])       
                    
                    self.update_payment_table(filtered_payments)
                    self.update_LoansRecords(filtered_loans)
                    self.update_assets_table(filtered_Assests)        

    
    def filter_employee_table(self):
        search_query = self.main_window.EmployeeMainPage_search_txt.text()
        if search_query:
            filtered_employees = Employees.search(search_query)
            self.update_employee_table(filtered_employees)
        else:
            self.update_employee_table(self.original_employee_data)

    def filter_loan_table(self):
        search_query = self.main_window.LoansRecordsPage_search_txt.text()
        if search_query:
            filtered_loan = Financial_Loan.search(search_query)
            self.update_LoansRecords(filtered_loan)
        else:
            self.update_LoansRecords(self.original_financialLoan_data)

    def filter_Assest_table(self):
        search_query = self.main_window.AssetsRecordsPage_search_txt.text()
        if search_query:
            filtered_Assest = AssetsOfAllocations.search(search_query)
            self.update_assets_table(filtered_Assest)
        else:
            self.update_assets_table(self.original_assets_data)

    def filter_payment_table(self):
        search_query = self.main_window.PaymentRecordsPage_search_txt.text()
        if search_query:
            filtered_payment = Payment.search(search_query)
            self.update_payment_table(filtered_payment)
        else:
            self.update_payment_table(self.original_payment_data)

    def filter_assest_invitory_table(self):
            search_query = self.main_window.AssetInventory_search_txt.text()
            if search_query:
                filtered_assest_inventory = AssetInventory.search(search_query)
                self.update_assest_inventory_table(filtered_assest_inventory)
            else:
                self.update_assest_inventory_table(self.original_assest_invontary_data)


    


    def edit_auditor(self):
        selected_row = self.main_window.AuditorTabel.currentRow()
        if selected_row >= 0:
            auditor_id = self.main_window.AuditorTabel.item(selected_row, 0).text()
            username = self.main_window.AuditorManginigPageEdit_USERNAME_TXT_.text()
            enc_pass = self.main_window.AuditorManginigPageEdit_EncPassword_TXT_.text()
            admin_check = self.main_window.Admin_checkEdit_Checkbox_.isChecked()  
            hashed_password = hashpassword(enc_pass)

            data = {

                'User_name': username,
                'Enc_password': hashed_password,
                'Admin_check': admin_check
            }
            if not ( username and enc_pass ):
                self.show_message_box("Error", "Please fill in all the required fields.")
                return
 
            try:
                Auditor.edit(auditor_id, data)
                self.show_message_box("Success", "Auditor edited successfully.")
                self.original_auditor_data[selected_row] 
                self.update_auditor_table(self.original_assets_data)
                self.go_to_Auditor_record()
                self.load_data()

            except ValueError as e:
                self.show_message_box("Error", str(e))
        else:
            self.show_message_box("Error", "No Auditor")     

    def edit_assest_inventory(self):
        selected_row = self.main_window.InventoryTablePage_Assets.currentRow()
        if selected_row >= 0:  
            assest_inventory_id = self.main_window.InventoryTablePage_Assets.item(selected_row, 0).text()
            name= self.main_window.InventoryEdit_ObjectName_Assets_.text()
            description= self.main_window.InventoryEditDescription_Assets_.text()
            serial_number= self.main_window.InventoryEditSerialNumber_Assets_.text()
            location= self.main_window.InventoryEditLocation_Assets_.text()
            money_value= self.main_window.InventoryEditMoneyValue_Assets_.text()
            quantity= self.main_window.InventoryEditQuantity_Assets_.value()


            data = {
                'Name': name,
                'Description': description,
                'Serial_number': serial_number,     
                'Quantity': quantity,
                'Money_value': money_value,
                'Location': location

            }
            if not ( name and description and serial_number and location and money_value and quantity):
                self.show_message_box("Error", "Please fill in all the fields.")
                return
            AssetInventory.edit(assest_inventory_id, data)
            self.show_message_box("Success", "assestInvontary record edited successfully.")
            self.original_assest_invontary_data[selected_row]
            self.update_assest_inventory_table(self.original_assest_invontary_data)
            self.load_data()
            self.go_to_assest_inventroy_table()
            
    def edit_asset_allocation(self,lang):
        selected_row = self.main_window.AssetsRecordsPage_AssetsDataTable_.currentRow()
        if selected_row >= 0:
            allocation_id = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row, 0).text()
            note = self.main_window.AssetsEditPage_note_txt_.text()
            suggested_return_date = self.main_window.AssetsAddingPage_suggsestedReturnTime_date_2.date().toString("yyyy-MM-dd")
            given_statu1=self.main_window.AssetsEditPage_GivenState_enum_.currentText()
            given_statu = Translateion(given_statu1,lang)
            if given_statu not in [given_status_enum.name for given_status_enum in Given_status]:
                self.show_message_box("Error", "Invalid Given status selected.")
                return 
            given_status = Given_status[given_statu]
     


            data = {

                'Note': note,
                'Suggested_ReturnDate': suggested_return_date,
                'Given_status': given_status
            }
            if not suggested_return_date:
                self.show_message_box("Error", "Please fill in all the required fields.")
                return
            try:
                AssetsOfAllocations.edit(allocation_id, data)
                self.show_message_box("Success", "Asset allocation edited successfully.")
                self.original_assets_data[selected_row] 
                self.update_assets_table(self.original_assets_data)
                self.go_to_assets_main_page()
                self.load_data()

            except ValueError as e:
                self.show_message_box("Error", str(e))
        else:
            self.show_message_box("Error", "No asset allocation selected.")     
    
    def edit_employee(self,lang):
        selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
        if selected_row >= 0:
            employee_id = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()

            name = self.main_window.Edit_EmployeePage_Name_txt_.text()
            employee_number = self.main_window.EditEmployeePage_Employeenumber_txt_.text()
            phone_number = self.main_window.EditEmployeePage_Phone_txt_.text()
            department1 = self.main_window.EditEmployeePage_Department_enum_.currentText()
            department_id = self.get_department_id(department1) 
            address = self.main_window.Edit_EmployeePage_Address_txt_.text()
            postal_code = self.main_window.EditEmployeePage_Postalcode_txt_.text()
            email = self.main_window.EditEmployeePage_Email_txt.text()
            grade1 = self.main_window.EditEmployeePage_Grade_enum_.currentText()
            Grade1 = Translateion(grade1,lang)
            iBAN = self.main_window.EditEmployeePage_IBAN_txt_.text()
            bank = self.main_window.EditEmployeePage_Bank_txt_.text()
            
            
            if not department_id :    
                self.show_message_box("Error", "Invalid Deparment selected.")
                return
            if Grade1 not in [grade.name for grade in Grades]:
                self.show_message_box("Error", "Invalid Grade selected.")
                return
            
            if not (name and employee_number and phone_number and address and postal_code and Grade1 and email and iBAN and bank):
                self.show_message_box("Error", "Please fill in all the fields.")
                return
            
            if "@" not in email:
                    self.show_message_box("Error", "Invalid email address.")
                    return
            
            if len(phone_number) != 10 or not phone_number.isdigit():
                self.show_message_box("Error", " phone number 10-digit number.")
                return
            data = {
        'Name': name,
        'Employee_number': employee_number,
        'PhoneNumber': phone_number,
        'Department_id': department_id,
        'Address': address,
        'PostalCode': postal_code,
        'Grade': Grades[Grade1],
        "Email": email,
        'IBAN': iBAN,
        'Bank': bank,
    }

            try:
                Employees.edit(int(employee_id), data)
                self.show_message_box("Success", "Employee edited successfully.")
                self.original_employee_data[selected_row]   
                self.update_employee_table(self.original_employee_data)
                self.load_data()
                self.go_to_employee_main_page()
            except ValueError as e:
                self.show_message_box("Error", str(e))
        else:
            self.show_message_box("Error", "No employee selected.")


    def edit_Loans(self,lang):
         selected_row = self.main_window.LoansRecordsPage_LoansDataTable.currentRow()
         if selected_row >= 0:

            Loan_id=self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,0).text()
            amount = self.main_window.LoansEditTab_amount_txt_.text()
            currency1 = self.main_window.LoansEditTab_currency_enum_.currentText()
            currency = Translateion(currency1,lang)
            loan_type1 = self.main_window.LoansEditTab_loantype_enum_.currentText()
            loan_type = Translateion(loan_type1,lang)
            type_of_deposit1 = self.main_window.LoansEditTab_TypeOfDeposit_enum_.currentText()
            type_of_deposit = Translateion(type_of_deposit1,lang)

            if currency not in [currency.name for currency in Currency]:
                self.show_message_box("Error", "Invalid Currency selected.")
                return
            if loan_type not in [loan_type.name for loan_type in LoanType]:
                self.show_message_box("Error", "Invalid Loan Type selected.")
                return
            if type_of_deposit not in [type_of_deposit.name for type_of_deposit in TypeOfDeposit]:
                self.show_message_box("Error", "Invalid Type Of Deposit selected.")
                return
            if not all([ amount, currency, loan_type, type_of_deposit]):
                self.show_message_box("Error", "Please fill in all the fields.")
                return
        

            if not amount.isdigit() or int(amount) <= 0:
                self.show_message_box("Error", "Amount should be a positive number.")
                return
            
            data = {
                'Amount': amount,
                'Currency': currency,
                'Loan_type': loan_type,
                'Type_of_deposit': type_of_deposit
            }

            try:
                Financial_Loan.edit(Loan_id, data)
                self.show_message_box("Success", "Financial loan record edited successfully.")
                self.original_financialLoan_data[selected_row] 
                self.update_LoansRecords(self.original_financialLoan_data)
                self.load_data()
                self.go_to_loans_main_page()
            except ValueError as e:
             self.show_message_box("Error", str(e))
         else:
            self.show_message_box("Error", "Invalid currency, loan type, or type of deposit selected.")


    

    def remove_employee(self):
        selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
        if selected_row >= 0:
            employee_id = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()
            try:
                Employees.delete( int(employee_id))
                self.show_message_box("Success", "Employee removed successfully.")
                self.original_employee_data.pop(selected_row)
                self.update_employee_table(self.original_employee_data)
            except PermissionError as not_admin:
                self.show_message_box("Error", str(not_admin))
        else:
            self.show_message_box("Error", "No employee selected.")
    
    
    def return_asset(self,lang):
        selected_row = self.main_window.AssetsRecordsPage_AssetsDataTable_.currentRow()
        asset_id = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row, 0).text()
        returned_quantity = self.inventroy_page.Inventory_page_quantity_spinbox.value()
        returned_status1 = self.inventroy_page.Inventory_page_Returnstate_enum.currentText()
        returned_status = Translateion(returned_status1,lang)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if returned_status not in [returned_status_enum.name for returned_status_enum in Returned_status]:
            self.show_message_box("Error", "Invalid Return status selected.")
            return
        if not returned_quantity:
            self.show_message_box("Error", "Please fill in all the required fields.")
            return

        with Session(engine) as session:
            asset = session.query(Assets_Allocation).filter(Assets_Allocation.id == asset_id).first()
            if asset is None:
                self.show_message_box("Error", "Asset not found. Cannot return the item.")
            else:
                asset_inventory = session.query(Asset_Inventory).filter(Asset_Inventory.id == asset.Asset_id).first()
                if asset_inventory is None:
                    self.show_message_box("Error", "Asset Inventory not found. Cannot return the item.")
                elif asset.IsReturned == False: 
                    if asset.Unrecived_Quantity is not None and asset.Unrecived_Quantity < returned_quantity:
                        self.show_message_box("Error", "Unreceived quantity is less than the returned quantity.")
                    else:
                        asset.Returned_status = returned_status
                        asset_inventory.Quantity += returned_quantity
                        if asset.Unrecived_Quantity is None:
                             asset.Unrecived_Quantity = 0

                        asset.Unrecived_Quantity -= returned_quantity

                        if asset.Unrecived_Quantity == 0:
                            asset.IsReturned = True                   
                            asset.Return_Date = timestamp
                        
                        session.commit()
                        self.show_message_box("Success", "Asset returned successfully.")
                        self.clear_return_asset()
                        selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
                        if selected_row >= 0:
                            employee_id_current = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()    
                            with Session(engine) as session:
                                assests = session.query(Assets_Allocation).filter(Assets_Allocation.Employee_id == employee_id_current).all()

                                add_Assests =[]
                                for asset in assests :
                                    employee_id = asset.Employee_id
                                    employee = session.query(Employee).filter(Employee.id == employee_id).first() 
                                    department = session.query(Department).filter(Department.id == asset.Department_id).first()                 
                                    assest_inventory=session.query(Asset_Inventory).filter(Asset_Inventory.id==asset.Asset_id).first()

                                    if department :
                                        department_name=department.Name 
                                    else:
                                        department_name = None  
                                    add_Assests.append([asset.id ,employee.Name, employee.Employee_number,assest_inventory.Name,department_name, asset.Quantity, asset.Unrecived_Quantity,asset.Allocation_Date,asset.IsReturned, asset.Return_Date, asset.Note, asset.Suggested_ReturnDate, asset.Given_status,asset.Returned_status])
                                self.load_data() 
                            self.update_assets_table(add_Assests)
                        else:
                            self.load_data() 


                        self.inventroy_page.close()
                else:
                    self.show_message_box("Error", "Asset is already returned.")

    def is_admin(self):

         with Session(engine) as session:
            is_admin = session.query(Auditors_user).filter(Auditors_user.Employee_id == self.auditor_id, Auditors_user.Admin_check == True).first()
            if not is_admin:
                raise PermissionError
            return True
         
    def user_button(self):

        self.main_window.EmployeeStackedWidget.setCurrentIndex(5)

  

    def get_logged_in_auditor(self):
        with Session(engine) as session:
            auditors_user = session.query(Auditors_user).filter(Auditors_user.Login_status == True).first()

        if auditors_user:
             return auditors_user
        else:
            self.show_message_box("Error", "No auditor logged in.")
            return None    
        
    def logout(self):
            user_name = self.login_window.User_txt_login.text()

            if Auditor.logout(user_name):
                self.main_window.close()
                self.login_window.show()
                self.login_window.User_txt_login.clear()
                self.login_window.Pass_txt_login.clear()
                self.main_window.Assest_Inventory_stackedWidget.setCurrentIndex(0)
                self.main_window.AssetAllocations_stackedwidget.setCurrentIndex(0)
                self.main_window.EmployeeStackedWidget.setCurrentIndex(0)


    def sort_table_emplyee(self, logical_index):
        self.main_window.EmployeeMainPage_EmployeeDataTable.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_asset_inventory(self, logical_index):
        self.main_window.InventoryTablePage_Assets.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_Asset(self, logical_index):
        self.main_window.AssetsRecordsPage_AssetsDataTable_.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_loan(self, logical_index):
        self.main_window.LoansRecordsPage_LoansDataTable.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_payment(self, logical_index):
        self.main_window.PaymentRecordsPage_LoanPaymantTableData.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_department(self, logical_index):
        self.main_window.DepartemntTable.sortItems(logical_index, QtCore.Qt.AscendingOrder)                
    def sort_table_auditor(self, logical_index):
        self.main_window.AuditorTabel.sortItems(logical_index, QtCore.Qt.AscendingOrder)                


    def check_admin_visibility(self):
            try:
                self.is_admin()
                self.main_window.EmployeeUsersnButton.setVisible(True)
                self.main_window.EmployeeMainPage_remove_butt.setVisible(True)
                self.main_window.DepartemntTable_Add_butt.setVisible(True)


            except PermissionError:
                self.main_window.EmployeeUsersnButton.setVisible(False)
                self.main_window.EmployeeMainPage_remove_butt.setVisible(False)
                self.main_window.DepartemntTable_Add_butt.setVisible(False)

    def get_department_id(self,department_name):
            with Session(engine) as session:
                department = session.query(Department).filter_by(Name=department_name).first()
                if department:
                    return department.id        


    def move_focus_to_password(self):
        self.login_window.Pass_txt_login.setFocus()
    
    def go_to_return_asset(self):
        selected_row = self.main_window.AssetsRecordsPage_AssetsDataTable_.currentRow()
        if selected_row >= 0:
            asset_id = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row, 0).text()
            with Session(engine) as session:
                asset = session.query(Assets_Allocation).filter(Assets_Allocation.id==asset_id).first()
            if asset.IsReturned ==True:
                self.show_message_box("Error", "Asset is already returned.")
            else:
                self.clear_return_asset()
                self.inventroy_page.show()


        else:
            self.show_message_box("Error", "Please select an asset from the table.")

    def go_to_add_employee(self):

        self.clear_employee_adding_fields()

        self.populate_combo_boxes_department()

        self.main_window.EmployeeStackedWidget.setCurrentIndex(3)
    def go_to_debartment(self) :
        self.main_window.EmployeeStackedWidget.setCurrentIndex(1)
   
    def go_to_add_department(self):

        self.clear_adding_department()
        self.main_window.EmployeeStackedWidget.setCurrentIndex(2)

    def go_to_employee_main_page(self):

        self.main_window.EmployeeStackedWidget.setCurrentIndex(0)


    def go_to_Add_Auditor(self):
        
        self.clear_auditor_adding_fields()

        self.main_window.EmployeeStackedWidget.setCurrentIndex(6)    
    
    def go_to_Auditor_record(self):
        self.clear_assets
    
        self.main_window.EmployeeStackedWidget.setCurrentIndex(5)


    def go_to_add_assets(self):

            selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
            if selected_row >= 0:
                employee_id = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()
                self.current_employee_id = employee_id
               
                self.clear_assets_adding_fields()
                self.main_window.AssetAllocations_stackedwidget.setCurrentIndex(1)
                self.populate_combo_boxes_object_name()
                self.populate_combo_boxes_department()

               

            else:
                self.show_message_box("Error", "No employee selected.")

    
    def go_to_assets_main_page(self):
        self.main_window.AssetAllocations_stackedwidget.setCurrentIndex(0)
    def go_to_assest_inventroy_add(self):

        self.clear_add_assest_inventory()

        self.main_window.Assest_Inventory_stackedWidget.setCurrentIndex(1)
    def go_to_assest_inventroy_table(self):
        self.main_window.Assest_Inventory_stackedWidget.setCurrentIndex(0)

    def go_to_assest_inventroy_edit(self):
        selected_row = self.main_window.InventoryTablePage_Assets.currentRow()

        if selected_row >= 0:
            name = self.main_window.InventoryTablePage_Assets.item(selected_row, 1).text()
            description = self.main_window.InventoryTablePage_Assets.item(selected_row, 2).text()
            serial_number = self.main_window.InventoryTablePage_Assets.item(selected_row, 3).text()
            money_value = self.main_window.InventoryTablePage_Assets.item(selected_row, 5).text()
            quantity = self.main_window.InventoryTablePage_Assets.item(selected_row, 4).text()
            location = self.main_window.InventoryTablePage_Assets.item(selected_row, 6).text()

            self.main_window.InventoryEdit_ObjectName_Assets_.setText(name)
            self.main_window.InventoryEditDescription_Assets_.setText(description)
            self.main_window.InventoryEditSerialNumber_Assets_.setText(serial_number)
            self.main_window.InventoryEditMoneyValue_Assets_.setText(money_value)
            self.main_window.InventoryEditQuantity_Assets_.setValue(int(quantity))
            self.main_window.InventoryEditLocation_Assets_.setText(location)

            self.main_window.Assest_Inventory_stackedWidget.setCurrentIndex(2)

        else:
            self.show_message_box("Error", "No Assest Inventory selected.")



   
    def go_to_add_loan(self):
        selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
        if selected_row >= 0:
            employee_id = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 0).text()
            self.main_window.LoansRecord_stackedwidget.setCurrentIndex(1)
            self.current_employee_id = employee_id
            self.clear_loans_adding_fields()

        else:
            self.show_message_box("Error", "No employee selected.")

   
    def go_to_loans_main_page(self):
        
        self.main_window.LoansRecord_stackedwidget.setCurrentIndex(0)
   
    def go_to_pay_loan(self):

        selected_row = self.main_window.LoansRecordsPage_LoansDataTable.currentRow()
        if selected_row >= 0:
            loan_id = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row, 0).text()
            self.current_loan_id = loan_id
            
            with Session(engine) as session:
                loans = session.query(FinancialLoan).filter(FinancialLoan.id==self.current_loan_id ).first()
                self.current_employee_id= loans.Employee_id
                if loans.Paidinfull == True:
                    self.show_message_box("Error", "loan is Paid in full.") 
                    return
            self.main_window.LoansRecord_stackedwidget.setCurrentIndex(3)
        else:
            self.show_message_box("Error", "No loan selected.")

    def go_to_payment_main_Page(self):
        self.main_window.LoansRecord_stackedwidget.setCurrentIndex(0)
        widget = self.main_window.LoansAndPaymentSecondTabWidget.widget(1)
        self.main_window.LoansAndPaymentSecondTabWidget.setCurrentWidget(widget)

    def go_to_assets_edit_page(self,lang):
        lang = self.current_language

        selected_row = self.main_window.AssetsRecordsPage_AssetsDataTable_.currentRow()
    
        if selected_row >= 0:
            
            
            assest_id = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row, 0).text()
            note = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row, 10).text()
            suggested_return_date = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row,11).text()
            given_status1 = self.main_window.AssetsRecordsPage_AssetsDataTable_.item(selected_row,12 ).text()
            given_status = Translateion(given_status1,lang)
            self.populate_combo_boxes_department()
            self.main_window.AssetsEditPage_note_txt_.setText(note)
            self.main_window.AssetsAddingPage_suggsestedReturnTime_date_2.setDate(QtCore.QDate.fromString(suggested_return_date, "yyyy-MM-dd"))
            self.main_window.AssetsEditPage_GivenState_enum_.setCurrentText(given_status)
            with Session(engine) as session:
                asest = session.query(Assets_Allocation).filter(Assets_Allocation.id == assest_id).first()
                if asest.IsReturned == True:
                    self.show_message_box("Error", "Asest is alredy Returned.") 
                    return
            self.main_window.AssetAllocations_stackedwidget.setCurrentIndex(2)
        else:
            self.show_message_box("Error", "No Assest selected.")        

    def go_to_Edit_employee(self,lang):
        lang = self.current_language

        selected_row = self.main_window.EmployeeMainPage_EmployeeDataTable.currentRow()
        
        if selected_row >= 0:
            name = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 1).text()
            employee_number = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 2).text()
            phone_number = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 3).text()
            department1 = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 4).text()
            address = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 5).text()
            postal_code = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 6).text()
            grade1 = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 7).text()
            Grade1 = Translateion(grade1,lang)
            iBAN = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 10).text()
            bank = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 11).text()
            email = self.main_window.EmployeeMainPage_EmployeeDataTable.item(selected_row, 8).text()

        
            self.populate_combo_boxes_department()
            
            
            self.main_window.Edit_EmployeePage_Name_txt_.setText(name)
            self.main_window.EditEmployeePage_Employeenumber_txt_.setText(employee_number)
            self.main_window.EditEmployeePage_Phone_txt_.setText(phone_number)
            self.main_window.Edit_EmployeePage_Address_txt_.setText(address)
            self.main_window.EditEmployeePage_Postalcode_txt_.setText(postal_code)
            self.main_window.EditEmployeePage_IBAN_txt_.setText(iBAN)
            self.main_window.EditEmployeePage_Grade_enum_.setCurrentText(Grade1)
            self.main_window.EditEmployeePage_Department_enum_.setCurrentText(department1)
            self.main_window.EditEmployeePage_Bank_txt_.setText(bank)
            self.main_window.EditEmployeePage_Email_txt.setText(email)
   
            self.main_window.EmployeeStackedWidget.setCurrentIndex(4)  
        else:
            self.show_message_box("Error", "No employee selected.")




    def go_to_edit_loanrecordes(self,lang):
        lang = self.current_language
        selected_row = self.main_window.LoansRecordsPage_LoansDataTable.currentRow()
        if  selected_row >= 0:
            loan_ID = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,0).text()
            amount = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,3).text()
            currency1 = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,4).text()
            currency = Translateion(currency1,lang)
            loan_type1 = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,6).text()
            loan_type = Translateion(loan_type1,lang)
            type_of_deposit1 = self.main_window.LoansRecordsPage_LoansDataTable.item(selected_row,7).text()
            type_of_deposit = Translateion(type_of_deposit1,lang)
            self.main_window.LoansEditTab_amount_txt_.setText(amount)
            self.main_window.LoansEditTab_currency_enum_.setCurrentText(currency)
            self.main_window.LoansEditTab_loantype_enum_.setCurrentText(loan_type)
            self.main_window.LoansEditTab_TypeOfDeposit_enum_.setCurrentText(type_of_deposit)
            with Session(engine) as session:
                loans = session.query(FinancialLoan).filter(FinancialLoan.id == loan_ID).first()
                if loans.Paidinfull == True:
                    self.show_message_box("Error", "Loan is Paid in full.") 
                    return


            self.main_window.LoansRecord_stackedwidget.setCurrentIndex(2)
        else:
             self.show_message_box("Error", "No Loan selected.")

    def go_to_edit_auditor(self):
            selected_row = self.main_window.AuditorTabel.currentRow()
            if  selected_row >= 0:

                username = self.main_window.AuditorTabel.item(selected_row,3).text()
                enc_pass = self.main_window.AuditorTabel.item(selected_row,4).text()
                admin_check = self.main_window.AuditorTabel.item(selected_row, 6).text() 

                self.main_window.AuditorManginigPageEdit_USERNAME_TXT_.setText(username)
                self.main_window.AuditorManginigPageEdit_EncPassword_TXT_.setText(enc_pass)
                self.main_window.Admin_checkEdit_Checkbox_.setChecked(admin_check == 'True')

                self.main_window.EmployeeStackedWidget.setCurrentIndex(7)
            else:
                self.show_message_box("Error", "No Auditor selected.")


    def apply_dark_mode(self):
        if self.login_window.Dark_mode_checkBox.isChecked():
            dark_palette = QtGui.QPalette()
            dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
            dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 255, 255))
            dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
            dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
            dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
            dark_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255, 255, 255))
            dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 255))
            dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
            dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255, 255, 255))
            dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 0, 0))
            dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
            dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
            dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(255, 255, 255))
            self.qapp.setPalette(dark_palette)
        else:
            self.qapp.setStyle("Fusion")
            default_palette = QtGui.QPalette()
            self.qapp.setPalette(default_palette)
            
    def run(self):
        self.login_window.show()
        sys.exit(self.qapp.exec_())
        
if __name__=="__main__":

    app = MyApp()
    app.run()