// EMPLOYEE SALARY CALCULATIONS
//SALARY PER MONTH

// DECLARE ABSENT SERVES AS MINUS TO THE DAYS WORK


function deductionValues(){

      // PROVIDE THE ID OF INPUTTED DATA SALARY FROM ADMIN INPUT
      var getBasicValue = document.getElementById('salary');
      var getBasic = getBasicValue.value;
  
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
    let netPayValue = document.getElementById("net-pay")

    salaryValue.textContent = getBasic;
    SSSValue.textContent = SSS;
    philhealthValue.textContent = philhealth;
    pagIbigValue.textContent = pagibig;
    totalDeductionValue.textContent = totalDeduction.toFixed(2);
    netPayValue.textContent= netPay.toFixed(2);
}



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




