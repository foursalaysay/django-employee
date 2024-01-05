function enableEdit() {
  const formElements = ['id', 'name', 'position', 'email', 'contact', 'address', 'photo-upload'];

  formElements.forEach(elementId => {
    document.getElementById(elementId).disabled = false;
  });

  // Show the Save button and hide the Edit button
  document.getElementById('edit-btn').style.display = 'none';
  document.getElementById('save-btn').style.display = 'inline-block';

  triggerFileInput(); // Trigger file input click
}

function triggerFileInput() {
  document.getElementById('photo-upload').click();
}

function previewPhoto(event) {
  const input = event.target;
  const photo = document.getElementById('profile-photo');

  const reader = new FileReader();
  reader.onload = function () {
    photo.src = reader.result;
  };

  if (input.files && input.files[0]) {
    reader.readAsDataURL(input.files[0]);
  }
}

function clearFileInput() {
  document.getElementById('photo-upload').value = '';
}

function setDefaultPhoto() {
  document.getElementById('profile-photo').src = 'profile-photo.jpg';
}

function saveChanges() {
  // Add logic to save the changes or perform any necessary actions
  // For example, you can send the updated data to a server or update a local storage
  alert('Changes saved!');
  disableEdit(); // Call this function to disable editing after saving
}

function disableEdit() {
  const formElements = ['id', 'name', 'position', 'email', 'contact', 'address', 'photo-upload'];

  formElements.forEach(elementId => {
    document.getElementById(elementId).disabled = true;
  });

  // Show the Edit button and hide the Save button
  document.getElementById('edit-btn').style.display = 'inline-block';
  document.getElementById('save-btn').style.display = 'none';
}

function submitAttendance() {
  const status = document.getElementById('attendance-status').value;
  const date = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  const entry = document.createElement('li');
  entry.textContent = `Date: ${date} - Status: ${status}`;
  document.getElementById('attendance-history').appendChild(entry);

  clearFileInput();
  setDefaultPhoto();
}

$(document).ready(function () {
  $('#real-calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    defaultDate: new Date(),
    navLinks: true,
    editable: true,
    eventLimit: true,
    events: [
      {
        title: 'Meeting',
        start: '2023-01-01T10:00:00',
        end: '2023-01-01T12:00:00'
      },
      {
        title: 'Conference',
        start: '2023-01-05',
        end: '2023-01-07'
      },
      // Add more events as needed
    ]
  });
});
