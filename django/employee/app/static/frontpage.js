document.addEventListener('DOMContentLoaded', function() {
    const adminButton = document.getElementById('admin-button');
    const employeeButton = document.getElementById('employee-button');
    const backToSignUpAdmin = document.getElementById('back-to-signup-admin');
    const backToSignUpEmployee = document.getElementById('back-to-signup-employee');
    const welcomeForm = document.getElementById('welcome-form');
    const adminForm = document.getElementById('admin-form');
    const employeeForm = document.getElementById('employee-form');
    const employeeProfile = document.getElementById('employee-profile');
  
    adminButton.addEventListener('click', function() {
      welcomeForm.style.display = 'none';
      adminForm.style.display = 'block';
      employeeForm.style.display = 'none';
      employeeProfile.style.display = 'none';
    });
  
    employeeButton.addEventListener('click', function() {
      welcomeForm.style.display = 'none';
      adminForm.style.display = 'none';
      employeeForm.style.display = 'block';
      employeeProfile.style.display = 'none';
    });
  
    backToSignUpAdmin.addEventListener('click', function() {
      welcomeForm.style.display = 'block';
      adminForm.style.display = 'none';
      employeeForm.style.display = 'none';
      employeeProfile.style.display = 'none';
    });
  
    backToSignUpEmployee.addEventListener('click', function() {
      welcomeForm.style.display = 'block';
      adminForm.style.display = 'none';
      employeeForm.style.display = 'none';
      employeeProfile.style.display = 'none';
    });
  
    document.getElementById('logout-employee').addEventListener('click', function() {
      welcomeForm.style.display = 'block';
      adminForm.style.display = 'none';
      employeeForm.style.display = 'none';
      employeeProfile.style.display = 'none';
    });
  });
  
  