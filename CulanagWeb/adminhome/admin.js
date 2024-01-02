function addEmployee() {
    var idNum = $("#idNum").val();
    var fullName = $("#fullName").val();
    var contactNum = $("#contactNum").val();
    var position = $("#position").val();
    var typeOfLeave = $("#typeOfLeave").val();
    var leaveCount = $("#leaveCount").val();

    // Reset error messages
    $("#fullNameError").text("");
    $("#contactNumError").text("");
    $("#leaveCountError").text("");
    $("#generalError").text("");

    // Validate Full Name
    if (!/^[a-zA-Z\s]+$/.test(fullName)) {
        $("#fullNameError").text("Full Name should contain only letters");
        return;
    }

    // Validate Contact Number
    if (!/^\d{11}$/.test(contactNum)) {
        $("#contactNumError").text("Contact Number should be 11 digits");
        return;
    }

    // Validate Leave Count
    if (!/^\d+$/.test(leaveCount)) {
        $("#leaveCountError").text("Leave Count should be a number");
        return;
    }

    // Validate the form is not blank
    if (!idNum || !fullName || !contactNum || !position || !typeOfLeave || !leaveCount) {
        $("#generalError").text("All fields are required");
        return;
    }

    var table = $("#employeeTableBody");
    var newRow = $("<tr>");

    newRow.append("<td>" + idNum + "</td>");
    newRow.append("<td>" + fullName + "</td>");
    newRow.append("<td>" + contactNum + "</td>");
    newRow.append("<td>" + position + "</td>");
    newRow.append("<td>" + typeOfLeave + "</td>");
    newRow.append("<td>" + leaveCount + "</td>");
    newRow.append('<td><button class="btn btn-warning" onclick="editEmployee(this)">Edit</button> ' +
        '<button class="btn btn-danger" onclick="deleteEmployee(this)">Delete</button></td>');

    table.append(newRow);

    var existingEmployees = JSON.parse(localStorage.getItem('employees')) || [];

    existingEmployees.push({
        idNum: idNum,
        fullName: fullName,
        contactNum: contactNum,
        position: position,
        typeOfLeave: typeOfLeave,
        leaveCount: leaveCount
    });

    localStorage.setItem('employees', JSON.stringify(existingEmployees));

    $("#form")[0].reset();
}

function displayEmployeeList() {
    var table = $("#employeeTableBody");
    table.empty();

    var existingEmployees = JSON.parse(localStorage.getItem('employees')) || [];

    for (var i = 0; i < existingEmployees.length; i++) {
        var newRow = $("<tr>");

        newRow.append("<td>" + existingEmployees[i].idNum + "</td>");
        newRow.append("<td>" + existingEmployees[i].fullName + "</td>");
        newRow.append("<td>" + existingEmployees[i].contactNum + "</td>");
        newRow.append("<td>" + existingEmployees[i].position + "</td>");
        newRow.append("<td>" + existingEmployees[i].typeOfLeave + "</td>");
        newRow.append("<td>" + existingEmployees[i].leaveCount + "</td>");
        newRow.append('<td><button class="btn btn-warning" onclick="editEmployee(this)">Edit</button> ' +
            '<button class="btn btn-danger" onclick="deleteEmployee(this)">Delete</button></td>');

        table.append(newRow);
    }
}

function editEmployee(button) {
    var row = $(button).closest("tr");
    var columns = row.find("td");

    $("#idNum").val(columns[0].innerText);
    $("#fullName").val(columns[1].innerText);
    $("#contactNum").val(columns[2].innerText);
    $("#position").val(columns[3].innerText);
    $("#typeOfLeave").val(columns[4].innerText);
    $("#leaveCount").val(columns[5].innerText);
}

function updateEmployee() {
    var idNum = $("#idNum").val();
    var fullName = $("#fullName").val();
    var contactNum = $("#contactNum").val();
    var position = $("#position").val();
    var typeOfLeave = $("#typeOfLeave").val();
    var leaveCount = $("#leaveCount").val();

    $("#fullNameError").text("");
    $("#contactNumError").text("");
    $("#leaveCountError").text("");
    $("#generalError").text("");

    if (!/^[a-zA-Z\s]+$/.test(fullName)) {
        $("#fullNameError").text("Full Name should contain only letters");
        return;
    }

    if (!/^\d{11}$/.test(contactNum)) {
        $("#contactNumError").text("Contact Number should be 11 digits");
        return;
    }

    if (!/^\d+$/.test(leaveCount)) {
        $("#leaveCountError").text("Leave Count should be a number");
        return;
    }

    if (!idNum || !fullName || !contactNum || !position || !typeOfLeave || !leaveCount) {
        $("#generalError").text("All fields are required");
        return;
    }

    validateAndUpdateEmployee(idNum, fullName, contactNum, position, typeOfLeave, leaveCount);

    updateEmpInfoTable();

    $("#form")[0].reset();
}

function validateAndUpdateEmployee(idNum, fullName, contactNum, position, typeOfLeave, leaveCount) {
    var existingEmployees = JSON.parse(localStorage.getItem('employees')) || [];

    for (var i = 0; i < existingEmployees.length; i++) {
        if (existingEmployees[i].idNum === idNum) {
            existingEmployees[i].fullName = fullName;
            existingEmployees[i].contactNum = contactNum;
            existingEmployees[i].position = position;
            existingEmployees[i].typeOfLeave = typeOfLeave;
            existingEmployees[i].leaveCount = leaveCount;
            break;
        }
    }

    localStorage.setItem('employees', JSON.stringify(existingEmployees));
}

function updateEmpInfoTable() {
    var existingEmployees = JSON.parse(localStorage.getItem('employees')) || [];
    var table = $("#employeeTableBody");
    table.empty();

    for (var i = 0; i < existingEmployees.length; i++) {
        var newRow = $("<tr>");

        newRow.append("<td>" + existingEmployees[i].idNum + "</td>");
        newRow.append("<td>" + existingEmployees[i].fullName + "</td>");
        newRow.append("<td>" + existingEmployees[i].contactNum + "</td>");
        newRow.append("<td>" + existingEmployees[i].position + "</td>");
        newRow.append("<td>" + existingEmployees[i].typeOfLeave + "</td>");
        newRow.append("<td>" + existingEmployees[i].leaveCount + "</td>");
        newRow.append('<td><button class="btn btn-warning" onclick="editEmployee(this)">Edit</button> ' +
            '<button class="btn btn-danger" onclick="deleteEmployee(this)">Delete</button></td>');

        table.append(newRow);
    }
}

function deleteEmployee(button) {
    var row = $(button).closest("tr");
    var idNumToDelete = row.find("td:eq(0)").text();

    row.remove();

    var existingEmployees = JSON.parse(localStorage.getItem('employees')) || [];
    var updatedEmployees = existingEmployees.filter(function (employee) {
        return employee.idNum !== idNumToDelete;
    });

    localStorage.setItem('employees', JSON.stringify(updatedEmployees));
}

displayEmployeeList();
