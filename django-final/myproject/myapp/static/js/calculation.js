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

    let tax;

    if (getBasic <= 20833){
        tax = 0;
    }else if (getBasic >= 20833 && getBasic <= 33332){
        tax = getBasic * 0.20;
    }else if(getBasic >= 33332){
        tax= 2500 + (getBasic * 0.25);
    }


    // Your existing calculations
    let SSS = getBasic * 0.045;
    let philhealth = getBasic * 0.05;
    let pagibig = getBasic * 0.02;

    let totalDeduction = SSS + philhealth + pagibig + tax;
    let netPay = getBasic - totalDeduction;

    // Set the calculated values in the corresponding input fields
    document.getElementById('basic-salary').value = calculateBasicSalary(getBasic).toFixed(2);
    document.getElementById('sss').value = SSS.toFixed(2);
    document.getElementById('philhealth').value = philhealth.toFixed(2);
    document.getElementById('pagibig').value = pagibig.toFixed(2);
    document.getElementById('tax').value = tax.toFixed(2);
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





