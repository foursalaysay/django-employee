// EMPLOYEE SALARY CALCULATIONS
//SALARY PER MONTH

// DECLARE ABSENT SERVES AS MINUS TO THE DAYS WORK

function getSalary(){
    // PROVIDE THE ID OF INPUTTED DATA SALARY FROM ADMIN INPUT
    var getBasicValue = document.getElementById('')
    var getBasic = getBasicValue.value;

    var SSS = getBasic * 0.045;
    var philhealth = getBasic * 0.05;
    var pagibig = getBasic * 0.02;

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




