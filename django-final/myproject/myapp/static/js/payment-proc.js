function openDialog(username, name, address) {
    document.getElementById('dialog').style.display = 'block';
    document.getElementById('employee-username').innerText = username;

    // Set input field values
    document.getElementById('employee-username-input').value = username;
    document.getElementById('employee-name-input').value = name;
    document.getElementById('employee-address-input').value = address;

    // Get the current date and update the 'current-date' input
    const currentDate = new Date();
    const formattedDate = currentDate.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
    document.getElementById('current-date-input').value = formattedDate;
}

function closeDialog() {
    document.getElementById('dialog').style.display = 'none';
}
// function updateCurrentDate() {
//     const currentDate = new Date();
//     const options = { year: 'numeric', month: 'long', day: 'numeric' };
//     const formattedDate = currentDate.toLocaleDateString('en-US', options);

//     document.getElementById('current-date').innerText = formattedDate;
// }

// // Call the function to update the date when the page loads
// updateCurrentDate();

// // Optionally, update the date periodically (e.g., every second)
// setInterval(updateCurrentDate, 1000);

var currentDate = new Date();

  // Format the date as YYYY-MM-DD (you can change the format as needed)
  var formattedDate = currentDate.toISOString().slice(0, 10);

  // Set the formatted date to the input field
  window.onload = function() {
    document.getElementById("current-date-input").value = formattedDate;
  };