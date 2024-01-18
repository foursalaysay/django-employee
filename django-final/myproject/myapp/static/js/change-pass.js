     



    
     const newPasswordInput = document.getElementById('new-password');
     const showPasswordCheckbox = document.getElementById('showPassword');
     

     showPasswordCheckbox.addEventListener('change', function() {
         // If the checkbox is checked, change the input type to 'text'; otherwise, set it back to 'password'
         newPasswordInput.type = this.checked ? 'text' : 'password';
     });
     
     function showPasswordContainer() {
        var changePassContainer = document.querySelector('.change-pass');
        changePassContainer.style.display = (changePassContainer.style.display === 'block') ? 'none' : 'block';
    }