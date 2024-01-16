// EMPLOYEE SALARY CALCULATIONS
//SALARY PER MONTH

// DECLARE ABSENT SERVES AS MINUS TO THE DAYS WORK


function deductionValues() {
    // ... (the rest of your JavaScript code)
    // PROVIDE THE ID OF INPUTTED DATA SALARY FROM ADMIN INPUT
    var getBasicValue = document.getElementById('salary');
    var getBasic = parseFloat(getBasicValue.value);

    let SSS = getBasic * 0.045;
    let philhealth = getBasic * 0.05;
    let pagibig = getBasic * 0.02;

    let totalDeduction = SSS + philhealth + pagibig;
    let netPay = getBasic - totalDeduction;

    let salaryValue = document.getElementById('basic-salary');
    let SSSValue = document.getElementById('sss');
    let philhealthValue = document.getElementById("philhealth");
    let pagIbigValue = document.getElementById("pagibig");
    let totalDeductionValue = document.getElementById("total-deduction");
    let netPayValue = document.getElementById("net-pay");

    salaryValue.value = getBasic.toFixed(2);
    SSSValue.value = SSS.toFixed(2);
    philhealthValue.value = philhealth.toFixed(2);
    pagIbigValue.value = pagibig.toFixed(2);
    totalDeductionValue.value = totalDeduction.toFixed(2);
    netPayValue.value = netPay.toFixed(2);
}

// Set up event listener when the page loads
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('calculateBtn').addEventListener('click', deductionValues);
});



// PUT THIS ONCHANGE ON INPUT OF ABSENT
function getValue() {
    // GET ID OF INPUTTED DAYS OF ABSENT
    var inputElement = document.getElementById("myInput");
    var inputValue = inputElement.value;
    console.log("Input value:", inputValue);

    var getInputTotalDays = document.getElementById("");
    // MAO NI ANG TOTAL WORKING DAYS
    var totalDaysWorked = getInputTotalDays.value - inputValue;

    // KUNG HALFDAY GANE ABSENT NA NA


    var dayRate = document.getElementById('')
    var dayRateValue = inputRate.value;
}




