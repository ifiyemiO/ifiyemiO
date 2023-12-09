# One stop Insurance Company Policy
# Date written: Nov 20, 2023
# Author: Ifiyemi

# import required libraries
import datetime
import random
import FormatValues as FV # gave the library an alias that is not as long to type in.

# Set up program constants
NEXT_POL_NUM = 1944
BAS_PREM = 869.00
DISC_ADD_CAR = 25/100
EXT_LIA_COV_COST =  130
GLAS_COV_COST = 86.00
LOAN_CAR_COV_COST = 58.00
HST_RATE = 15/100
PRO_FEE = 39.99

# Set up program functions

def CalcMonthlyPay(TotCost, PayMeth):
    # Calculate monthly payment for monthly payment option or down payment options, to be fully paid in 8 months
    if PayMeth == "Monthly":
        MonthlyPay = (PRO_FEE + TotCost)/8
    elif PayMeth == "Down Payment":
        MonthlyPay = ((TotCost-DownPay) + PRO_FEE)/8
    elif PayMeth == "Full":
        MonthlyPay = 0
    return MonthlyPay

def CalcFirPayDate(InvDate):
    global FirPayDate
    # Calculate the First Payment Date as the first of the next month
    
    CurDate = datetime.datetime.now() # Grab the current date from the system date
    InvDate = CurDate

    InvYear = InvDate.year
    InvMonth = InvDate.month + 1
    InvDay =  1 # day is set to 1. InvDay = InvDate.day

    
    if InvMonth > 12:
        InvMonth -= 12
        InvYear +=1

    FirPayDate = datetime.datetime(InvYear, InvMonth, InvDay)

    return FirPayDate
    

# Start the main program
while True:
    FirstName = input("Enter Customer First Name: ").title()
    LastName = input("Enter Customer Last Name: ").title()
    StAdd = input("Enter Customer Address: ")
    city = input("Enter the customer city: ").title()
    ProvLst = [ "NL", "NS", "NB", "PE"]
    while True:
        Prov = input("Enter the Province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank - Please reenter.")
        elif len(Prov) !=2:
            print("Error - Province is a 2 digit code - Please reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province - Please reenter.")
        else:
            break

    PostCode = input("Enter Postal Code(X9X 9X9): ")
    PhoneNum = input("Enter Customer Phone Number(999)-999-9999): ")
    PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
    NumCars = int(input("Enter the Number of cars being Insured: "))
    ExtLiab = input("Enter Option for Extra Liability up to $1,000,000(Y or N): ").upper()
    GlaCov = input("Enter Option for Glass Coverage(Y or N): ").upper()
    CarLoan = input("Enter Option for Car Loaner(Y or N): ").upper()
    PayLst = ["Full", "Monthly", "Down Payment"]
    while True:
        PayMeth = input("Enter Payment Method(Full, Monthly, Down Payment): ").title()
        if PayMeth == "":
            print("Error - Payment Method cannot be blank - Please reenter.")
        elif PayMeth not in PayLst:
            print("Error - invalid entry - must be Full, Monthly or Down Payment - Please reenter.")
        else:
            break
    
    if PayMeth == "Down Payment":
        DownPay = float(input("Enter Down Payment Amount: "))
    elif PayMeth == "Full":
        DownPay = 0

    ClaimNumLst = []
    ClaimDateLst = []
    ClaimCostLst = []

    while True:
        ClaimNum = (input("Enter the Claim Number(Enter to end): "))
        if ClaimNum == "":
            break
        ClaimDate = input("Enter the Claim Date(YYYY-MM-DD): ")
        ClaimDate =  datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
        ClaimCost = float(input("Enter the Total Claim Cost: "))

        ClaimNumLst.append(ClaimNum)
        print(ClaimNumLst)
        ClaimDateLst.append(ClaimDate)
        print(ClaimDateLst)
        ClaimCostLst.append(ClaimCost)
        print(ClaimCostLst)

    # Calculations:
    Auto = BAS_PREM 
    if NumCars > 1:
        Auto = BAS_PREM + (NumCars * (BAS_PREM * DISC_ADD_CAR))
    TotExtCost = EXT_LIA_COV_COST + GLAS_COV_COST + LOAN_CAR_COV_COST
    TotInsPrem = TotExtCost + Auto
    Hst = TotInsPrem * HST_RATE
    TotCost = TotInsPrem + Hst
    MonthlyPay = CalcMonthlyPay(TotCost, PayMeth)

    CurDate = datetime.datetime.now() # Grab the current date from the system date
    InvDate = CurDate.strftime("%Y-%m-%d")
    FirstPayDate = CalcFirPayDate(InvDate)
    

    # Display Results
    print()
    print(f"ONE STOP INSURANCE COMPANY")
    print(f"INSURANCE POLICY CLAIMS FORM")
    print()        
    print(f"Invoice Date: {FV.FDateM(CurDate):<10}               Next Policy Number: {NEXT_POL_NUM:>4}")
    print(f"===============================================================")
    print()
    print(f"{FirstName[0]:<1s}, {LastName:<10s}")
    print(f"--------------------------------")
    print(f"{StAdd:<20s}")
    print(f"--------------------------------")
    print(f"{city:<10s}    {Prov:<2s},     {PostCode:<7s} ")
    print(f"--------------------------------")
    print(f"{PhoneNum:<10}")
    print(f"--------------------------------")
    print()
    print(f"Number of Cars Insured:      {NumCars:>2d}  ")
    print()
    print(f"Extra Liability: {ExtLiab:<3s}       Glass Coverage: {ExtLiab:<3s}       Car Loan: {CarLoan:<3s}")
    print()
    print(f"               Base Premium including Additional Cars: {FV.FDollar2(Auto):>9s}")
    print()
    print(f"                                     Total Extra Cost: {FV.FDollar2(TotExtCost):>9s}")
    print()
    print(f"                                    Insurance Premium: {FV.FDollar2(TotInsPrem):>9s}")
    print()
    print(f"                                                  HST: {FV.FDollar2(Hst):>9s}")
    print(f"                                                       _________")
    print()
    print
    print(f"                                           Total Cost: {FV.FDollar2(TotCost):>9s}")
    print()
    print(f"================================================================")
    print(f"Payment Method: {PayMeth:<12s}      Monthly Payment Amount: {FV.FDollar2(MonthlyPay):<12s}")
    print()
    print(f"Down Payment Amount: {FV.FDollar2(DownPay):<9s}    First Payment Date: {FV.FDateS(FirstPayDate):>10}")

    print()
    print(f"Claim #         Claim Date             Amount   ")
    print(f"-----------------------------------------------")
    Index = 0
    for Claim in ClaimNumLst:
        print(f" {str(ClaimNumLst[Index])}            {str(ClaimDateLst[Index])}     {FV.FDollar2(ClaimCostLst[Index]):<9s}")
        Index +=1

    print()
    print(f"          Thank you for being our valued Customer")
    print()
    while True:
        Continue = input("Do you want to continue (Y / N): ").upper()
 
        if Continue != "Y" and Continue != "N":
            print("Must enter a Y or N - please re-enter.")
        else:
            break
    
    if Continue == "N":
        break
 
print()
print("Thank you and have a nice day!")    


