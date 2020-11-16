import tkinter as tk

root = tk.Tk()
root.title("Wage Calculator")

def calculateWage():
    hourlyWage = hourlyWageEntry.get()
    sundayWage = sundayWageEntry.get()
    regHours = regHoursEntry.get()
    sunHours = sunHoursEntry.get()

    regDollarsPreTax = float(regHours) * float(hourlyWage)
    sunDollarsPreTax = float(sunHours) * float(sundayWage)
    preTaxTotal = regDollarsPreTax + sunDollarsPreTax

    taxRate = taxRateEnrty.get()
    taxRateDecimal = ((100 - float(taxRate)) / 100)

    postTaxDollars = preTaxTotal * taxRateDecimal

    result = tk.Tk()
    result.title("Result")

    resultLabelPreTax = tk.Label(result, text="You will earn ${} pre-tax.".format(preTaxTotal))
    resultLabelPostTax = tk.Label(result, text="You will earn ${} post-tax.".format(postTaxDollars))
    okButton = tk.Button(result, text="OK", command=lambda: result.destroy())

    resultLabelPreTax.pack()
    resultLabelPostTax.pack()
    okButton.pack()

    result.mainloop()

instructionsLabel = tk.Label(root, text="Thanks for using.\nDon't leave fields blank, enter 0 instead.")
hourlyWageLabel = tk.Label(root, text="Hourly wage in $")
sundayWagelabel = tk.Label(root, text="Sunday wage in $")
regHoursLabel = tk.Label(root, text="Regular Hours Worked")
sunHoursLabel = tk.Label(root, text="Sunday Hours Worked")
taxRateLabel = tk.Label(root, text="Tax Rate in %")

hourlyWageEntry = tk.Entry(root)
sundayWageEntry = tk.Entry(root)
regHoursEntry = tk.Entry(root)
sunHoursEntry = tk.Entry(root)
taxRateEnrty = tk.Entry(root)

calculateButton = tk.Button(root, text="Calculate Wages", command=calculateWage)

instructionsLabel.grid(row=0, column=0, columnspan=2)
hourlyWageLabel.grid(row=1, column=0)
sundayWagelabel.grid(row=2, column=0)
regHoursLabel.grid(row=3, column=0)
sunHoursLabel.grid(row=4, column=0)
taxRateLabel.grid(row=5, column=0)

hourlyWageEntry.grid(row=1, column=1)
sundayWageEntry.grid(row=2, column=1)
regHoursEntry.grid(row=3, column=1)
sunHoursEntry.grid(row=4, column=1)
taxRateEnrty.grid(row=5, column=1)

calculateButton.grid(row=6, column=0, columnspan=2)

root.mainloop()