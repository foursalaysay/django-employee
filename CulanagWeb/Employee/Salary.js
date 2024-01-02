function calculateSalary() {
    var employeeId = document.getElementById("employeeId").value;
    var employeeName = document.getElementById("employeeName").value;
    var employeeContact = document.getElementById("employeeContact").value;
    var employeeType = document.getElementById("employeeType").value;
    var absences = parseInt(document.getElementById("absences").value) || 0;

    var baseSalary;
    switch (employeeType) {
        case "Regular":
            baseSalary = 50000;
            break;
        case "Irregular":
            baseSalary = 40000;
            break;
        case "Part-Time":
            baseSalary = 30000;
            break;
        default:
            displayResult("Invalid employee type");
            return;
    }

    var salary = baseSalary - (absences * 1000); // Deduct $1000 for each absence

    displayResult(`Employee ID: ${employeeId}<br>
                   Name: ${employeeName}<br>
                   Contact: ${employeeContact}<br>
                   Employee Type: ${employeeType}<br>
                   Base Salary: $${baseSalary}<br>
                   Deductions (${absences} absences): -$${absences * 1000}<br>
                   Total Salary: $${salary}`);
}

function displayResult(result) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = result;
}
