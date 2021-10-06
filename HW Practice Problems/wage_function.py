#Function to calculate take home pay
def calc_pay(iHours, fWage, fTax, fFICA):
    #Determine take home pay before taxes and FICA (rounded to 2 decimals)
    iPay = iHours * fWage
    round(iPay, 2)
    #Turn fTAx and fFICA inputs into decimals
    fTAxDecimal = fTax * 0.01
    fFICADecimal = fFICA * 0.01
    #Apply tax and FICA rates to total pay (round to 2 decimals)
    iTotalPay = round(iPay * (1 - (fTAxDecimal + fFICADecimal)), 2)

    #Return the total pay after taxes and FICA
    return iTotalPay