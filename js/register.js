

window.addEventListener('DOMContentLoaded', () => {

    const getRegisterForm = document.querySelector('#register-scroll')
    if(getRegisterForm.scrollHeight > getRegisterForm.clientHeight){
        getRegisterForm.classList.add('overscroll');
    }
  });