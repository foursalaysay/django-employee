// Function to add employee
function addEmployee() {
    var idNum = document.getElementById("idNum").value;
    var fullName = document.getElementById("fullName").value;
    var position = document.getElementById("position").value;
    var leaveCount = parseInt(document.getElementById("leaveCount").value);

    // Validate the form is not blank
    if (!idNum || !fullName || !position || isNaN(leaveCount)) {
        alert("All fields are required");
        return;
    }

    var table = document.getElementById("employeeTableBody");
    var newRow = table.insertRow();

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);

    cell1.innerHTML = idNum;
    cell2.innerHTML = fullName;
    cell3.innerHTML = position;
    cell4.innerHTML = leaveCount;

    // Calculate and display salary
    var salary = calculateSalary(position, leaveCount);
    cell5.innerHTML = salary;

    // Add edit and delete buttons
    cell6.innerHTML = '<button onclick="editEmployee(this)">Edit</button>' +
                      '<button onclick="deleteEmployee(this)">Delete</button>';

    // Clear the form fields after adding an employee
    document.getElementById("form").reset();
}

// Function to calculate salary based on position and leave count
function calculateSalary(position, leaveCount) {
    var baseSalary;

    switch (position) {
        case 'Regular':
            baseSalary = 50000;
            break;
        case 'Irregular':
            baseSalary = 40000;
            break;
        case 'PartTime':
            baseSalary = 30000;
            break;
        default:
            baseSalary = 0;
    }

    // Deduct 1000 for each leave day
    var deductedSalary = baseSalary - (leaveCount * 1000);

    // Ensure salary is not negative
    return Math.max(deductedSalary, 0);
}

// Function to edit employee
function editEmployee(button) {
    var row = button.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");

    var idNum = cells[0].innerText;
    var fullName = cells[1].innerText;
    var position = cells[2].innerText;
    var leaveCount = cells[3].innerText;

    // Populate the form with the selected employee's data
    document.getElementById("idNum").value = idNum;
    document.getElementById("fullName").value = fullName;
    document.getElementById("position").value = position;
    document.getElementById("leaveCount").value = leaveCount;

    // Remove the row from the table
    row.remove();
}

// Function to delete employee
function deleteEmployee(button) {
    var row = button.parentNode.parentNode;
    row.remove();
}
