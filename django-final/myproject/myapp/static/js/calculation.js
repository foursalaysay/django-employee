// EMPLOYEE SALARY CALCULATIONS
//SALARY PER MONTH

function deductionValues(){
    // ... (the rest of your JavaScript code)
    // PROVIDE THE ID OF INPUTTED DATA SALARY FROM ADMIN INPUT
    
    var getBasic;

    var selectedValue = document.getElementById("employmentType").value;

    if (selectedValue === 'regular'){
        getBasic = 30000;
    }else if (selectedValue === 'contractual'){
        getBasic = 25000;
    }else{
        getBasic = 20000;
    }


    // Your existing calculations
    let SSS = getBasic * 0.045;
    let philhealth = getBasic * 0.05;
    let pagibig = getBasic * 0.02;

    let totalDeduction = SSS + philhealth + pagibig;
    let netPay = getBasic - totalDeduction;

    // Set the calculated values in the corresponding input fields
    document.getElementById('basic-salary').value = calculateBasicSalary(getBasic).toFixed(2);
    document.getElementById('sss').value = SSS.toFixed(2);
    document.getElementById('philhealth').value = philhealth.toFixed(2);
    document.getElementById('pagibig').value = pagibig.toFixed(2);
    document.getElementById('tax').value = 
    document.getElementById('total-deduction').value = totalDeduction.toFixed(2);
    document.getElementById('net-pay').value = netPay.toFixed(2);
}

// Function to calculate basic salary
function calculateBasicSalary(salary) {
    // Implement your calculation logic for basic salary
    // Example: 80% of the input salary
    return salary * 0.8;
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




